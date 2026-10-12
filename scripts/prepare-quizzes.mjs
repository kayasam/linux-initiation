import fs from "node:fs"
import path from "node:path"
import vm from "node:vm"
import { fileURLToPath } from "node:url"

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..")
const source =
  process.argv[2] || "C:/Users/kayaw/Nextcloud/Obsidian/CoffreSam/Formations/linux-initiation"
const clean = (s) =>
  s
    .replace(/<[^>]*>/g, "")
    .replaceAll("&gt;", ">")
    .replaceAll("&lt;", "<")
    .replaceAll("&amp;", "&")
    .replaceAll("&quot;", '"')
    .replaceAll("&#39;", "'")
const chapters = JSON.parse(fs.readFileSync(path.join(root, "chapters.json"), "utf8"))
const banks = {}
for (const chapter of chapters) {
  const html = fs.readFileSync(path.join(source, "cours", chapter.slug + ".html"), "utf8")
  let questions
  const array = html.match(/const (?:quizData|questions) = (\[[\s\S]*?\n\]);/)
  if (array) {
    const items = vm.runInNewContext(array[1], Object.create(null), { timeout: 1000 })
    questions = items.map((q) => ({
      theme: chapter.title,
      question: clean(q.q),
      choices: q.opts.map(clean),
      answer: q.correct,
      explanation: clean(q.feedback || q.fb),
    }))
  } else {
    const answers = vm.runInNewContext("(" + html.match(/const answers = (\{.*?\});/)[1] + ")")
    const feedbacks = vm.runInNewContext(
      "(" + html.match(/const feedbacks = (\{[\s\S]*?\n\});/)[1] + ")",
    )
    questions = [
      ...html.matchAll(
        /<div class="quiz-question" id="q(\d+)">([\s\S]*?)<div class="quiz-feedback"/g,
      ),
    ].map((m) => {
      const answer = answers[m[1]]
      const options = [...m[2].matchAll(/<button class="quiz-option"[^>]*>([\s\S]*?)<\/button>/g)]
      return {
        theme: chapter.title,
        question: clean(m[2].match(/<h4>(.*?)<\/h4>/)[1]).replace(/^Question \d+ — /, ""),
        choices: options.map((x) => clean(x[1]).replace(/^[a-d]\) /, "")),
        answer: "abcd".indexOf(answer),
        explanation: clean(feedbacks[m[1]][answer]),
      }
    })
  }
  // Avoid two equivalent correct choices in the original APT question.
  if (chapter.slug.startsWith("08-"))
    questions.find((q) => q.question.includes("curl et git")).choices[0] =
      "sudo apt update curl git"
  for (const q of questions) {
    if (
      q.choices.length !== 4 ||
      !Number.isInteger(q.answer) ||
      q.answer < 0 ||
      q.answer > 3 ||
      !q.explanation
    )
      throw Error("Question invalide : " + q.question)
  }
  const count = questions.length
  if (count < 5) throw Error("Quiz incomplet : " + chapter.slug)
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
    .replaceAll("01-introduction-itil", chapter.slug)
    .replaceAll("Découverte ITIL", "Linux — Initiation")
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
