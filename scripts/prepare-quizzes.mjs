import fs from "node:fs"
import path from "node:path"
import { fileURLToPath } from "node:url"

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..")
const chapters = JSON.parse(fs.readFileSync(path.join(root, "chapters.json"), "utf8"))
const baseQuestions = JSON.parse(
  fs.readFileSync(path.join(root, "site-content/assets/quiz/quiz-questions.json"), "utf8"),
)
const supplements = {}
let section
for (const line of fs
  .readFileSync(path.join(root, "site-content/assets/quiz/questions-complementaires.txt"), "utf8")
  .split(/\r?\n/)) {
  if (!line.trim()) continue
  if (/^\[\d{2}\]$/.test(line)) {
    section = line.slice(1, -1)
    supplements[section] = []
    continue
  }
  const parts = line.split("§")
  if (!section || parts.length !== 6) throw Error("Question complémentaire invalide : " + line)
  supplements[section].push(parts)
}
const banks = {}
for (const chapter of chapters) {
  let questions = structuredClone(baseQuestions[chapter.slug])
  const extra = supplements[chapter.slug.slice(0, 2)] || []
  questions.push(
    ...extra.map(([question, ...parts]) => ({
      theme: chapter.title,
      question,
      choices: parts.slice(0, 4),
      answer: 0,
      explanation: parts[4],
    })),
  )
  // Balance the authored bank too. Runtime shuffles questions and answer slots independently.
  questions = questions.map((q, index) => {
    const answer = index % 4
    const correct = q.choices[q.answer]
    const choices = q.choices.filter((_, i) => i !== q.answer)
    choices.splice(answer, 0, correct)
    return { ...q, choices, answer }
  })
  for (const q of questions) {
    if (
      q.choices.length !== 4 ||
      new Set(q.choices).size !== 4 ||
      !Number.isInteger(q.answer) ||
      q.answer < 0 ||
      q.answer > 3 ||
      !q.explanation
    )
      throw Error("Question invalide : " + q.question)
  }
  const count = questions.length
  if (count !== 20) throw Error("Quiz incomplet : " + chapter.slug)
  if (new Set(questions.map((q) => q.question)).size !== 20)
    throw Error("Questions dupliquées : " + chapter.slug)
  if ([0, 1, 2, 3].some((i) => questions.filter((q) => q.answer === i).length !== 5))
    throw Error("Répartition invalide : " + chapter.slug)
  banks[chapter.slug] = {
    ...chapter,
    id: chapter.slug,
    chapter: "Chapitre " + chapter.slug.slice(0, 2),
    intro: "Vérifiez les notions du cours. Chaque réponse est expliquée.",
    chapterLink: "../../" + chapter.slug + "/",
    questions,
  }
  let page = fs.readFileSync(path.join(root, "site-content", "quiz-template.html"), "utf8")
  page = page
    .replaceAll("__CHAPTER__", chapter.slug)
    .replaceAll("20 questions", count + " questions")
    .replaceAll("sur 20", "sur " + count)
    .replaceAll("16/20", Math.ceil(count * 0.8) + "/" + count)
    .replaceAll("0/20", "0/" + count)
    .replaceAll("/20", "/" + count)
    .replaceAll("../" + chapter.slug, "../../" + chapter.slug + "/")
  const dest = path.join(root, "content/cours/quiz", chapter.slug + ".html")
  fs.mkdirSync(path.dirname(dest), { recursive: true })
  fs.writeFileSync(dest, page)
  console.log(chapter.slug + " : " + count + " questions")
}
fs.writeFileSync(
  path.join(root, "content/assets/quiz/quiz-banks.js"),
  "window.linuxQuizBanks = " + JSON.stringify(banks, null, 2) + "\n",
)
fs.rmSync(path.join(root, "content/quiz-template.html"), { force: true })
