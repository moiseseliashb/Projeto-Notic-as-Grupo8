/* Vem ouvi - logica de UI (sem backend) */

const STORAGE_KEY = "vem-ouvi-favorites";

function loadFavorites() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return [];
    const parsed = JSON.parse(raw);
    return Array.isArray(parsed) ? parsed : [];
  } catch {
    return [];
  }
}

function saveFavorites(items) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(items));
}

function updateFavoritesCount() {
  const el = document.getElementById("favorites-count");
  if (!el) return;
  const count = loadFavorites().length;
  el.textContent = String(count);
}

function escapeHtml(str) {
  return String(str)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function renderFavorites(container) {
  const items = loadFavorites();
  container.innerHTML = "";

  if (items.length === 0) {
    container.innerHTML = `
      <div class="card">
        <h3>Sem favoritos ainda</h3>
        <p>Quando voce salvar uma noticia, ela vai aparecer aqui.</p>
      </div>
    `;
    return;
  }

  for (const item of items) {
    const title = escapeHtml(item.title || "");
    const summary = escapeHtml(item.summary || "");
    const url = escapeHtml(item.url || "");

    const card = document.createElement("article");
    card.className = "card";
    card.innerHTML = `
      <h3>${title || "Noticia"}</h3>
      <p>${summary || ""}</p>
      <div class="meta">
        ${url ? `<span class="chip">Link salvo</span>` : ""}
      </div>
      <div class="card-actions">
        <a class="btn btn-secondary" href="${url || "#"}" ${url ? "" : "aria-disabled=\"true\""}>Abrir</a>
        <button class="btn btn-danger" type="button" data-remove="${escapeHtml(
          item.id
        )}">Remover</button>
      </div>
    `;
    container.appendChild(card);
  }
}

function addFavoriteFromButton(btn) {
  const title = btn.getAttribute("data-title") || "";
  const summary = btn.getAttribute("data-summary") || "";
  const url = btn.getAttribute("data-url") || "";

  // id simples para o front-end (para remover).
  const id = `${Date.now()}_${Math.random().toString(16).slice(2)}`;

  const items = loadFavorites();
  items.unshift({ id, title, summary, url });
  saveFavorites(items);
  updateFavoritesCount();
}

document.addEventListener("DOMContentLoaded", () => {
  updateFavoritesCount();

  const favoritesContainer = document.getElementById("favorites-list");
  if (favoritesContainer) {
    renderFavorites(favoritesContainer);
  }

  const menuToggle = document.getElementById("menu-toggle");
  const navMenu = document.getElementById("nav-menu");
  if (menuToggle && navMenu) {
    menuToggle.addEventListener("click", () => navMenu.classList.toggle("open"));
    // Fecha ao clicar em link
    navMenu.querySelectorAll("a").forEach((a) =>
      a.addEventListener("click", () => navMenu.classList.remove("open"))
    );
  }
});

document.addEventListener("click", (e) => {
  const saveBtn = e.target.closest(".save-fav");
  if (saveBtn) {
    addFavoriteFromButton(saveBtn);
    return;
  }

  const removeBtn = e.target.closest("[data-remove]");
  if (removeBtn) {
    const id = removeBtn.getAttribute("data-remove");
    const items = loadFavorites().filter((it) => String(it.id) !== String(id));
    saveFavorites(items);
    updateFavoritesCount();
    const favoritesContainer = document.getElementById("favorites-list");
    if (favoritesContainer) renderFavorites(favoritesContainer);
  }
});

