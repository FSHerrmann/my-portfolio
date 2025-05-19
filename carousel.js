document.addEventListener('DOMContentLoaded', function() {
  const cards = document.querySelectorAll('.carousel-track .flip-card');
  const prevBtn = document.querySelector('.carousel-arrow-left');
  const nextBtn = document.querySelector('.carousel-arrow-right');
  let current = 0;

  function updateClasses() {
    const len = cards.length;
    cards.forEach((card, i) => {
      card.classList.remove('prev', 'active', 'next');
      if (i === current) {
        card.classList.add('active');
      } else if (i === (current - 1 + len) % len) {
        card.classList.add('prev');
      } else if (i === (current + 1) % len) {
        card.classList.add('next');
      }
    });
  }

  function showCard(index) {
    current = (index + cards.length) % cards.length;
    updateClasses();
    // Não desabilita mais os botões (carrossel infinito)
    // prevBtn.disabled = index === 0;
    // nextBtn.disabled = index === cards.length - 1;
  }

  prevBtn.addEventListener('click', () => {
    showCard(current - 1);
  });

  nextBtn.addEventListener('click', () => {
    showCard(current + 1);
  });

  // Initialize
  showCard(current);
});
