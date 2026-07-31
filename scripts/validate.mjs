#!/usr/bin/env node

import { readdir, readFile, stat } from "node:fs/promises";
import path from "node:path";
import process from "node:process";

const root = process.cwd();
const expectedSkills = ["ohada-legal-practice", "website-legal-compliance"];
const errors = [];

const fail = (message) => errors.push(message);
const readJson = async (relativePath) =>
  JSON.parse(await readFile(path.join(root, relativePath), "utf8"));
const unique = (values) => new Set(values).size === values.length;
const sameMembers = (left, right) =>
  left.length === right.length && [...left].sort().join("\n") === [...right].sort().join("\n");

async function walk(directory) {
  const entries = await readdir(directory, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    const target = path.join(directory, entry.name);
    if (entry.isDirectory()) files.push(...(await walk(target)));
    else if (entry.isFile()) files.push(target);
  }
  return files;
}

function parseFrontmatter(content, skillId) {
  const match = content.match(/^---\n([\s\S]*?)\n---(?:\n|$)/);
  if (!match) {
    fail(`${skillId}: missing YAML frontmatter`);
    return {};
  }

  const properties = {};
  for (const line of match[1].split("\n")) {
    const separator = line.indexOf(":");
    if (separator < 1) {
      fail(`${skillId}: unsupported frontmatter line: ${line}`);
      continue;
    }
    const key = line.slice(0, separator).trim();
    let value = line.slice(separator + 1).trim();
    if (
      (value.startsWith('"') && value.endsWith('"')) ||
      (value.startsWith("'") && value.endsWith("'"))
    ) {
      value = value.slice(1, -1);
    }
    properties[key] = value;
  }

  const keys = Object.keys(properties).sort();
  if (keys.join(",") !== "description,name") {
    fail(`${skillId}: frontmatter must contain only name and description`);
  }
  if (properties.name !== skillId) fail(`${skillId}: name must match its directory`);
  if (!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(properties.name ?? "")) {
    fail(`${skillId}: invalid skill name`);
  }
  if (!properties.description || properties.description.length > 1024) {
    fail(`${skillId}: description must contain 1 to 1024 characters`);
  }
  return properties;
}

async function validateSkill(skill) {
  const directory = path.join(root, skill.path);
  const entrypoint = path.join(directory, "SKILL.md");
  const content = await readFile(entrypoint, "utf8");
  parseFrontmatter(content, skill.id);

  if (content.split("\n").length > 500) fail(`${skill.id}: SKILL.md exceeds 500 lines`);
  if (await stat(path.join(directory, "agents")).then(() => true).catch(() => false)) {
    fail(`${skill.id}: harness metadata must live under adapters/`);
  }

  const markdownFiles = (await walk(directory)).filter((file) => file.endsWith(".md"));
  for (const file of markdownFiles) {
    const relative = path.relative(root, file);
    const markdown = await readFile(file, "utf8");
    if (/\/Users\//.test(markdown)) fail(`${relative}: contains an absolute private path`);
    if (/\$[a-z0-9]+(?:-[a-z0-9]+)+/i.test(markdown)) {
      fail(`${relative}: contains harness-specific $skill invocation syntax`);
    }

    const linkPattern = /\[[^\]]*\]\(([^)]+)\)/g;
    for (const match of markdown.matchAll(linkPattern)) {
      const target = match[1].split("#", 1)[0];
      if (!target || /^(?:https?:|mailto:)/.test(target)) continue;
      const resolved = path.resolve(path.dirname(file), target);
      if (!resolved.startsWith(`${directory}${path.sep}`)) {
        fail(`${relative}: relative link escapes the skill directory: ${target}`);
        continue;
      }
      const exists = await stat(resolved).then(() => true).catch(() => false);
      if (!exists) fail(`${relative}: broken relative link: ${target}`);
    }
  }
}

const catalogue = await readJson("catalog/marketplace.json");
const collection = await readJson("collections/legal.json");
await readJson("catalog/schemas/marketplace.schema.json");
await readJson("catalog/schemas/collection.schema.json");

if (catalogue.schemaVersion !== "1.0") fail("catalogue: unsupported schemaVersion");
if (catalogue.marketplace?.id !== "skill-market") fail("catalogue: invalid marketplace id");
if (!Array.isArray(catalogue.skills)) fail("catalogue: skills must be an array");

const discoveredSkills = (await readdir(path.join(root, "skills"), { withFileTypes: true }))
  .filter((entry) => entry.isDirectory())
  .map((entry) => entry.name);
const declaredSkills = catalogue.skills.map((skill) => skill.id);

if (!sameMembers(discoveredSkills, expectedSkills)) {
  fail(`skills/: expected only ${expectedSkills.join(", ")}`);
}
if (!sameMembers(declaredSkills, expectedSkills)) {
  fail(`catalogue: expected only ${expectedSkills.join(", ")}`);
}
if (!unique(declaredSkills)) fail("catalogue: duplicate skill ids");

const categories = new Set(catalogue.categories.map((category) => category.id));
const tags = new Set(catalogue.tags.map((tag) => tag.id));
for (const skill of catalogue.skills) {
  if (skill.path !== `skills/${skill.id}`) fail(`${skill.id}: catalogue path mismatch`);
  if (!categories.has(skill.category)) fail(`${skill.id}: unknown category ${skill.category}`);
  for (const tag of skill.tags) if (!tags.has(tag)) fail(`${skill.id}: unknown tag ${tag}`);
  if (!unique(skill.tags)) fail(`${skill.id}: duplicate tags`);
  const installHarnesses = skill.compatibility?.installTested?.map((entry) => entry.harness) ?? [];
  if (!sameMembers(installHarnesses, ["claude-code", "codex", "cursor"])) {
    fail(`${skill.id}: expected isolated install evidence for Claude Code, Codex, and Cursor`);
  }
  const runtimeEvidence = skill.compatibility?.runtimeTested ?? [];
  if (!sameMembers(runtimeEvidence, ["codex-cli@0.145.0 (2026-07-31)"])) {
    fail(`${skill.id}: runtime evidence must match the verified Codex invocation`);
  }
  await validateSkill(skill);
}

if (collection.schemaVersion !== "1.0" || collection.id !== "legal") {
  fail("collection: expected legal schemaVersion 1.0");
}
if (!sameMembers(collection.skills, expectedSkills)) {
  fail(`collection legal: expected only ${expectedSkills.join(", ")}`);
}
if (!unique(collection.skills)) fail("collection legal: duplicate skill ids");

const collectionEntry = catalogue.collections.find((entry) => entry.id === "legal");
if (collectionEntry?.manifest !== "collections/legal.json") {
  fail("catalogue: legal collection manifest mismatch");
}

for (const skillId of expectedSkills) {
  const overlay = path.join(
    root,
    "adapters",
    "codex-openai",
    "overlays",
    skillId,
    "agents",
    "openai.yaml"
  );
  const content = await readFile(overlay, "utf8");
  if (!content.includes(`$${skillId}`)) {
    fail(`${skillId}: OpenAI adapter default prompt must mention $${skillId}`);
  }
}

if (errors.length) {
  console.error(`Validation failed with ${errors.length} error(s):`);
  for (const error of errors) console.error(`- ${error}`);
  process.exit(1);
}

console.log(`Validated ${expectedSkills.length} canonical skills and collection legal.`);
