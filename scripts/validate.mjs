#!/usr/bin/env node

import { readdir, readFile, stat } from "node:fs/promises";
import path from "node:path";
import process from "node:process";

const root = process.cwd();
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

async function validateFigmaEdition(skill, edition) {
  const expectedPath = `figma-skills/${skill.id}/SKILL.md`;
  if (edition.path !== expectedPath) {
    fail(`${skill.id}: Figma edition path must be ${expectedPath}`);
  }
  if (!sameMembers(edition.targets ?? [], ["figma-agent", "figma-make"])) {
    fail(`${skill.id}: Figma edition must target Figma Agent and Figma Make`);
  }

  const entrypoint = path.join(root, edition.path);
  const directory = path.dirname(entrypoint);
  const content = await readFile(entrypoint, "utf8").catch(() => "");
  if (!content) {
    fail(`${skill.id}: missing standalone Figma edition`);
    return;
  }

  parseFrontmatter(content, skill.id);
  if (content.split("\n").length > 500) fail(`${skill.id}: Figma edition exceeds 500 lines`);
  if (/\/Users\//.test(content)) fail(`${skill.id}: Figma edition contains a private path`);
  if (/\$[a-z0-9]+(?:-[a-z0-9]+)+/i.test(content)) {
    fail(`${skill.id}: Figma edition contains harness-specific $skill syntax`);
  }
  if (/\bmcp__[a-z0-9_.-]+/i.test(content)) {
    fail(`${skill.id}: Figma edition contains a harness-qualified MCP tool name`);
  }
  if (/(?:references|scripts|assets)\/[a-z0-9._/-]+/i.test(content)) {
    fail(`${skill.id}: Figma edition references an unavailable bundled resource`);
  }

  const files = await walk(directory);
  if (files.length !== 1 || files[0] !== entrypoint) {
    fail(`${skill.id}: Figma edition must contain only one standalone SKILL.md file`);
  }

  const linkPattern = /\[[^\]]*\]\(([^)]+)\)/g;
  for (const match of content.matchAll(linkPattern)) {
    const target = match[1].split("#", 1)[0];
    if (target && !/^(?:https?:|mailto:)/.test(target)) {
      fail(`${skill.id}: Figma edition cannot reference bundled files: ${target}`);
    }
  }
}

const catalogue = await readJson("catalog/marketplace.json");
await readJson("catalog/schemas/marketplace.schema.json");
await readJson("catalog/schemas/collection.schema.json");

if (catalogue.schemaVersion !== "1.0") fail("catalogue: unsupported schemaVersion");
if (catalogue.marketplace?.id !== "balise") fail("catalogue: invalid marketplace id");
for (const field of ["categories", "tags", "skills", "collections"]) {
  if (!Array.isArray(catalogue[field])) fail(`catalogue: ${field} must be an array`);
}

const catalogueCategories = Array.isArray(catalogue.categories) ? catalogue.categories : [];
const catalogueTags = Array.isArray(catalogue.tags) ? catalogue.tags : [];
const catalogueSkills = Array.isArray(catalogue.skills) ? catalogue.skills : [];
const catalogueCollections = Array.isArray(catalogue.collections) ? catalogue.collections : [];
const readme = await readFile(path.join(root, "README.md"), "utf8");

const discoveredSkills = (await readdir(path.join(root, "skills"), { withFileTypes: true }))
  .filter((entry) => entry.isDirectory())
  .map((entry) => entry.name);
const declaredSkills = catalogueSkills.map((skill) => skill.id);

if (!sameMembers(discoveredSkills, declaredSkills)) {
  fail("skills/: directories must match catalogue skill ids");
}
if (!unique(declaredSkills)) fail("catalogue: duplicate skill ids");

const categoryIds = catalogueCategories.map((category) => category.id);
const tagIds = catalogueTags.map((tag) => tag.id);
const collectionIds = catalogueCollections.map((collection) => collection.id);
if (!unique(categoryIds)) fail("catalogue: duplicate category ids");
if (!unique(tagIds)) fail("catalogue: duplicate tag ids");
if (!unique(collectionIds)) fail("catalogue: duplicate collection ids");

