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
      const resources = registry[key]
      const children = folder.nextElementSibling?.querySelector<HTMLUListElement>(":scope > ul")
      if (!resources || !children || children.querySelector(":scope > .explorer-chapter-resources")) return
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
        anchor.setAttribute("aria-label", resource.label + " — " + resource.detail)
        if (resource.kind === "markdown") anchor.setAttribute("download", "")
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
        if (resource.kind === "tp") {
          children.querySelectorAll<HTMLAnchorElement>(":scope > li > a[href]").forEach((existing) => {
            const path = new URL(existing.href, location.href).pathname.replace(/\/$/, "")
            const target = new URL(resource.href, location.href).pathname.replace(/\/$/, "")
            if (path === target || path.endsWith("/" + key + "/tp")) existing.parentElement!.hidden = true
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
