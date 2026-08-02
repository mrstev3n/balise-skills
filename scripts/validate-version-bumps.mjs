#!/usr/bin/env node

import { execFileSync } from "node:child_process";
import { readFile } from "node:fs/promises";
import path from "node:path";
import process from "node:process";

const root = process.cwd();
const baseRef = process.env.VERSION_BASE_REF || "origin/main";
const errors = [];
const semver = /^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$/;

function git(...args) {
  return execFileSync("git", args, {
    cwd: root,
    encoding: "utf8",
    stdio: ["ignore", "pipe", "pipe"]
  }).trim();
}

function readAtBase(relativePath) {
  try {
    return JSON.parse(git("show", `${baseRef}:${relativePath}`));
  } catch {
    return null;
  }
}

function isGreater(current, previous) {
  if (!semver.test(current) || !semver.test(previous)) return false;
  const left = current.split(".").map(Number);
  const right = previous.split(".").map(Number);
  return left.some((value, index) => value !== right[index] && value > right[index] &&
    left.slice(0, index).every((part, earlier) => part === right[earlier]));
}

function changedSkillIds(files) {
  const ids = new Set();
  const patterns = [
    /^skills\/([^/]+)\//,
    /^figma-skills\/([^/]+)\//,
    /^adapters\/codex-openai\/overlays\/([^/]+)\//
  ];
  for (const file of files) {
    for (const pattern of patterns) {
      const match = pattern.exec(file);
      if (match) ids.add(match[1]);
    }
  }
  return ids;
}

try {
  git("rev-parse", "--verify", `${baseRef}^{commit}`);
} catch {
  console.error(`Référence de comparaison introuvable : ${baseRef}`);
  process.exit(1);
}

const current = JSON.parse(await readFile(path.join(root, "catalog/marketplace.json"), "utf8"));
const previous = readAtBase("catalog/marketplace.json");
if (!previous) {
  console.error(`Catalogue introuvable sur ${baseRef}.`);
  process.exit(1);
}

const changedFiles = git("diff", "--name-only", baseRef).split("\n").filter(Boolean);
const currentSkills = new Map(current.skills.map((skill) => [skill.id, skill]));
const previousSkills = new Map(previous.skills.map((skill) => [skill.id, skill]));

for (const id of changedSkillIds(changedFiles)) {
  const skill = currentSkills.get(id);
  const oldSkill = previousSkills.get(id);
  if (!skill) {
    errors.push(`${id}: contenu modifié mais skill absent du catalogue actuel`);
    continue;
  }
  if (!oldSkill) continue;
  if (!isGreater(skill.version, oldSkill.version)) {
    errors.push(`${id}: la version doit être supérieure à ${oldSkill.version}`);
  }
  if (skill.updatedAt === oldSkill.updatedAt) {
    errors.push(`${id}: updatedAt doit changer avec le contenu du skill`);
  }
}

for (const file of changedFiles.filter((file) => /^collections\/[^/]+\.json$/.test(file))) {
  const collection = JSON.parse(await readFile(path.join(root, file), "utf8"));
  const oldCollection = readAtBase(file);
  if (!oldCollection || !oldCollection.updatedAt) continue;
  if (!isGreater(collection.version, oldCollection.version)) {
    errors.push(`${collection.id}: la version de collection doit être supérieure à ${oldCollection.version}`);
  }
  if (collection.updatedAt === oldCollection.updatedAt) {
    errors.push(`${collection.id}: updatedAt doit changer avec le manifeste`);
  }
}

if (errors.length) {
  console.error(`Validation des versions échouée (${errors.length}) :`);
  for (const error of errors) console.error(`- ${error}`);
  process.exit(1);
}

console.log(`Versions cohérentes avec ${baseRef}.`);
