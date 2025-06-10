# interface.py

import tkinter as tk
from data import curriculo_data
from projetos import filtrar_projetos
from gerador_curriculo import gerar_html, salvar_pdf

class GeradorCurriculoApp:
    def __init__(self, root):
        self.root = root
        root.title("Gerador de Currículo Dinâmico")
        root.state('zoomed')

        self.lingua_var = tk.StringVar(value='pt')
        self.area_var = tk.StringVar(value='web')

        main_frame = tk.Frame(root)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        opcoes_frame = tk.Frame(main_frame)
        opcoes_frame.pack(fill='x', pady=10)

        tk.Label(opcoes_frame, text="Idioma:", font=("Arial", 10, "bold")).pack(side='left', padx=(0, 5))
        tk.Radiobutton(opcoes_frame, text="PT-BR", variable=self.lingua_var, value='pt', command=self.reconstruir_interface).pack(side='left')
        tk.Radiobutton(opcoes_frame, text="EN-US", variable=self.lingua_var, value='en', command=self.reconstruir_interface).pack(side='left')

        tk.Label(opcoes_frame, text="Área:", font=("Arial", 10, "bold")).pack(side='left', padx=(20, 5))
        tk.Radiobutton(opcoes_frame, text="Web Dev", variable=self.area_var, value='web', command=self.reconstruir_interface).pack(side='left')
        tk.Radiobutton(opcoes_frame, text="Java Web", variable=self.area_var, value='java_web', command=self.reconstruir_interface).pack(side='left')
        tk.Radiobutton(opcoes_frame, text="Dados", variable=self.area_var, value='dados', command=self.reconstruir_interface).pack(side='left')

        self.conteudo_frame = tk.Frame(main_frame)
        self.conteudo_frame.pack(fill="both", expand=True)

        tk.Button(main_frame, text="Gerar Currículo em PDF", font=("Arial", 12, "bold"),
                  command=self.gerar_curriculo_pdf).pack(pady=(20, 5))

        self.reconstruir_interface()

    def limpar_conteudo(self):
        for widget in self.conteudo_frame.winfo_children():
            widget.destroy()

    def reconstruir_interface(self):
        self.limpar_conteudo()

        lingua = self.lingua_var.get()
        area = self.area_var.get()

        dados_atuais = curriculo_data[lingua][area]
        soft_skills_atuais = curriculo_data[lingua]['soft_skills']

        self.vars_conhecimentos = []
        self.vars_cursos = []
        self.vars_soft_skills = []
        
        left_frame = tk.Frame(self.conteudo_frame)
        left_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))

        right_frame = tk.Frame(self.conteudo_frame)
        right_frame.pack(side='right', fill='both', expand=True, padx=(10, 0))

        frame_conhecimentos = tk.LabelFrame(left_frame, text="Conhecimentos", padx=10, pady=10)
        frame_conhecimentos.pack(fill="x", anchor="n", pady=(0, 10))
        self.gerar_grade_horizontal(
            frame_conhecimentos,
            dados_atuais.get('conhecimentos', []),
            self.vars_conhecimentos,
            dados_atuais.get('descricao_padrao_conhecimentos', {})
        )

        frame_cursos = tk.LabelFrame(left_frame, text="Cursos", padx=10, pady=10)
        frame_cursos.pack(fill="x", anchor="n")
        self.gerar_grade_horizontal(
            frame_cursos,
            dados_atuais.get('cursos', []),
            self.vars_cursos,
            dados_atuais.get('descricao_padrao_cursos', {})
        )

        frame_soft_skills = tk.LabelFrame(right_frame, text="Soft Skills", padx=10, pady=10)
        frame_soft_skills.pack(fill='x', anchor='n', pady=(0, 10))
        for item in soft_skills_atuais:
            var = tk.BooleanVar()
            chk = tk.Checkbutton(frame_soft_skills, text=item, variable=var)
            chk.pack(anchor="w")
            self.vars_soft_skills.append((item, var))

        self.frame_projetos = tk.LabelFrame(right_frame, text="Projetos Sugeridos", padx=10, pady=10)
        self.frame_projetos.pack(fill='both', expand=True, anchor='n')
        self.lista_projetos = tk.Listbox(self.frame_projetos, height=15)
        self.lista_projetos.pack(fill='both', expand=True)

        self.atualizar_projetos()

    def gerar_grade_horizontal(self, frame, lista, var_list, descricoes_padrao, colunas=2):
        for idx, item in enumerate(lista):
            linha = idx // colunas
            coluna = idx % colunas

            cell = tk.Frame(frame)
            cell.grid(row=linha, column=coluna, padx=5, pady=5, sticky="w")

            var = tk.BooleanVar()
            entry = tk.Entry(cell, width=30)
            
            command = lambda i=item, v=var, e=entry, d=descricoes_padrao: self.on_check_change(i, v, e, d)

            chk = tk.Checkbutton(cell, text=item, variable=var, command=command)
            chk.pack(anchor="w")

            entry.config(state="disabled")
            entry.pack(anchor="w", fill="x", expand=True)

            var_list.append((item, var, entry))

    def on_check_change(self, item, var, entry, descricoes_padrao):
        if var.get():
            entry.config(state="normal")
            entry.delete(0, tk.END)
            entry.insert(0, descricoes_padrao.get(item, ""))
        else:
            entry.delete(0, tk.END)
            entry.config(state="disabled")
        self.atualizar_projetos()

    def atualizar_projetos(self):
        self.lista_projetos.delete(0, tk.END)
        area = self.area_var.get()
        conhecimentos_ativos = [item for item, var, _ in self.vars_conhecimentos if var.get()]
        projetos = filtrar_projetos(conhecimentos_ativos, area)
        for projeto, tags in projetos:
            self.lista_projetos.insert(tk.END, f"{projeto['title']} [Tags: {', '.join(tags)}]")

    def coletar_dados(self):
        lingua = self.lingua_var.get()
        area = self.area_var.get()
        
        base_dados = curriculo_data[lingua]
        
        dados_fixos_coletados = base_dados['dados_fixos'].copy()
        dados_fixos_coletados['formacao'] = base_dados['dados_fixos'][f'formacao_{area}']
        dados_fixos_coletados['resumo'] = base_dados['dados_fixos'][f'resumo_{area}']

        conhecimentos_selecionados = [(item, entry.get()) for item, var, entry in self.vars_conhecimentos if var.get()]
        cursos_selecionados = [(item, entry.get()) for item, var, entry in self.vars_cursos if var.get()]
        soft_skills = [item for item, var in self.vars_soft_skills if var.get()]
        
        conhecimentos_ativos = [item for item, var, _ in self.vars_conhecimentos if var.get()]
        projetos_filtrados = filtrar_projetos(conhecimentos_ativos, area)
        
        return {
            "dados_fixos": dados_fixos_coletados,
            "titulos_secoes": base_dados['titulos_secoes'],
            "conhecimentos": conhecimentos_selecionados,
            "cursos": cursos_selecionados,
            "soft_skills": soft_skills,
            "projetos": projetos_filtrados,
            "idiomas": base_dados['idiomas']
        }

    def gerar_curriculo_pdf(self):
        dados = self.coletar_dados()
        html = gerar_html(**dados)
        salvar_pdf(html)