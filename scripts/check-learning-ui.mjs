import assert from "node:assert/strict"
import fs from "node:fs"
import vm from "node:vm"

// Exercise the actual quiz engine, including its displayed answer positions.
class Element {
  constructor() {
    this.children = []
    this.dataset = {}
    this.style = {}
    this.events = {}
    this.textContent = ""
    this.classList = { add() {}, remove() {} }
  }
  set innerHTML(value) {
    this.children = [new Element(), new Element()]
  }
  get lastElementChild() {
    return this.children.at(-1)
  }
  get nextElementSibling() {
    return (this.sibling ??= new Element())
  }
  replaceChildren(...children) {
    this.children = children
  }
  appendChild(element) {
    this.children.push(element)
  }
  append(...elements) {
    this.children.push(...elements)
  }
  addEventListener(event, handler) {
    this.events[event] = handler
  }
  querySelectorAll() {
    return this.children
  }
  scrollIntoView() {}
  focus() {}
}
const context = { window: {} }
vm.runInNewContext(fs.readFileSync("content/assets/quiz/quiz-banks.js", "utf8"), context)
const banks = context.window.linuxQuizBanks
assert.equal(Object.keys(banks).length, 10)
let attempts = 0
for (const [id, bank] of Object.entries(banks)) {
  assert.equal(bank.questions.length, 20)
  assert.deepEqual(
    [0, 1, 2, 3].map((i) => bank.questions.filter((q) => q.answer === i).length),
    [5, 5, 5, 5],
  )
  const elements = {}
  const get = (id) => (elements[id] ??= new Element())
  const root = new Element()
  root.dataset.quiz = id
  const document = {
    getElementById: get,
    createElement: () => new Element(),
    querySelector: (s) => (s === "[data-quiz]" ? root : get(s)),
  }
  const storage = new Map()
  vm.runInNewContext(fs.readFileSync("site-content/assets/quiz/quiz-engine.js", "utf8"), {
    window: { linuxQuizBanks: banks },
    document,
    localStorage: {
      getItem: (key) => storage.get(key),
      setItem: (key, value) => storage.set(key, value),
    },
  })
  const orders = new Set(),
    layouts = new Set()
  for (let attempt = 0; attempt < 100; attempt++) {
    const positions = [0, 0, 0, 0],
      questions = [],
      choices = []
    let expected = 0
    for (let index = 0; index < 20; index++) {
      const title = get("question-title").textContent
      questions.push(title)
      const question = bank.questions.find((q) => q.question === title)
      assert.ok(question)
      const answers = get("answers").children
      const position = answers.findIndex((b) => Number(b.dataset.index) === question.answer)
      positions[position]++
      choices.push(position)
      const correct = attempt % 3 === 0 || (attempt % 3 === 2 && index % 2 === 0)
      if (correct) expected++
      const button = answers.find((b) => (Number(b.dataset.index) === question.answer) === correct)
      button.events.click()
      button.events.click() // A second activation must not add another point.
      assert.equal(get("next-question").disabled, false)
      assert.ok(get("feedback").children[2].textContent)
      get("next-question").events.click()
    }
    assert.deepEqual(positions, [5, 5, 5, 5])
    assert.equal(new Set(questions).size, 20)
    assert.equal(get("result-score").textContent, expected + "/20")
    orders.add(questions.join("|"))
    layouts.add(choices.join(""))
    get("restart-quiz").events.click()
    assert.equal(get("current-question").textContent, "Question 1 sur 20")
    attempts++
  }
  assert.ok(orders.size > 90, "Question order is not sufficiently shuffled")
  assert.ok(layouts.size > 90, "Answer slots are not sufficiently shuffled")
}

// WCAG contrast calculation for the theme's text and controls on actual palette surfaces.
const css = fs.readFileSync("site-content/assets/themes/theme.css", "utf8")
const rgb = (hex) => hex.match(/[a-f0-9]{2}/gi).map((v) => parseInt(v, 16) / 255)
const luminance = (values) =>
  values
    .map((v) => (v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4))
    .reduce((sum, v, i) => sum + v * [0.2126, 0.7152, 0.0722][i], 0)
