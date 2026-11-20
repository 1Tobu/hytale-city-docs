(() => {
  const site = new URL("../", document.currentScript.src);
  const dialog = document.querySelector(".docs-access");
  if (!dialog) return;

  const storageKey = "hytalecity-docs-access:" + site.pathname;
  const passwordDigest = "1c121f05823ad624c2b637bf09b871dbd0a27854cb06d3b2ddd57f9d7da476f8";
  const navigation = performance.getEntriesByType("navigation")[0];
  const referrer = document.referrer ? new URL(document.referrer) : null;
  const internal = referrer?.origin === site.origin && referrer.pathname.startsWith(site.pathname);
  const continuing = navigation?.type !== "reload" && (internal || navigation?.type === "back_forward");

  function reveal() {
    document.documentElement.setAttribute("data-docs-unlocked", "");
    if (dialog.open) dialog.close();
  }

  try {
    if (continuing && sessionStorage.getItem(storageKey) === "unlocked") {
      reveal();
      return;
    }
    sessionStorage.removeItem(storageKey);
  } catch {
    // The form still works on this page when browser storage is unavailable.
  }

  const form = dialog.querySelector("form");
  const password = form.elements.password;
  const submit = form.querySelector("button");
  const error = form.querySelector("[role=alert]");
  dialog.addEventListener("cancel", (event) => event.preventDefault());
  password.addEventListener("input", () => {
    error.hidden = true;
    password.removeAttribute("aria-invalid");
  });
  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    submit.disabled = true;
    try {
      const bytes = new TextEncoder().encode(password.value);
      const result = await crypto.subtle.digest("SHA-256", bytes);
      const digest = Array.from(new Uint8Array(result), (byte) => byte.toString(16).padStart(2, "0")).join("");
      password.value = "";
      if (digest === passwordDigest) {
        try {
          sessionStorage.setItem(storageKey, "unlocked");
        } catch {
          // This unlock can only last for the current document without storage.
        }
        reveal();
      } else {
        error.textContent = error.dataset.invalid;
        error.hidden = false;
        password.setAttribute("aria-invalid", "true");
        password.focus();
      }
    } catch {
      error.textContent = error.dataset.unavailable;
      error.hidden = false;
    } finally {
      submit.disabled = false;
    }
  });

  dialog.showModal();
})();
