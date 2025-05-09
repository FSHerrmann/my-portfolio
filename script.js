document.addEventListener('DOMContentLoaded', loadProjects);

// This function loads all the project cards dynamically
function loadProjects() {
  const projects = [
    {
      title: "Week 2 – Login & Bakery Pages",
      description: "A login form with styled HTML/CSS and a bakery landing page with Flexbox. Includes form structure, responsive layout, and semantic HTML.",
      image: "images/week2-thumbnail.jpg",
    },
    {
      title: "Project Two",
      description: "A brief description of the project goes here.",
      image: "project2.jpg",
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

// This function creates the HTML structure for a single project card
function createProjectCard(project) {
  const card = document.createElement('div'); // Create a div element for the project card
  card.classList.add('project-card'); // Add a class to the card for styling

  const image = document.createElement('img'); // Create the image element for the project
  image.src = project.image; // Set the source of the image
  image.alt = `${project.title} Preview`; // Set the alt text for the image

  const projectInfo = document.createElement('div'); // Create a div for project info (title and description)
  projectInfo.classList.add('project-info'); // Add a class to the info div

  const title = document.createElement('h2'); // Create an h2 element for the project title
  title.classList.add('project-title'); // Add a class for styling
  title.textContent = project.title; // Set the title text

  const description = document.createElement('p'); // Create a paragraph element for the project description
  description.classList.add('project-description'); // Add a class for styling
  description.textContent = project.description; // Set the description text

  projectInfo.appendChild(title); // Add the title to the project info div
  projectInfo.appendChild(description); // Add the description to the project info div

  card.appendChild(image); // Append the image to the card
  card.appendChild(projectInfo); // Append the project info div to the card

  return card; // Return the fully created project card
}