const categories = new Map(catalogueCategories.map((category) => [category.id, category]));
const tags = new Set(tagIds);
for (const skill of catalogueSkills) {
  if (skill.path !== `skills/${skill.id}`) fail(`${skill.id}: catalogue path mismatch`);
  if (!categories.has(skill.category)) fail(`${skill.id}: unknown category ${skill.category}`);
  if (categories.get(skill.category)?.status !== "active") {
    fail(`${skill.id}: category ${skill.category} must be active`);
  }
  for (const tag of skill.tags) if (!tags.has(tag)) fail(`${skill.id}: unknown tag ${tag}`);
  if (!unique(skill.tags)) fail(`${skill.id}: duplicate tags`);
  const installHarnesses = skill.compatibility?.installTested?.map((entry) => entry.harness) ?? [];
  if (!sameMembers(installHarnesses, ["claude-code", "codex", "cursor"])) {
    fail(`${skill.id}: expected isolated install evidence for Claude Code, Codex, and Cursor`);
  }
  if (!unique(installHarnesses)) fail(`${skill.id}: duplicate install evidence`);
  const runtimeEvidence = skill.compatibility?.runtimeTested ?? [];
  if (!unique(runtimeEvidence)) fail(`${skill.id}: duplicate runtime evidence`);

  const editions = skill.editions ?? [];
  const editionIds = editions.map((edition) => edition.id);
  if (!unique(editionIds)) fail(`${skill.id}: duplicate edition ids`);
  const agentEdition = editions.find((edition) => edition.id === "agent-skills");
  if (!agentEdition) {
    fail(`${skill.id}: missing canonical Agent Skills edition`);
  } else {
    if (agentEdition.path !== skill.path) fail(`${skill.id}: Agent Skills edition path mismatch`);
    if (!sameMembers(agentEdition.targets ?? [], ["claude-code", "codex", "cursor"])) {
      fail(`${skill.id}: Agent Skills edition targets must match tested harnesses`);
    }
  }
  const figmaEdition = editions.find((edition) => edition.id === "figma");
  if (figmaEdition) await validateFigmaEdition(skill, figmaEdition);

  const sectionMatch = readme.match(
    new RegExp("### `" + skill.id + "`\\n([\\s\\S]*?)(?=\\n### `|\\n## )")
  );
  if (!sectionMatch) {
    fail(`${skill.id}: missing README section`);
  } else {
    const section = sectionMatch[1];
    if (!section.includes("assets/badges/agent-skills.svg")) {
      fail(`${skill.id}: README section is missing the Agent Skills badge`);
    }
    const hasFigmaAgentBadge = section.includes("assets/badges/figma-agent.svg");
    const hasFigmaMakeBadge = section.includes("assets/badges/figma-make.svg");
    if (figmaEdition && (!hasFigmaAgentBadge || !hasFigmaMakeBadge)) {
      fail(`${skill.id}: README section is missing Figma availability badges`);
    }
    if (!figmaEdition && (hasFigmaAgentBadge || hasFigmaMakeBadge)) {
      fail(`${skill.id}: README advertises an undeclared Figma edition`);
    }
  }
  await validateSkill(skill);

  for (const adapter of skill.compatibility?.adapters ?? []) {
    if (adapter !== "codex-openai") continue;
    const overlay = path.join(
      root,
      "adapters",
      "codex-openai",
      "overlays",
      skill.id,
      "agents",
      "openai.yaml"
    );
    const content = await readFile(overlay, "utf8").catch(() => "");
    if (!content.includes(`$${skill.id}`)) {
      fail(`${skill.id}: OpenAI adapter default prompt must mention $${skill.id}`);
    }
  }
}

const expectedFigmaEditions = catalogueSkills
  .filter((skill) => skill.editions?.some((edition) => edition.id === "figma"))
  .map((skill) => skill.id);
const discoveredFigmaEditions = (
  await readdir(path.join(root, "figma-skills"), { withFileTypes: true })
)
  .filter((entry) => entry.isDirectory())
  .map((entry) => entry.name);
if (!sameMembers(discoveredFigmaEditions, expectedFigmaEditions)) {
  fail("figma-skills/: directories must match declared Figma editions");
}

const expectedOpenAiOverlays = catalogueSkills
  .filter((skill) => skill.compatibility?.adapters?.includes("codex-openai"))
  .map((skill) => skill.id);
const discoveredOpenAiOverlays = (
  await readdir(path.join(root, "adapters", "codex-openai", "overlays"), { withFileTypes: true })
)
  .filter((entry) => entry.isDirectory())
  .map((entry) => entry.name);
if (!sameMembers(discoveredOpenAiOverlays, expectedOpenAiOverlays)) {
  fail("codex-openai: overlay directories must match declared adapters");
}

const declaredManifests = catalogueCollections.map((entry) => entry.manifest);
const discoveredManifests = (await readdir(path.join(root, "collections"), { withFileTypes: true }))
  .filter((entry) => entry.isFile() && entry.name.endsWith(".json"))
  .map((entry) => `collections/${entry.name}`);
if (!sameMembers(discoveredManifests, declaredManifests)) {
  fail("collections/: manifests must match catalogue collection entries");
}

for (const entry of catalogueCollections) {
  const collection = await readJson(entry.manifest);
  if (collection.schemaVersion !== "1.0") fail(`${entry.id}: unsupported collection schemaVersion`);
  if (collection.id !== entry.id) fail(`${entry.id}: collection id mismatch`);
  if (!unique(collection.skills)) fail(`${entry.id}: duplicate skill ids`);
  for (const skillId of collection.skills) {
    if (!declaredSkills.includes(skillId)) fail(`${entry.id}: unknown skill ${skillId}`);
  }
}

if (errors.length) {
  console.error(`Validation failed with ${errors.length} error(s):`);
  for (const error of errors) console.error(`- ${error}`);
  process.exit(1);
}

console.log(
  `Validated ${declaredSkills.length} canonical skills, ${expectedFigmaEditions.length} standalone Figma editions, and ${catalogueCollections.length} collections.`
);
