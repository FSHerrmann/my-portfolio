# data.py

# Estrutura de dados final, com todas as seções e descrições atualizadas
curriculo_data = {
    'pt': {
        'dados_fixos': {
            "nome": "Felipe Schneider Herrmann",
            "email": "fsherrmann.dev@gmail.com",
            "telefone": "(48) 99109-9898",
            "formacao_web": "Desenvolvedor Web",
            "formacao_dados": "Analista de Dados",
            "formacao_java_web": "Desenvolvedor Full-Stack Java",
            "formacao_detalhada": """
                <li>
                    <strong>Formação Desenvolvimento Web (600h)</strong> - SENAI / Joinville Mais Tec (Cursando)
                    <br><em>Formação Full-Stack completa com foco em Java/Spring para o back-end e React para o front-end, incluindo metodologias ágeis e cultura DevOps.</em>
                </li>
                <li>
                    <strong>Engenharia de Computação</strong> - Universidade Federal de Santa Catarina (UFSC)
                    <br><em>Cursado entre 2013 e 2017, com base sólida em Lógica de Programação, Algoritmos, Estrutura de Dados e Arquitetura de Computadores.</em>
                </li>
            """,
            "resumo_web": "Desenvolvedor com foco na criação de interfaces modernas, responsivas e performáticas, utilizando as melhores práticas de mercado em HTML, CSS, JavaScript e React.",
            "resumo_dados": "Analista de dados com experiência no tratamento e adequação de dados para projetos internacionais. Hábil em extrair, traduzir e visualizar informações para gerar insights de negócio, com forte proficiência em Python (Pandas), SQL e ferramentas de BI.",
            "resumo_java_web": "Desenvolvedor Full-Stack com sólida formação em Java, Spring Boot para o back-end e React para o front-end. Experiência em criar APIs RESTful, gerenciar bancos de dados e aplicar metodologias ágeis.",
            "experiencias": [
                {
                    "cargo": "Analista de Projetos (PJ)",
                    "empresa": "4C Innovation",
                    "periodo": "Abril 2025 - Presente",
                    "pontos": [
                        "[Descreva sua principal responsabilidade na nova função, ex: Gerenciamento do ciclo de vida de projetos...]",
                        "[Adicione outra tarefa ou resultado importante, ex: Comunicação com stakeholders para alinhamento de escopo...]"
                    ]
                },
                {
                    "cargo": "Estagiário de Engenharia e Projetos",
                    "empresa": "4C Innovation",
                    "periodo": "Abril 2023 - Abril 2025",
                    "pontos": [
                        "Responsável pelo levantamento, tratamento e adequação de dados de produtos para o catálogo digital de uma empresa multinacional.",
                        "Realizei a adaptação e tradução de especificações técnicas de produtos entre Português, Espanhol e Inglês, garantindo a consistência e padronização da informação para o mercado internacional.",
                        "Utilizei <strong>Excel Avançado</strong> para processar, validar e organizar grandes volumes de dados de forma eficiente, assegurando a qualidade da informação para as plataformas online da companhia."
                    ]
                }
            ]
        },
        'titulos_secoes': {
            "formacao_academica": "Formação Principal",
            "resumo": "Resumo Profissional",
            "experiencia": "Experiência Profissional",
            "conhecimentos": "Conhecimentos Técnicos",
            "cursos": "Cursos e Certificações Complementares",
            "projetos": "Projetos Relevantes",
            "soft_skills": "Habilidades Interpessoais (Soft Skills)",
            "idiomas": "Idiomas"
        },
        'web': {
            'conhecimentos': ["HTML", "CSS", "JavaScript", "React", "TypeScript", "Git", "Engenharia de Software", "Teste de Software", "QA (Quality Assurance)"],
            'descricao_padrao_conhecimentos': {
                "HTML": "Criação de estruturas semânticas com HTML5.",
                "CSS": "Estilização de layouts responsivos com Flexbox e Grid.",
                "JavaScript": "Interatividade, manipulação de DOM e consumo de APIs.",
                "React": "Criação de interfaces com componentes e hooks.",
                "TypeScript": "Programação tipada para projetos escaláveis.",
                "Git": "Controle de versão com ramificações e merge.",
                "Engenharia de Software": "Aplicação de princípios de engenharia para o design, desenvolvimento e manutenção de software de qualidade.",
                "Teste de Software": "Criação e execução de planos de teste para garantir a qualidade e funcionalidade do software.",
                "QA (Quality Assurance)": "Aplicação de processos de Garantia de Qualidade para assegurar a entrega de um produto estável e confiável."
            },
            'cursos': ["Desenvolvimento Web Completo", "Python 3 na Web com Django", "Introdução a banco de dados com MySQL", "Curso Completo de PHP (2012)", "Terminal Linux", "Gestão Ágil de Projetos"],
            'descricao_padrao_cursos': {
                "Desenvolvimento Web Completo": "Formação Full-Stack abrangente, cobrindo desde o front-end (HTML5, CSS3, Bootstrap, JavaScript/ES6+) até o back-end (PHP 7 com OO, MVC e APIs) e banco de dados (MySQL). Inclui o desenvolvimento de 20 projetos práticos, como clones de aplicações reais e sistemas de e-commerce.",
                "Python 3 na Web com Django": "Desenvolvimento de aplicações web robustas com o framework Python Django.",
                "Introdução a banco de dados com MySQL": "Fundamentos de SQL e modelagem de dados com MySQL e PHPMyAdmin.",
                "Curso Completo de PHP (2012)": "Formação em desenvolvimento back-end com PHP e conexão com bancos de dados (SENAC/SC).",
                "Terminal Linux": "Curso focado no domínio do terminal Linux, abordando desde a navegação no sistema de arquivos e gerenciamento de permissões até a criação de programas com Shell Script para automação de tarefas.",
                "Gestão Ágil de Projetos": "Capacitação em metodologias ágeis para gestão de projetos de tecnologia. Cobre a implementação e as cerimônias de frameworks como Scrum e Kanban, além de tópicos avançados em liderança, gestão de riscos e contratos ágeis."
            }
        },
        'dados': {
            'conhecimentos': ["Python", "Pandas", "NumPy", "Matplotlib", "SQL", "Power BI", "Git", "Excel"],
            'descricao_padrao_conhecimentos': {
                "Python": "Análise de dados e automação de scripts com Python.",
                "Pandas": "Manipulação e tratamento de grandes volumes de dados.",
                "NumPy": "Computação numérica e operações com arrays.",
                "Matplotlib": "Criação de visualizações de dados estáticas e interativas.",
                "SQL": "Consultas complexas, junções e extração de dados de bancos relacionais.",
                "Power BI": "Desenvolvimento de dashboards e relatórios interativos.",
                "Git": "Controle de versão para projetos de dados.",
                "Excel": "Análise de dados e funções avançadas."
            },
            'cursos': ["O curso completo de Banco de Dados e SQL", "Machine Learning e Data Science de A a Z", "Data Science: Visualização de Dados", "Terminal Linux", "Gestão Ágil de Projetos", "Artificial Intelligence A-Z"],
            'descricao_padrao_cursos': {
                "O curso completo de Banco de Dados e SQL": "Curso prático de modelagem e administração de bancos de dados relacionais. Cobre a instalação, configuração e programação (SQL, T-SQL, PL/SQL) em múltiplos sistemas (MySQL, SQL Server, Oracle), incluindo rotinas de backup, procedures e triggers.",
                "Machine Learning e Data Science de A a Z": "Formação completa no fluxo de trabalho de Data Science, desde o pré-processamento de dados com Pandas e Scikit-learn até a construção e avaliação de modelos preditivos. Cobre os principais pilares de Machine Learning: Classificação, Regressão e Agrupamento, com projetos práticos em previsão de crédito, segmentação de clientes e análise de sentimentos.",
                "Data Science: Visualização de Dados": "Técnicas e ferramentas para criar visualizações de dados impactantes com Python.",
                "Terminal Linux": "Curso focado no domínio do terminal Linux, abordando desde a navegação no sistema de arquivos e gerenciamento de permissões até a criação de programas com Shell Script para automação de tarefas.",
                "Gestão Ágil de Projetos": "Capacitação em metodologias ágeis para gestão de projetos de tecnologia. Cobre a implementação e as cerimônias de frameworks como Scrum e Kanban, além de tópicos avançados em liderança, gestão de riscos e contratos ágeis.",
                "Artificial Intelligence A-Z": "Treinamento avançado em Inteligência Artificial focado na construção de agentes autônomos. Aborda desde Q-Learning e Deep Q-Learning até modelos de ponta como A3C, PPO e SAC, aplicados em otimização de processos e simulações. Inclui fine-tuning de LLMs (Llama 2)."
            }
        },
        'java_web': {
            'conhecimentos': ["Java", "Spring Boot", "SQL", "React", "Git", "Scrum", "DevOps", "Engenharia de Software", "Teste de Software", "Validação de Sistemas"],
            'descricao_padrao_conhecimentos': {
                "Java": "Desenvolvimento de aplicações back-end robustas com a plataforma Java e princípios de Orientação a Objetos.",
                "Spring Boot": "Criação de APIs RESTful e microserviços com o ecossistema Spring.",
                "SQL": "Consultas e modelagem de bancos de dados relacionais.",
                "React": "Desenvolvimento de interfaces reativas com componentes, hooks e estado global.",
                "Git": "Controle de versão avançado com GitFlow e colaboração em equipe.",
                "Scrum": "Aplicação de metodologias ágeis para gerenciamento de projetos.",
                "DevOps": "Conceitos de CI/CD, containers e cultura DevOps para integração e deploy.",
                "Engenharia de Software": "Aplicação de princípios de engenharia para o design, desenvolvimento e manutenção de software de qualidade.",
                "Teste de Software": "Criação e execução de planos de teste para garantir a qualidade e funcionalidade do software.",
                "Validação de Sistemas": "Validação de sistemas complexos baseada em requisitos para assegurar o comportamento esperado."
            },
            'cursos': ["Gestão Ágil de Projetos", "Terminal Linux"], 
            'descricao_padrao_cursos': {
                 "Gestão Ágil de Projetos": "Capacitação em metodologias ágeis para gestão de projetos de tecnologia. Cobre a implementação e as cerimônias de frameworks como Scrum e Kanban, além de tópicos avançados em liderança, gestão de riscos e contratos ágeis.",
                 "Terminal Linux": "Curso focado no domínio do terminal Linux, abordando desde a navegação no sistema de arquivos e gerenciamento de permissões até a criação de programas com Shell Script para automação de tarefas."
            }
        },
        'soft_skills': ["Comunicação clara", "Trabalho em equipe", "Resolução de problemas", "Adaptabilidade", "Gestão de tempo", "Aprendizado contínuo", "Proatividade", "Empatia"],
        'idiomas': {
            "Português": ("Nativo", "Domínio completo da língua."),
            "Inglês": ("Avançado", "Capaz de comunicar-se com fluência em contextos profissionais."),
            "Espanhol": ("Intermediário", "Compreensão de textos e conversas.")
        }
    },
    'en': {
        'dados_fixos': {
            "nome": "Felipe Schneider Herrmann",
            "email": "fsherrmann.dev@gmail.com",
            "telefone": "+55 (48) 99109-9898",
            "formacao_web": "Web Developer",
            "formacao_dados": "Data Analyst",
            "formacao_java_web": "Full-Stack Java Developer",
             "formacao_detalhada": """
                <li>
                    <strong>Web Development Training (600h)</strong> - SENAI / Joinville Mais Tec (In progress)
                    <br><em>Complete Full-Stack training focusing on Java/Spring for the back-end and React for the front-end, including agile methodologies and DevOps culture.</em>
                </li>
                <li>
                    <strong>Computer Engineering</strong> - Federal University of Santa Catarina (UFSC)
                    <br><em>Studied from 2013 to 2017, with a strong foundation in Logic, Algorithms, Data Structures, and Computer Architecture.</em>
                </li>
            """,
            "resumo_web": "Developer focused on creating modern, responsive, and high-performance interfaces, using market best practices in HTML, CSS, JavaScript, and React.",
            "resumo_dados": "Data analyst with experience in processing and adapting data for international projects. Skilled in extracting, translating, and visualizing information to generate business insights, with strong proficiency in Python (Pandas), SQL, and BI tools.",
            "resumo_java_web": "Full-Stack Developer with a strong background in Java and Spring Boot for the back-end, and React for the front-end. Experienced in creating RESTful APIs, managing databases, and applying agile methodologies.",
            "experiencias": [
                {
                    "cargo": "Project Analyst (Contractor)",
                    "empresa": "4C Innovation",
                    "periodo": "April 2025 - Present",
                    "pontos": [
                        "[Describe your main responsibility in the new role, e.g., Managing the project lifecycle...]",
                        "[Add another important task or result, e.g., Communicating with stakeholders to align scope...]"
                    ]
                },
                {
                    "cargo": "Engineering and Projects Intern",
                    "empresa": "4C Innovation",
                    "periodo": "April 2023 - April 2025",
                    "pontos": [
                        "Responsible for gathering, processing, and adapting product data for the company's digital catalog.",
                        "Carried out the adaptation and translation of technical product specifications between Portuguese, Spanish, and English, ensuring information consistency for the international market.",
                        "Utilized <strong>Advanced Excel</strong> to efficiently process, validate, and organize large volumes of information."
                    ]
                }
            ]
        },
        'titulos_secoes': {
            "formacao_academica": "Core Education",
            "resumo": "Professional Summary",
            "experiencia": "Professional Experience",
            "conhecimentos": "Technical Skills",
            "cursos": "Complementary Courses & Certifications",
            "projetos": "Relevant Projects",
            "soft_skills": "Soft Skills",
            "idiomas": "Languages"
        },
        'web': {
            'conhecimentos': ["HTML", "CSS", "JavaScript", "React", "TypeScript", "Git", "Software Engineering", "Software Testing", "QA (Quality Assurance)"],
            'descricao_padrao_conhecimentos': {
                "HTML": "Creation of semantic structures with HTML5.",
                "CSS": "Styling responsive layouts with Flexbox and Grid.",
                "JavaScript": "Interactivity, DOM manipulation, and API consumption.",
                "React": "Building interfaces with components and hooks.",
                "TypeScript": "Typed programming for scalable projects.",
                "Git": "Version control with branching and merging.",
                "Software Engineering": "Application of engineering principles to the design, development, and maintenance of quality software.",
                "Software Testing": "Creation and execution of test plans to ensure software quality and functionality.",
                "QA (Quality Assurance)": "Application of Quality Assurance processes to ensure the delivery of a stable and reliable product."
            },
            'cursos': ["Complete Web Development", "Python 3 on the Web with Django", "Introduction to Databases with MySQL", "Complete PHP Course (2012)", "Linux Terminal", "Agile Project Management"],
            'descricao_padrao_cursos': {
                "Complete Web Development": "Comprehensive Full-Stack training, covering from the front-end (HTML5, CSS3, Bootstrap, JavaScript/ES6+) to the back-end (PHP 7 with OOP, MVC & APIs) and databases (MySQL). Includes the development of 20 practical projects, such as clones of real-world applications and e-commerce systems.",
                "Python 3 on the Web with Django": "Development of robust web applications with the Python Django framework.",
                "Introduction to Databases with MySQL": "Fundamentals of SQL and data modeling with MySQL and PHPMyAdmin.",
                "Complete PHP Course (2012)": "Training in back-end development with PHP and database connection (SENAC/SC).",
                "Linux Terminal": "Course focused on mastering the Linux terminal, covering from file system navigation and permission management to creating programs with Shell Script for task automation.",
                "Agile Project Management": "Training in agile methodologies for technology project management. Covers the implementation and ceremonies of frameworks like Scrum and Kanban, in addition to advanced topics in leadership, risk management, and agile contracts."
            }
        },
        'dados': {
            'conhecimentos': ["Python", "Pandas", "NumPy", "Matplotlib", "SQL", "Power BI", "Git", "Excel"],
            'descricao_padrao_conhecimentos': {
                "Python": "Data analysis and script automation with Python.",
                "Pandas": "Manipulation and processing of large datasets.",
                "NumPy": "Numerical computing and array operations.",
                "Matplotlib": "Creation of static and interactive data visualizations.",
                "SQL": "Complex queries, joins, and data extraction from relational databases.",
                "Power BI": "Development of interactive dashboards and reports.",
                "Git": "Version control for data projects.",
                "Excel": "Data analysis and advanced functions."
            },
            'cursos': ["The Complete SQL and Database Bootcamp", "Machine Learning and Data Science A-Z", "Data Science: Data Visualization", "Linux Terminal", "Agile Project Management", "Artificial Intelligence A-Z"],
            'descricao_padrao_cursos': {
                "The Complete SQL and Database Bootcamp": "Practical course on relational database modeling and administration. Covers installation, configuration, and programming (SQL, T-SQL, PL/SQL) across multiple systems (MySQL, SQL Server, Oracle), including backup routines, procedures, and triggers.",
                "Machine Learning and Data Science A-Z": "Complete training in the Data Science workflow, from data pre-processing with Pandas and Scikit-learn to building and evaluating predictive models. Covers the main pillars of Machine Learning: Classification, Regression, and Clustering, with practical projects in credit scoring, customer segmentation, and sentiment analysis.",
                "Data Science: Data Visualization": "Techniques and tools to create impactful data visualizations with Python.",
                "Terminal Linux": "Course focused on mastering the Linux terminal, covering from file system navigation and permission management to creating programs with Shell Script for task automation.",
                "Agile Project Management": "Training in agile methodologies for technology project management. Covers the implementation and ceremonies of frameworks like Scrum and Kanban, in addition to advanced topics in leadership, risk management, and agile contracts.",
                "Artificial Intelligence A-Z": "Advanced training in Artificial Intelligence focused on building autonomous agents. Covers from Q-Learning and Deep Q-Learning to state-of-the-art models like A3C, PPO, and SAC, applied to process optimization and simulations. Includes fine-tuning LLMs (Llama 2)."
            }
        },
        'java_web': {
            'conhecimentos': ["Java", "Spring Boot", "SQL", "React", "Git", "Scrum", "DevOps", "Software Engineering", "Software Testing", "System Validation"],
            'descricao_padrao_conhecimentos': {
                "Java": "Development of robust back-end applications with the Java platform and OOP principles.",
                "Spring Boot": "Creation of RESTful APIs and microservices with the Spring ecosystem.",
                "SQL": "Querying and modeling of relational databases.",
                "React": "Development of reactive interfaces with components, hooks, and global state.",
                "Git": "Advanced version control with GitFlow and team collaboration.",
                "Scrum": "Application of agile methodologies for project management.",
                "DevOps": "Concepts of CI/CD, containers, and DevOps culture for integration and deployment.",
                "Software Engineering": "Application of engineering principles to the design, development, and maintenance of quality software.",
                "Software Testing": "Creation and execution of test plans to ensure software quality and functionality.",
                "System Validation": "Validation of complex systems based on requirements to ensure expected behavior."
            },
            'cursos': ["Agile Project Management", "Linux Terminal"], 
            'descricao_padrao_cursos': {
                "Agile Project Management": "Training in agile methodologies for technology project management. Covers the implementation and ceremonies of frameworks like Scrum and Kanban, in addition to advanced topics in leadership, risk management, and agile contracts.",
                "Linux Terminal": "Course focused on mastering the Linux terminal, covering from file system navigation and permission management to creating programs with Shell Script for task automation."
            }
        },
        'soft_skills': ["Clear communication", "Teamwork", "Problem-solving", "Adaptability", "Time management", "Continuous learning", "Proactivity", "Empathy"],
        'idiomas': {
            "Portuguese": ("Native", "Full command of the language."),
            "English": ("Advanced", "Able to communicate fluently in professional contexts."),
            "Spanish": ("Intermediate", "Comprehension of texts and conversations.")
        }
    }
}