const contrast = (a, b) => {
  const l1 = luminance(a),
    l2 = luminance(b)
  return (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05)
}
let comparisons = 0
for (const mode of ["light", "dark"]) {
  const block = css.match(new RegExp('html\\[data-theme="' + mode + '"\\] \\{([\\s\\S]*?)\\}'))[1]
  const colors = Object.fromEntries(
    [...block.matchAll(/--([\w-]+):\s*(#[a-f0-9]{6})/gi)].map((m) => [m[1], rgb(m[2])]),
  )
  for (const foreground of [
    "text",
    "text-dim",
    "accent",
    "accent2",
    "success",
    "danger",
    "warn",
    "syntax-command",
    "syntax-flag",
    "syntax-arg",
    "syntax-path",
  ]) {
    for (const background of ["bg", "surface", "surface2", "code-bg"]) {
      const ratio = contrast(colors[foreground], colors[background])
      assert.ok(ratio >= 4.5, `${mode}: ${foreground}/${background} = ${ratio.toFixed(2)}`)
      comparisons++
    }
  }
  assert.ok(contrast(colors["on-accent"], colors.accent) >= 4.5)
  for (const status of ["correct", "wrong"]) {
    const background = colors[status].map((v, i) => v * 0.12 + colors.panel[i] * 0.88)
    assert.ok(contrast(colors.text, background) >= 4.5)
  }
}
console.log(
  `Validated: 200 questions, ${attempts} attempts with 5/5/5/5, randomized order, scoring and restart; ${comparisons} text contrast pairs >= 4.5:1.`,
)

// Test the theme switch itself: saved preference, system default, iframe sync and blocked storage.
for (const systemDark of [false, true]) {
  for (const saved of [null, "light", "dark", "blocked"]) {
    const html = { dataset: {}, setAttribute() {} }
    const body = {
      prepend(element) {
        this.toolbar = element
      },
    }
    const listeners = {},
      sent = []
    const media = {
      matches: systemDark,
      addEventListener(type, handler) {
        listeners["media:" + type] = handler
      },
    }
    const quiz = new Element()
    html.dataset.chapter = "01-comprendre-linux"
    let preference = saved
    const document = {
      documentElement: html,
      body,
      readyState: "complete",
      getElementById: (id) => (id === "tab-quiz" ? quiz : null),
      querySelectorAll: (selector) =>
        selector === ".theme-switch"
          ? body.toolbar?.children || []
          : quiz.children.filter((e) => e.className === "course-quiz-frame"),
      createElement: (tag) => {
        const element = new Element()
        element.setAttribute = () => {}
        if (tag === "iframe") element.contentWindow = { postMessage: (data) => sent.push(data) }
        return element
      },
    }
    const parent = {}
    const window = {
      parent,
      location: { protocol: "https:", origin: "https://example.test" },
      matchMedia: () => media,
      addEventListener: (name, handler) => (listeners[name] = handler),
    }
    vm.runInNewContext(fs.readFileSync("site-content/assets/themes/theme.js", "utf8"), {
      window,
      document,
      localStorage: {
        getItem() {
          if (saved === "blocked") throw Error("Unavailable")
          return saved
        },
        setItem(key, value) {
          if (saved === "blocked") throw Error("Unavailable")
          assert.equal(key, "theme")
          preference = value
        },
      },
    })
    const initial = ["light", "dark"].includes(saved) ? saved : systemDark ? "dark" : "light"
    assert.equal(html.dataset.theme, initial)
    assert.equal(quiz.children.length, 2)
    assert.equal(quiz.children[1].src, "quiz/01-comprendre-linux.html")
    const button = body.toolbar.children[0]
    button.events.click()
    const next = initial === "dark" ? "light" : "dark"
    assert.equal(html.dataset.theme, next)
    assert.ok(button.textContent.includes(next === "dark" ? "clair" : "sombre"))
    if (saved !== "blocked") assert.equal(preference, next)
    assert.equal(sent.at(-1).theme, next)
    listeners.storage({ key: "theme", newValue: initial })
    assert.equal(html.dataset.theme, initial)
    listeners.message({
      source: parent,
      origin: "https://evil.test",
      data: { type: "linux-theme", theme: next },
    })
    assert.equal(html.dataset.theme, initial)
    listeners.message({
      source: parent,
      origin: window.location.origin,
      data: { type: "linux-theme", theme: next },
    })
    assert.equal(html.dataset.theme, next)
  }
}
console.log(
  "Theme switch verified: light/dark, saved preference, system default, blocked storage and embedded quiz synchronization.",
)
