document.addEventListener('DOMContentLoaded', loadProjects);

// This function loads all the project cards dynamically
function loadProjects() {
  const projects = [
    {
      title: "Week 2 – Login & Bakery Pages",
      description: "A login form with styled HTML/CSS and a bakery landing page with Flexbox. Includes form structure, responsive layout, and semantic HTML.",
      image: "assets/week2-thumbnail.jpg",
      link: "https://fsherrmann.github.io/my-portfolio/projects/Senai/Week%202/week2.html", // ou link do GitHub Pages

    },
    {
      title: "Week 3 – Salary Calculation and Employee Information",
      description: "A JavaScript program for calculating employee salaries, considering regular and overtime hours. Includes functions for salary calculation based on department and position (Admin and Management), and also features data validation.",
      image: "project2.jpg",
      link: "https://fsherrmann.github.io/my-portfolio/projects/Senai/Week%203/week3.html",
    },
    {
      title: "Project Three",
      description: "A brief description of the project goes here.",
      image: "project3.jpg",
    },
  ];

  const container = document.getElementById('project-container'); // Get the container where cards will be appended

  // Loop through the projects array and create a project card for each project
  projects.forEach(project => {
    const projectCard = createProjectCard(project);
    container.appendChild(projectCard); // Append the created card to the container
  });
}

function createProjectCard(project) {
  // Cria o link que envolve o card inteiro
  const link = document.createElement('a');
  link.href = project.link;
  link.target = "_blank"; // Abre em nova aba (opcional)
  link.style.textDecoration = 'none';
  link.style.color = 'inherit';
  link.classList.add('card-link'); // Classe para ajustar o estilo do link

  // Cria o card
  const card = document.createElement('div');
  card.classList.add('project-card');

  const image = document.createElement('img');
  image.src = project.image;
  image.alt = `${project.title} Preview`;

  const title = document.createElement('h2');
  title.classList.add('project-title');
  title.textContent = project.title;

  const description = document.createElement('p');
  description.classList.add('project-description');
  description.textContent = project.description;

  card.appendChild(image);
  card.appendChild(title);
  card.appendChild(description);

  link.appendChild(card); // TODO o card fica dentro do link

  return link;
}