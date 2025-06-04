# projetos.py

# Lista de projetos disponíveis com tags associadas
projetos_disponiveis = [
    {
        "title": "Week 2 – Login & Bakery Pages",
        "description": "A login form with styled HTML/CSS and a bakery landing page with Flexbox. Includes form structure, responsive layout, and semantic HTML.",
        "link": "https://fsherrmann.github.io/my-portfolio/projects/Senai/Week2/week2.html",
        "tags": ["HTML", "CSS", "Flexbox", "Forms"]
    },
    {
        "title": "Week 3 – Salary Calculation and Employee Information",
        "description": "A JavaScript program for calculating employee salaries, considering regular and overtime hours. Includes functions for salary calculation based on department and position (Admin and Management), and also features data validation.",
        "link": "https://fsherrmann.github.io/my-portfolio/projects/Senai/Week3/week3.html",
        "tags": ["JavaScript", "Logic", "Conditionals", "Functions"]
    },
    {
        "title": "Week 4 – JavaScript Loops, Conditionals, and User Interaction",
        "description": "A JavaScript program that counts prime, even, and odd numbers using loops, with basic arithmetic via arrow functions and interactive results shown through the DOM.",
        "link": "https://fsherrmann.github.io/my-portfolio/projects/Senai/Week4/week4.html",
        "tags": ["JavaScript", "Loops", "Conditionals", "Arrow Functions", "DOM Manipulation", "User Interaction"]
    },
    {
        "title": "Week 5 – Login Screen with Department Validation and Interactions",
        "description": "Login form with user code, department selection, and password. Validates credentials with JavaScript and shows dynamic content for Commercial, HR, and IT departments, including product display, salary table, and binary conversion.",
        "link": "https://fsherrmann.github.io/my-portfolio/projects/Senai/Week5/week5.html",
        "tags": ["HTML", "CSS", "JavaScript", "Form Validation", "DOM Manipulation", "Event Handling"]
    },
    {
        "title": "Week 6 – Hangman Game with Login and LocalStorage",
        "description": "A Hangman game with a login screen that saves the player's nickname in localStorage. Includes word selection, letter guessing with validation, display of correct and wrong letters, win message with player's nickname, and game restart.",
        "link": "https://fsherrmann.github.io/my-portfolio/projects/Senai/week6/week6.html",
        "tags": ["HTML", "CSS", "JavaScript", "Game Development", "LocalStorage", "Event Handling"]
    },
    {
        "title": "Week 8 – Digital Menu with React & TypeScript",
        "description": "A digital menu for a restaurant built with React and TypeScript using componentization. Includes a responsive navigation menu, presentation banner, Gnocchi and Pasta cards with integrated sauces (using CSS Grid), Drinks categories (using Flexbox), and a Footer with social icons.",
        "link": "https://fsherrmann.github.io/my-portfolio/projects/Senai/Week8/mamamia-menu",
        "tags": ["React", "TypeScript", "Componentization", "CSS Grid", "Flexbox"]
    }
]

# Conjunto para armazenar títulos de projetos removidos manualmente (se necessário no futuro)
projetos_excluidos = set()

# Função para filtrar os projetos com base nos conhecimentos selecionados
def filtrar_projetos(conhecimentos_selecionados):
    filtrados = []
    for projeto in projetos_disponiveis:
        if projeto['title'] in projetos_excluidos:
            continue
        tags_em_comum = [tag for tag in projeto['tags'] if tag in conhecimentos_selecionados]
        if tags_em_comum:
            filtrados.append((projeto, tags_em_comum))
    return filtrados
