import tkinter as tk
from tkinter import messagebox
import webbrowser
import os
import pdfkit

# Dados fixos do currículo
dados_fixos = {
    "nome": "Felipe Schneider Herrmann",
    "email": "fsherrmann.dev@gmail.com",
    "telefone": "(48) 99109-9898",
    "formacao": "Web Developer Front-End",
    "resumo": "Desenvolvedor com foco em interfaces modernas e responsivas.",
    "experiencia": "Estágio em Desenvolvimento Web - Empresa X (jan/2024 – abr/2024)"
}

# Lista de projetos disponíveis com tags
projetos_disponiveis = [
    {
        "title": "Week 6 – Hangman Game with Login and LocalStorage",
        "description": "A Hangman game with a login screen that saves the player's nickname in localStorage. Includes word selection, letter guessing with validation, display of correct and wrong letters, win message with player's nickname, and game restart.",
        "link": "https://fsherrmann.github.io/my-portfolio/projects/Senai/week6/week6.html",
        "tags": ["HTML", "CSS", "JavaScript", "Game Development", "LocalStorage", "Event Handling"]
    }
]

# Conjunto para armazenar títulos de projetos que o usuário removeu manualmente
projetos_excluidos = set()

# Função para filtrar projetos com base nos conhecimentos selecionados
def filtrar_projetos(conhecimentos_selecionados):
    filtrados = []
    for projeto in projetos_disponiveis:
        if projeto['title'] in projetos_excluidos:
            continue  # Ignora se foi excluído manualmente
        if any(tag in conhecimentos_selecionados for tag in projeto['tags']):
            filtrados.append(projeto)
    return filtrados

# Exemplo de uso no contexto de geração do currículo:
conhecimentos_ativos = ["HTML", "JavaScript"]

# Atualiza a lista de projetos a serem incluídos automaticamente
projetos_a_incluir = filtrar_projetos(conhecimentos_ativos)

# Para remover um projeto manualmente:
def excluir_projeto(titulo_projeto):
    projetos_excluidos.add(titulo_projeto)

# Exemplo:
# excluir_projeto("Week 6 – Hangman Game with Login and LocalStorage")

# Listas e descrições padrão
conhecimentos = ["HTML", "CSS", "JavaScript", "React", "Vue.js", "TypeScript", "Git", "Tailwind", "Figma"]
cursos = ["React Avançado", "JavaScript Moderno", "UX/UI Design", "Responsividade Web"]
soft_skills_opcoes = [
    "Comunicação clara",
    "Trabalho em equipe",
    "Resolução de problemas",
    "Adaptabilidade",
    "Gestão de tempo",
    "Aprendizado contínuo",
    "Proatividade",
    "Empatia"
]
descricao_padrao_conhecimentos = {
    "HTML": "Criação de estruturas semânticas com HTML5.",
    "CSS": "Estilização de layouts responsivos com Flexbox e Grid.",
    "JavaScript": "Interatividade, manipulação de DOM e consumo de APIs.",
    "React": "Criação de interfaces com componentes e hooks.",
    "Vue.js": "Desenvolvimento reativo com Vue CLI e Vuex.",
    "TypeScript": "Programação tipada em projetos escaláveis.",
    "Git": "Controle de versão com ramificações e merge.",
    "Tailwind": "Estilização rápida e utilitária com Tailwind CSS.",
    "Figma": "Criação e prototipagem de interfaces no Figma."
}
descricao_padrao_cursos = {
    "React Avançado": "Curso de React com foco em hooks, context API e performance.",
    "JavaScript Moderno": "Exploração de ES6+, async/await e boas práticas.",
    "UX/UI Design": "Princípios de usabilidade e design centrado no usuário.",
    "Responsividade Web": "Layouts flexíveis com media queries e mobile-first."
}
idiomas_fixos = {
    "Português": ("Fluente", "Domínio completo da língua, inclusive em ambientes técnicos."),
    "Inglês": ("Avançado", "Capaz de comunicar-se com fluência em contextos profissionais."),
    "Espanhol": ("Intermediário", "Compreensão de textos e conversas em ritmo moderado.")
}

