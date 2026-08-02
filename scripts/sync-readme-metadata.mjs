#!/usr/bin/env node

import { readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import process from "node:process";

const root = process.cwd();
const catalogue = JSON.parse(
  await readFile(path.join(root, "catalog/marketplace.json"), "utf8")
);
const readmePath = path.join(root, "README.md");
const original = await readFile(readmePath, "utf8");
const months = [
  "janvier",
  "février",
  "mars",
  "avril",
  "mai",
  "juin",
  "juillet",
  "août",
  "septembre",
  "octobre",
  "novembre",
  "décembre"
];

function formatDate(value) {
  const match = /^(\d{4})-(\d{2})-(\d{2})$/.exec(value);
  if (!match) throw new Error(`Date invalide dans le catalogue : ${value}`);
  const [, year, month, day] = match;
  return `${Number(day)} ${months[Number(month) - 1]} ${year}`;
}

let updated = original;
for (const skill of catalogue.skills) {
  const heading = `### \`${skill.id}\``;
  const start = updated.indexOf(heading);
  if (start < 0) throw new Error(`Section README introuvable : ${skill.id}`);
  const nextSkill = updated.indexOf("\n### `", start + heading.length);
  const nextSection = updated.indexOf("\n## ", start + heading.length);
  const candidates = [nextSkill, nextSection].filter((index) => index >= 0);
  const end = candidates.length ? Math.min(...candidates) : updated.length;
  const section = updated.slice(start, end);
  const badgeLine = section.match(/^.*assets\/badges\/agent-skills\.svg.*$/m)?.[0];
  if (!badgeLine) throw new Error(`Badge Agent Skills introuvable : ${skill.id}`);

  const metadata = `<sub>Version ${skill.version} · Mise à jour le ${formatDate(skill.updatedAt)}</sub>`;
  const withoutMetadata = section.replace(/\n<sub>Version [^\n]+<\/sub>\n*/, "\n");
  const replacement = withoutMetadata.replace(badgeLine, `${badgeLine}\n\n${metadata}`);
  updated = `${updated.slice(0, start)}${replacement}${updated.slice(end)}`;
}

if (process.argv.includes("--check")) {
  if (updated !== original) {
    console.error("README.md n’est pas synchronisé avec les versions du catalogue.");
    process.exit(1);
  }
  console.log("Les métadonnées du README sont synchronisées avec le catalogue.");
} else {
  await writeFile(readmePath, updated);
  console.log(`Métadonnées synchronisées pour ${catalogue.skills.length} skills.`);
}
