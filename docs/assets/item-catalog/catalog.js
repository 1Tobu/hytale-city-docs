(() => {
  const catalog = document.querySelector("#item-catalog");
  if (!catalog) return;

  const filter = document.querySelector("#item-filter");
  const results = document.querySelector("#item-results");
  const grid = document.querySelector("#item-grid");
  const previous = document.querySelector("#item-previous");
  const next = document.querySelector("#item-next");
  const pageLabel = document.querySelector("#item-page");
  const source = new URL("items.json", document.currentScript.src);
  const english = document.documentElement.lang === "en";
  const message = english ? {
    unavailable: "Image unavailable",
    noIcon: "No icon",
    count: (count, total) => `${count} of ${total} items`,
    page: (current, total) => `Page ${current} of ${total}`,
    error: "The item catalog could not be loaded.",
  } : {
    unavailable: "Bild nicht verfügbar",
    noIcon: "Kein Icon vorhanden",
    count: (count, total) => `${count} von ${total} Items`,
    page: (current, total) => `Seite ${current} von ${total}`,
    error: "Der Itemkatalog konnte nicht geladen werden.",
  };
  const pageSize = 60;
  const number = new Intl.NumberFormat(document.documentElement.lang);
  const normalize = (value) => value.toLowerCase().replace(/_/g, " ");
  let items = [];
  let matches = [];
  let page = 0;

  function render() {
    grid.replaceChildren();

    for (const item of matches.slice(page * pageSize, (page + 1) * pageSize)) {
      const card = document.createElement("li");
      const preview = document.createElement("div");
      preview.className = "item-preview";
      const fallback = document.createElement("span");
      fallback.textContent = item.icon ? message.unavailable : message.noIcon;
      preview.append(fallback);

      if (item.icon) {
        const icon = document.createElement("img");
        icon.alt = "";
        icon.loading = "lazy";
        icon.addEventListener("error", () => {
          icon.remove();
          fallback.hidden = false;
        });
        icon.src = new URL(item.icon, source);
        fallback.hidden = true;
        preview.append(icon);
      }

      const name = document.createElement("strong");
      name.textContent = item.name;
      const id = document.createElement("code");
      id.textContent = item.id;
      card.append(preview, name, id);
      grid.append(card);
    }

    const pages = Math.ceil(matches.length / pageSize);
    results.textContent = message.count(number.format(matches.length), number.format(items.length));
    pageLabel.textContent = pages ? message.page(page + 1, pages) : "";
    previous.disabled = page === 0;
    next.disabled = page + 1 >= pages;
  }

  filter.addEventListener("input", () => {
    const terms = normalize(filter.value).trim().split(/\s+/).filter(Boolean);
    matches = items.filter((item) => terms.every((term) => item.search.includes(term)));
    page = 0;
    render();
  });

  function changePage(offset) {
    page += offset;
    render();
    results.scrollIntoView({ block: "start" });
  }

  previous.addEventListener("click", () => changePage(-1));
  next.addEventListener("click", () => changePage(1));
  filter.disabled = true;
  fetch(source).then((response) => {
    if (!response.ok) throw new Error("Item catalog unavailable");
    return response.json();
  }).then((data) => {
    items = data.map((item) => ({ ...item, search: normalize(`${item.name} ${item.id}`) }));
    matches = items;
    filter.disabled = false;
    render();
  }).catch(() => {
    results.textContent = message.error;
  });
})();
