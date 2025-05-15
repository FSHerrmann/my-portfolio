// loadFooter.js
document.addEventListener("DOMContentLoaded", () => {
  fetch("../template.html") // ajuste o caminho se necessário
    .then(response => response.text())
    .then(html => {
      const parser = new DOMParser();
      const doc = parser.parseFromString(html, "text/html");
      const footer = doc.querySelector("footer");
      if (footer) {
        document.getElementById("footer").innerHTML = footer.outerHTML;
      }
    });
});