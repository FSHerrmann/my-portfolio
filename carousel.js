// carousel.js
document.addEventListener('DOMContentLoaded', function() {
  const cards = document.querySelectorAll('.carousel-track .flip-card');
  const prevBtn = document.querySelector('.carousel-arrow-left');
  const nextBtn = document.querySelector('.carousel-arrow-right');
  let current = 0;

  function showCard(index) {
    cards.forEach((card, i) => {
      card.classList.toggle('active', i === index);
    });
    prevBtn.disabled = index === 0;
    nextBtn.disabled = index === cards.length - 1;
  }

  prevBtn.addEventListener('click', () => {
    if (current > 0) {
      current--;
      showCard(current);
    }
  });

  nextBtn.addEventListener('click', () => {
    if (current < cards.length - 1) {
      current++;
      showCard(current);
    }
  });

  // Initialize
  showCard(current);
});
