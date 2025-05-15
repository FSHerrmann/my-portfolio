document.addEventListener("DOMContentLoaded", () => {
  fetch("../template.html") // ajuste o caminho se necessário
    .then(response => response.text())
    .then(html => {
      const parser = new DOMParser();
      const doc = parser.parseFromString(html, "text/html");

      // Carrega o footer
      const footer = doc.querySelector("footer");
      if (footer) {
        const footerContainer = document.getElementById("footer");
        if (footerContainer) {
          footerContainer.innerHTML = footer.outerHTML;
        }
      }
    });
});
