# interface.py

import tkinter as tk
from data import (
    conhecimentos, cursos, soft_skills_opcoes,
    descricao_padrao_conhecimentos, descricao_padrao_cursos, idiomas_fixos
)
from projetos import filtrar_projetos
from gerador_curriculo import gerar_html, salvar_html, salvar_pdf

# Dados fixos do currículo
dados_fixos = {
    "nome": "Felipe Schneider Herrmann",
    "email": "fsherrmann.dev@gmail.com",
    "telefone": "(48) 99109-9898",
    "formacao": "Web Developer Front-End",
    "resumo": "Desenvolvedor com foco em interfaces modernas e responsivas.",
    "experiencia": "Estágio em Desenvolvimento Web - Empresa X (jan/2024 – abr/2024)"
}

class GeradorCurriculoApp:
    def __init__(self, root):
        self.root = root
        root.title("Gerador de Currículo HTML e PDF")
        root.state('zoomed')

        self.vars_conhecimentos = []
        self.vars_cursos = []
        self.vars_soft_skills = []
        self.descricoes_conhecimentos = {}
        self.descricoes_cursos = {}

        main = tk.Frame(root)
        main.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(main, text="Gerador de Currículo Personalizado", font=("Arial", 16, "bold")).pack(pady=10)

        conteudo = tk.Frame(main)
        conteudo.pack(fill="both", expand=True)

        # Conhecimentos
        frame_conhecimentos = tk.LabelFrame(conteudo, text="Conhecimentos", padx=10, pady=10)
        frame_conhecimentos.grid(row=0, column=0, sticky="nw", padx=10, pady=10)
        self.gerar_grade_horizontal(
            frame_conhecimentos,
            conhecimentos,
            self.vars_conhecimentos,
            self.descricoes_conhecimentos,
            descricao_padrao_conhecimentos
        )

        # Cursos
        frame_cursos = tk.LabelFrame(conteudo, text="Cursos", padx=10, pady=10)
        frame_cursos.grid(row=1, column=0, sticky="nw", padx=10, pady=10)
        self.gerar_grade_horizontal(
            frame_cursos,
            cursos,
            self.vars_cursos,
            self.descricoes_cursos,
            descricao_padrao_cursos
        )

        # Soft Skills
        frame_soft_skills = tk.LabelFrame(conteudo, text="Soft Skills", padx=10, pady=10)
        frame_soft_skills.grid(row=0, column=1, sticky="nw", padx=10, pady=10)
        for item in soft_skills_opcoes:
            var = tk.BooleanVar()
            chk = tk.Checkbutton(frame_soft_skills, text=item, variable=var)
            chk.pack(anchor="w")
            self.vars_soft_skills.append((item, var))

        # Projetos automáticos
        self.frame_projetos = tk.LabelFrame(conteudo, text="Projetos Sugeridos", padx=10, pady=10)
        self.frame_projetos.grid(row=1, column=1, sticky="nw", padx=10, pady=10)
        self.lista_projetos = tk.Listbox(self.frame_projetos, height=10, width=80)
        self.lista_projetos.pack()

        # Botões
        #tk.Button(main, text="Gerar Currículo HTML", font=("Arial", 12, "bold"),
        #          command=self.gerar_curriculo_html).pack(pady=(20, 5))

        tk.Button(main, text="Gerar PDF", font=("Arial", 12, "bold"),
                  command=self.gerar_curriculo_pdf).pack(pady=(0, 20))

    def gerar_grade_horizontal(self, frame, lista, var_list, descr_dict, descricoes_padrao, colunas=3):
        for idx, item in enumerate(lista):
            linha = idx // colunas
            coluna = idx % colunas
            cell = tk.Frame(frame)
            cell.grid(row=linha, column=coluna, padx=5, pady=5, sticky="w")
            var = tk.BooleanVar()
            chk = tk.Checkbutton(
                cell,
                text=item,
                variable=var,
                command=lambda i=item: [self.preencher_automatica(i, var_list, descr_dict, descricoes_padrao), self.atualizar_projetos()]
            )
            chk.pack(anchor="w")
            entry = tk.Entry(cell, width=30)
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

    def atualizar_projetos(self):
        self.lista_projetos.delete(0, tk.END)
        conhecimentos_ativos = [item for item, var, _ in self.vars_conhecimentos if var.get()]
        projetos = filtrar_projetos(conhecimentos_ativos)
        for projeto, tags in projetos:
            self.lista_projetos.insert(tk.END, f"{projeto['title']} [Tags: {', '.join(tags)}]")

    def gerar_curriculo_html(self):
        dados = self.coletar_dados()
        html = gerar_html(**dados)
        salvar_html(html)

    def gerar_curriculo_pdf(self):
        dados = self.coletar_dados()
        html = gerar_html(**dados)
        salvar_pdf(html)

    def coletar_dados(self):
        conhecimentos_selecionados = [
            (item, entry.get()) for item, var, entry in self.vars_conhecimentos if var.get()
        ]
        cursos_selecionados = [
            (item, entry.get()) for item, var, entry in self.vars_cursos if var.get()
        ]
        soft_skills = [item for item, var in self.vars_soft_skills if var.get()]
        tecnologias_ativas = [item for item, var, _ in self.vars_conhecimentos if var.get()]
        projetos = filtrar_projetos(tecnologias_ativas)
        return {
            "dados_fixos": dados_fixos,
            "conhecimentos": conhecimentos_selecionados,
            "cursos": cursos_selecionados,
            "soft_skills": soft_skills,
            "projetos": projetos
        }
