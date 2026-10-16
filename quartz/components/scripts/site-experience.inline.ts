type CourseLink = { kind: string; href: string; chapterTitle?: string }
let releaseSiteExperience: (() => void) | undefined

function setupSiteExperience() {
  releaseSiteExperience?.()
  const article = document.querySelector<HTMLElement>(".center article")
  const left = document.querySelector<HTMLElement>(".sidebar.left")
  if (!article || !left) return
  const cleanups: (() => void)[] = []
  const on = (target: EventTarget, name: string, callback: EventListener) => {
    target.addEventListener(name, callback)
    cleanups.push(() => target.removeEventListener(name, callback))
  }
  const bar = article.querySelector<HTMLElement>(".chapter-resources")
  const kind = article.querySelector<HTMLElement>(".support-viewer")?.dataset.supportKind ?? (/\/tp(?:\/|$)/.test(location.pathname) ? "tp" : "markdown")
  const key = bar?.dataset.courseKey
  let registry: Record<string, CourseLink[]> = {}
  try { registry = JSON.parse(document.getElementById("course-resource-data")?.textContent ?? "{}") } catch {}
  const siteRoot = Object.values(registry)[0]?.[0]?.href.replace(/(?:bash\/)?\d\d-[^/]+\/$/, "") ?? "/"
  const isHome = Boolean(article.querySelector(".home-header"))
  document.body.classList.toggle("site-home", isHome)
  document.body.classList.toggle("site-course", Boolean(bar))
  article.id = "course-content"
  article.tabIndex = -1
  document.querySelectorAll<HTMLAnchorElement>(".breadcrumb-element a").forEach((link) => {
    if (link.textContent?.trim() === "Home") link.textContent = "Accueil"
  })
  const explorerTitle = left.querySelector<HTMLElement>(".desktop-explorer h2")
  if (explorerTitle) explorerTitle.textContent = "Chapitres"
  const skip = document.createElement("a")
  skip.className = "site-skip-link"
  skip.href = "#course-content"
  skip.textContent = "Aller au contenu"
  on(skip, "click", () => article.focus({ preventScroll: true }))
  document.body.prepend(skip)

  const header = document.createElement("header")
  header.className = "site-mobile-header"
  const brand = document.createElement("a")
  brand.href = siteRoot
  brand.textContent = "Linux & Bash"
  const trigger = document.createElement("button")
  trigger.type = "button"
  trigger.textContent = "☰ Chapitres"
  trigger.setAttribute("aria-controls", "chapter-drawer")
  trigger.setAttribute("aria-expanded", "false")
  const theme = document.createElement("button")
  theme.type = "button"
  theme.textContent = "◐"
  const nativeTheme = document.querySelector<HTMLButtonElement>("button.darkmode")
  on(theme, "click", () => nativeTheme?.click())
  function updateTheme() {
    const label = document.documentElement.getAttribute("saved-theme") === "dark" ? "Activer le thème clair" : "Activer le thème sombre"
    theme.setAttribute("aria-label", label)
    nativeTheme?.setAttribute("aria-label", label)
  }
  updateTheme()
  const themeObserver = new MutationObserver(updateTheme)
  themeObserver.observe(document.documentElement, { attributes: true, attributeFilter: ["saved-theme"] })
  header.append(trigger, brand, theme)
  skip.after(header)
  const backdrop = document.createElement("div")
  backdrop.className = "site-drawer-backdrop"
  backdrop.setAttribute("aria-hidden", "true")
  header.after(backdrop)
  const drawerHeading = document.createElement("div")
  drawerHeading.className = "site-drawer-heading"
  const drawerTitle = document.createElement("strong")
  drawerTitle.textContent = "Les chapitres"
  const close = document.createElement("button")
  close.type = "button"
  close.textContent = "Fermer ×"
  close.setAttribute("aria-label", "Fermer le menu des chapitres")
  drawerHeading.append(drawerTitle, close)
  left.prepend(drawerHeading)
  left.id = "chapter-drawer"
  const mobile = matchMedia("(max-width: 800px)")
  let open = false
  const content = [...document.querySelectorAll<HTMLElement>("#quartz-body > .center, #quartz-body > .right, #quartz-body > footer")]
  function setOpen(value: boolean, restore = true) {
    open = value && mobile.matches
    document.body.classList.toggle("chapter-menu-open", open)
    trigger.setAttribute("aria-expanded", String(open))
    content.forEach((item) => item.inert = open)
    header.inert = open
    if (open) {
      left.setAttribute("role", "dialog")
      left.setAttribute("aria-modal", "true")
      left.setAttribute("aria-label", "Chapitres des formations")
      close.focus()
    } else {
      left.removeAttribute("role"); left.removeAttribute("aria-modal"); left.removeAttribute("aria-label")
      if (restore && mobile.matches) trigger.focus()
    }
  }
  on(trigger, "click", () => setOpen(!open))
  on(close, "click", () => setOpen(false))
  on(backdrop, "click", () => setOpen(false))
  on(left, "click", ((event: MouseEvent) => {
    if ((event.target as Element).closest("a[href]") && open) setOpen(false, false)
  }) as EventListener)
  on(document, "keydown", ((event: KeyboardEvent) => {
    if (!open) return
    if (event.key === "Escape") { event.preventDefault(); setOpen(false); return }
    if (event.key === "Tab") {
      const focusable = [...left!.querySelectorAll<HTMLElement>('button, a[href], [tabindex="0"]')].filter((node) => node.getClientRects().length > 0)
      const first = focusable[0], last = focusable.at(-1)
      if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last?.focus() }
      else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first?.focus() }
    }
  }) as EventListener)
  const resized = () => setOpen(false, false)
  mobile.addEventListener("change", resized)
  setOpen(false, false)

  let pager: HTMLElement | undefined
  if (key && registry[key]) {
    const keys = Object.keys(registry).filter((candidate) => candidate.startsWith("bash/") === key.startsWith("bash/")).sort()
    const position = keys.indexOf(key)
    pager = document.createElement("nav")
    pager.className = "site-chapter-pager"
    pager.setAttribute("aria-label", "Continuer la formation")
    for (const [offset, label] of [[-1, "← Chapitre précédent"], [1, "Chapitre suivant →"]] as const) {
      const target = keys[position + offset]
      if (!target) continue
      const link = document.createElement("a")
      link.href = registry[target].find((item) => item.kind === kind)?.href ?? registry[target][0].href
      const caption = document.createElement("span")
      caption.textContent = label
      const title = document.createElement("strong")
      title.textContent = registry[target][0].chapterTitle ?? target.split("/").pop()!
      link.append(caption, title)
      if (offset === 1) link.className = "site-chapter-next"
      pager.append(link)
    }
    article.append(pager)
    try { localStorage.setItem("course-last-visited", JSON.stringify({ key, kind })) } catch {}
  }
  let resume: HTMLElement | undefined
  if (isHome) {
    try {
      const last = JSON.parse(localStorage.getItem("course-last-visited") ?? "null")
      const course = registry[last?.key]
      if (course) {
        resume = document.createElement("a")
        resume.className = "site-resume"
        ;(resume as HTMLAnchorElement).href = course.find((item) => item.kind === last.kind)?.href ?? course[0].href
        const label = document.createElement("span")
        label.textContent = "Reprendre ma lecture →"
        const title = document.createElement("strong")
        title.textContent = course[0].chapterTitle ?? last.key
        resume.append(label, title)
        article.querySelector(".home-header")?.append(resume)
      }
    } catch {}
  }
  releaseSiteExperience = () => {
    setOpen(false, false)
    cleanups.forEach((cleanup) => cleanup())
    themeObserver.disconnect(); mobile.removeEventListener("change", resized)
    skip.remove(); header.remove(); backdrop.remove(); drawerHeading.remove(); pager?.remove(); resume?.remove()
    left.removeAttribute("id")
    document.body.classList.remove("site-home", "site-course", "chapter-menu-open")
  }
  window.addCleanup?.(releaseSiteExperience)
}
document.addEventListener("nav", setupSiteExperience)
document.addEventListener("render", setupSiteExperience)
