type ChapterResource = { kind: string; label: string; detail: string; href: string; icon: string }
let releaseChapterResources: (() => void) | undefined

function setupChapterResources() {
  releaseChapterResources?.()
  const payload = document.getElementById("course-resource-data")
  if (!payload) return
  let registry: Record<string, ChapterResource[]>
  try { registry = JSON.parse(payload.textContent ?? "{}") } catch { return }
  const explorer = document.querySelector(".explorer-content")
  if (!explorer) return

  function populate() {
    explorer!.querySelectorAll<HTMLElement>(".folder-container[data-folderpath]").forEach((folder) => {
      const key = (folder.dataset.folderpath ?? "").replace(/\/index$/, "")
      const currentViewer = document.querySelector<HTMLElement>(".support-viewer")
      folder.classList.toggle("support-current-chapter", currentViewer?.dataset.courseKey === key)
      const resources = registry[key]
      const children = folder.nextElementSibling?.querySelector<HTMLUListElement>(":scope > ul")
      if (!resources || !children) return
      children.querySelectorAll<HTMLElement>(":scope > li").forEach((child) => {
        const path = child.querySelector<HTMLElement>(":scope > .folder-container")?.dataset.folderpath?.replace(/\/index$/, "")
        if (path === key + "/html" || path === key + "/quiz") child.hidden = true
      })
      const existingGroup = children.querySelector(":scope > .explorer-chapter-resources")
      if (existingGroup) {
        existingGroup.querySelectorAll<HTMLAnchorElement>("a[data-resource-kind]").forEach((anchor) => {
          if (currentViewer?.dataset.courseKey === key && anchor.dataset.resourceKind === currentViewer.dataset.supportKind) anchor.setAttribute("aria-current", "page")
          else anchor.removeAttribute("aria-current")
        })
        return
      }
      const item = document.createElement("li")
      item.className = "explorer-chapter-resources"
      const nav = document.createElement("nav")
      nav.className = "resource-buttons resource-buttons--explorer"
      nav.setAttribute("aria-label", "Ressources de " + folder.textContent?.trim())
      resources.forEach((resource) => {
        const anchor = document.createElement("a")
        anchor.href = resource.href
        anchor.className = "resource-button resource-" + resource.kind
        anchor.dataset.resourceKind = resource.kind
        if (currentViewer?.dataset.courseKey === key && resource.kind === currentViewer.dataset.supportKind) anchor.setAttribute("aria-current", "page")
        anchor.setAttribute("aria-label", resource.label + " — " + resource.detail)
        const icon = document.createElement("span")
        icon.className = "resource-icon"
        icon.setAttribute("aria-hidden", "true")
        const image = document.createElement("img")
        image.src = resource.icon
        image.alt = ""
        icon.append(image)
        const label = document.createElement("span")
        label.className = "resource-label"
        label.textContent = resource.label
        anchor.append(icon, label)
        nav.append(anchor)
        if (["tp", "html", "quiz"].includes(resource.kind)) {
          children.querySelectorAll<HTMLAnchorElement>(":scope > li > a[href]").forEach((existing) => {
            const path = new URL(existing.href, location.href).pathname.replace(/\/$/, "")
            const target = new URL(resource.href, location.href).pathname.replace(/\/$/, "")
            if (path === target || path.endsWith("/" + key + "/" + resource.kind)) existing.parentElement!.hidden = true
          })
        }
      })
      item.append(nav)
      children.prepend(item)
    })
  }
  populate()
  const observer = new MutationObserver(populate)
  observer.observe(explorer, { childList: true, subtree: true })
  releaseChapterResources = () => observer.disconnect()
  window.addCleanup?.(releaseChapterResources)
}
document.addEventListener("nav", setupChapterResources)
document.addEventListener("render", setupChapterResources)
