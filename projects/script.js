// Espera o carregamento completo da página para executar tudo
document.addEventListener('DOMContentLoaded', () => {
  if (document.getElementById('project-container')) {
    loadProjects();
  }
  if (document.getElementById('footer')) {
    loadFooter();
  }
});

// Carrega os cards dos projetos dinamicamente (só para index.html)
function loadProjects() {
  const projects = [
    {
      title: "Week 2 – Login & Bakery Pages",
      description: "A login form with styled HTML/CSS and a bakery landing page with Flexbox. Includes form structure, responsive layout, and semantic HTML.",
      link: "https://fsherrmann.github.io/my-portfolio/projects/Senai/Week2/week2.html",
      tags: ["HTML", "CSS", "Flexbox", "Forms"]
    },
    {
      title: "Week 3 – Salary Calculation and Employee Information",
      description: "A JavaScript program for calculating employee salaries, considering regular and overtime hours. Includes functions for salary calculation based on department and position (Admin and Management), and also features data validation.",
      link: "https://fsherrmann.github.io/my-portfolio/projects/Senai/Week3/week3.html",
      tags: ["JavaScript", "Logic", "Conditionals", "Functions"]
    },
    {
      title: "Week 4 – JavaScript Loops, Conditionals, and User Interaction",
      description: "A JavaScript program that counts prime, even, and odd numbers using loops, with basic arithmetic via arrow functions and interactive results shown through the DOM.",
      link: "https://fsherrmann.github.io/my-portfolio/projects/Senai/Week4/week4.html",
      tags: ["JavaScript", "Loops", "Conditionals", "Arrow Functions", "DOM Manipulation", "User Interaction"]
    },
    {
    title: "Week 5 – Login Screen with Department Validation and Interactions",
    description: "Login form with user code, department selection, and password. Validates credentials with JavaScript and shows dynamic content for Commercial, HR, and IT departments, including product display, salary table, and binary conversion.",
    link: "https://fsherrmann.github.io/my-portfolio/projects/Senai/Week5/week5.html",
    tags: ["HTML", "CSS", "JavaScript", "Form Validation", "DOM Manipulation", "Event Handling"]
    },
    {
  title: "Week 6 – Hangman Game with Login and LocalStorage",
  description: "A Hangman game with a login screen that saves the player's nickname in localStorage. Includes word selection, letter guessing with validation, display of correct and wrong letters, win message with player's nickname, and game restart.",
  link: "https://fsherrmann.github.io/my-portfolio/projects/Senai/Week6/game.html",
  tags: ["HTML", "CSS", "JavaScript", "Game Development", "LocalStorage", "Event Handling"]
  }, 
  {
  title: "Week 8 – Digital Menu with React & TypeScript",
  description: "A digital menu for a restaurant built with React and TypeScript using componentization. Includes a responsive menu, presentation screen, gnocchi and pasta cards with sauces, drinks categories, and a footer with social icons.",
  link: "Bombardillo Crocodillo",
  tags: ["React", "TypeScript", "Componentization", "CSS"]
  }
  ];

  const container = document.getElementById('project-container');
  if (!container) return;

  projects.forEach(project => {
    const projectCard = createProjectCard(project);
    container.appendChild(projectCard);
  });
}

function createProjectCard(project) {
  const link = document.createElement('a');
  link.href = project.link;
  link.style.textDecoration = 'none';
  link.style.color = 'inherit';
  link.classList.add('card-link');

  const card = document.createElement('div');
  card.classList.add('project-card');

  const title = document.createElement('h2');
  title.classList.add('project-title');
  title.textContent = project.title;

  const description = document.createElement('p');
  description.classList.add('project-description');
  description.textContent = project.description;

  card.appendChild(title);
  card.appendChild(description);
  link.appendChild(card);

  return link;
}

// Função dinâmica para determinar o caminho correto do template
function getFooterPath() {
  // Se está no index.html na raiz de projects/
  if (
    location.pathname.endsWith('/projects/index.html') ||
    location.pathname.endsWith('/projects/') ||
    location.pathname.match(/\/projects\/(index\.html)?$/)
  ) {
    return './Senai/template.html';
  }
  // Senão, está em alguma subpasta (Week 2, Week 3, etc)
  return '../template.html';
}

function loadFooter() {
  fetch(getFooterPath())
    .then(response => response.text())
    .then(html => {
      const tempDiv = document.createElement('div');
      tempDiv.innerHTML = html;
      const footer = tempDiv.querySelector('footer');
      if (footer) {
        document.getElementById('footer').innerHTML = footer.outerHTML;
      }
    })
    .catch(err => {
      document.getElementById('footer').innerHTML = '<footer>Footer not found.</footer>';
      console.error('Footer load error:', err);
    });
}