class GeradorCurriculo:
    def __init__(self, root):
        self.root = root
        root.title("Gerador de Currículo HTML e PDF")
        root.state('zoomed')

        self.vars_conhecimentos = []
        self.vars_cursos = []
        self.vars_soft_skills = []
        self.projetos = []
        self.descricoes_conhecimentos = {}
        self.descricoes_cursos = {}

        self.caminho_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
        self.pdf_config = pdfkit.configuration(wkhtmltopdf=self.caminho_wkhtmltopdf)

        main = tk.Frame(root)
        main.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(main, text="Gerador de Currículo Personalizado", font=("Arial", 16, "bold")).pack(pady=10)

        conteudo = tk.Frame(main)
        conteudo.pack(fill="both", expand=True)

        frame_conhecimentos = tk.LabelFrame(conteudo, text="Conhecimentos", padx=10, pady=10)
        frame_conhecimentos.grid(row=0, column=0, sticky="nw", padx=10, pady=10)
        self.gerar_grade_horizontal(frame_conhecimentos, conhecimentos, self.vars_conhecimentos, self.descricoes_conhecimentos, descricao_padrao_conhecimentos)

        frame_cursos = tk.LabelFrame(conteudo, text="Cursos", padx=10, pady=10)
        frame_cursos.grid(row=1, column=0, sticky="nw", padx=10, pady=10)
        self.gerar_grade_horizontal(frame_cursos, cursos, self.vars_cursos, self.descricoes_cursos, descricao_padrao_cursos)

        frame_soft_skills = tk.LabelFrame(conteudo, text="Soft Skills", padx=10, pady=10)
        frame_soft_skills.grid(row=0, column=1, sticky="nw", padx=10, pady=10)
        for item in soft_skills_opcoes:
            var = tk.BooleanVar()
            chk = tk.Checkbutton(frame_soft_skills, text=item, variable=var)
            chk.pack(anchor="w")
            self.vars_soft_skills.append((item, var))

        frame_projetos = tk.LabelFrame(conteudo, text="Projetos (Nome e Link)", padx=10, pady=10)
        frame_projetos.grid(row=1, column=1, sticky="nw", padx=10, pady=10)
        self.entrada_projeto = tk.Entry(frame_projetos, width=60)
        self.entrada_projeto.pack()
        tk.Button(frame_projetos, text="Adicionar Projeto", command=self.adicionar_projeto).pack(pady=5)
        self.lista_projetos = tk.Listbox(frame_projetos, height=6, width=80)
        self.lista_projetos.pack()

        tk.Button(main, text="Gerar Currículo HTML", font=("Arial", 12, "bold"),
                  command=self.gerar_curriculo_html).pack(pady=(20, 5))

        tk.Button(main, text="Gerar PDF", font=("Arial", 12, "bold"),
                  command=self.gerar_pdf).pack(pady=(0, 20))

    def gerar_grade_horizontal(self, frame, lista, var_list, descr_dict, descricoes_padrao, colunas=3):
        for idx, item in enumerate(lista):
            linha = idx // colunas
            coluna = idx % colunas
            cell = tk.Frame(frame)
            cell.grid(row=linha, column=coluna, padx=5, pady=5, sticky="w")
            var = tk.BooleanVar()
            chk = tk.Checkbutton(cell, text=item, variable=var,
                                 command=lambda i=item: self.preencher_automatica(i, var_list, descr_dict, descricoes_padrao))
            chk.pack(anchor="w")
            entry = tk.Entry(cell, width=30)
            entry.insert(0, "")
            entry.config(state="disabled")
            entry.pack()
            var_list.append((item, var, entry))
            descr_dict[item] = entry

    def preencher_automatica(self, item, lista_variaveis, dicionario_descricoes, descricoes_padrao):
        for nome, var, entry in lista_variaveis:
            if nome == item:
                if var.get():
                    entry.config(state="normal")
                    entry.delete(0, tk.END)
                    entry.insert(0, descricoes_padrao.get(item, ""))
                else:
                    entry.delete(0, tk.END)
                    entry.config(state="disabled")

    def adicionar_projeto(self):
        entrada = self.entrada_projeto.get().strip()
        if entrada:
            self.projetos.append(entrada)
            self.lista_projetos.insert(tk.END, entrada)
            self.entrada_projeto.delete(0, tk.END)

    def gerar_curriculo_html(self):
        html = self.montar_html()
        tecnologias_ativas = [item for item, _, _ in self.vars_conhecimentos if _.get()]
        projetos_automaticos = filtrar_projetos(tecnologias_ativas)        
        with open("curriculo_gerado.html", "w", encoding="utf-8") as f:
            f.write(html)
        messagebox.showinfo("Sucesso", "Currículo HTML gerado com sucesso!")
        webbrowser.open("file://" + os.path.abspath("curriculo_gerado.html"))

    def gerar_pdf(self):
        html = self.montar_html()
        tecnologias_ativas = [item for item, _, _ in self.vars_conhecimentos if _.get()]
        projetos_automaticos = filtrar_projetos(tecnologias_ativas)
        html_path = os.path.abspath("curriculo_gerado.html")
        output_path = os.path.abspath("curriculo_gerado.pdf")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html)
        try:
            pdfkit.from_file(html_path, output_path, configuration=self.pdf_config)
            messagebox.showinfo("PDF Gerado", f"PDF salvo com sucesso:\n{output_path}")
            webbrowser.open(f"file://{output_path}")
        except Exception as e:
            messagebox.showerror("Erro ao gerar PDF", str(e))

    def montar_html(self):
        conhecimentos_selecionados = [
            (item, self.descricoes_conhecimentos[item].get())
            for item, var, _ in self.vars_conhecimentos if var.get()
        ]
        cursos_selecionados = [
            (item, self.descricoes_cursos[item].get())
            for item, var, _ in self.vars_cursos if var.get()
        ]
        soft_skills = [item for item, var in self.vars_soft_skills if var.get()]
        
        # ✅ Geração correta dos projetos automáticos aqui dentro
        tecnologias_ativas = [item for item, _, _ in self.vars_conhecimentos if _ .get()]
        projetos_automaticos = filtrar_projetos(tecnologias_ativas)

        html = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Currículo - {dados_fixos['nome']}</title>
    <style>
        body {{
            font-family: 'Segoe UI', sans-serif;
            background-color: #ffffff;
            color: #444444;
            padding: 40px;
        }}
        h1 {{
            color: #8e44ad;
            font-size: 28px;
            margin-bottom: 5px;
        }}
        h2 {{
            color: #8e44ad;
            margin-top: 30px;
            margin-bottom: 10px;
        }}
        .section {{
            border-bottom: 1px solid #cccccc;
            padding-bottom: 15px;
            margin-bottom: 15px;
        }}
        ul {{
            list-style-type: disc;
            padding-left: 20px;
        }}
        a {{
            color: #3498db;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <h1>{dados_fixos['nome']}</h1>
    <p><strong>Email:</strong> {dados_fixos['email']}<br>
       <strong>Telefone:</strong> {dados_fixos['telefone']}<br>
       <strong>Formação:</strong> {dados_fixos['formacao']}</p>

    <div class="section">
        <h2>Resumo Profissional</h2>
        <p>{dados_fixos['resumo']}</p>
    </div>

    <div class="section">
        <h2>Experiência</h2>
        <p>{dados_fixos['experiencia']}</p>
    </div>

    <div class="section">
        <h2>Conhecimentos</h2>
        <ul>
            {''.join(f"<li><strong>{item}:</strong> {desc}</li>" for item, desc in conhecimentos_selecionados)}
        </ul>
    </div>

    <div class="section">
        <h2>Idiomas</h2>
        <ul>
            {''.join(f"<li><strong>{idioma}:</strong> {nivel} — {descricao}</li>" for idioma, (nivel, descricao) in idiomas_fixos.items())}
        </ul>
    </div>

    <div class="section">
        <h2>Cursos</h2>
        <ul>
            {''.join(f"<li><strong>{item}:</strong> {desc}</li>" for item, desc in cursos_selecionados)}
        </ul>
    </div>

    {"<div class='section'><h2>Soft Skills</h2><ul>" + ''.join(f"<li>{skill}</li>" for skill in soft_skills) + "</ul></div>" if soft_skills else ""}

    <div class="section">
        <h2>Projetos</h2>
        <ul>
            {''.join(f"<li><strong>{p['title']}</strong>: {p['description']} <a href='{p['link']}' target='_blank'>Ver</a></li>" for p in projetos_automaticos)}
            {''.join(f"<li><a href='{item.split()[-1]}' target='_blank'>{item}</a></li>" for item in self.projetos)}
        </ul>
    </div>
</body>
</html>
"""
        return html

# Execução
if __name__ == "__main__":
    root = tk.Tk()
    app = GeradorCurriculo(root)
    root.mainloop()
