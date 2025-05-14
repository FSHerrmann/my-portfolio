// Waits until the HTML content is fully loaded before executing the script
document.addEventListener('DOMContentLoaded', loadProjects);

// Loads all the project cards dynamically into the page
function loadProjects() {
  const projects = [
    {
      title: "Week 2 – Login & Bakery Pages",
      description: "A login form with styled HTML/CSS and a bakery landing page with Flexbox. Includes form structure, responsive layout, and semantic HTML.",
      link: "https://fsherrmann.github.io/my-portfolio/projects/Senai/Week%202/week2.html", // Link to the hosted project
      tags: ["HTML", "CSS", "Flexbox", "Forms"]

    },
    {
      title: "Week 3 – Salary Calculation and Employee Information",
      description: "A JavaScript program for calculating employee salaries, considering regular and overtime hours. Includes functions for salary calculation based on department and position (Admin and Management), and also features data validation.",
      link: "https://fsherrmann.github.io/my-portfolio/projects/Senai/Week%203/week3.html",
      tags: ["JavaScript", "Logic", "Conditionals", "Functions"]

    },
    {
      title: "Week 4 – JavaScript Loops, Conditionals, and User Interaction",
      description: "A JavaScript program that counts prime, even, and odd numbers using loops, with basic arithmetic via arrow functions and interactive results shown through the DOM.",
      link: "https://fsherrmann.github.io/my-portfolio/projects/Senai/Week%204/week4.html",
    },
  ];

  // Gets the container element where all project cards will be inserted
  const container = document.getElementById('project-container');

  // Iterates over each project object and creates a visual card for it
  projects.forEach(project => {
    const projectCard = createProjectCard(project);
    container.appendChild(projectCard); // Adds the card to the page
  });
}

// Creates an individual project card element based on a project's data
function createProjectCard(project) {
  // Creates a clickable link that wraps around the entire card
  const link = document.createElement('a');
  link.href = project.link;
  // link.target = "_blank"; // Opens the link in a new tab #OFF
  link.style.textDecoration = 'none'; // Removes default underline from links
  link.style.color = 'inherit'; // Ensures link text color matches card styling
  link.classList.add('card-link'); // Optional class for styling the link wrapper

  // Creates the card element
  const card = document.createElement('div');
  card.classList.add('project-card');

  // Creates and fills in the project title
  const title = document.createElement('h2');
  title.classList.add('project-title');
  title.textContent = project.title;

  // Creates and fills in the project description
  const description = document.createElement('p');
  description.classList.add('project-description');
  description.textContent = project.description;

  // Appends the title and description to the card
  card.appendChild(title);
  card.appendChild(description);

  // Puts the entire card inside the clickable link
  link.appendChild(card);

  return link; // Returns the completed card element
}
