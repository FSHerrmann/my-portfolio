# gerador_curriculo.py

import os
import pdfkit
from tkinter import messagebox
import webbrowser
from data import idiomas_fixos

# Configuração para wkhtmltopdf
caminho_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
pdf_config = pdfkit.configuration(wkhtmltopdf=caminho_wkhtmltopdf)

# Geração do HTML
def gerar_html(dados_fixos, conhecimentos, cursos, soft_skills, projetos):
    html = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Currículo - {dados_fixos['nome']}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
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
            {''.join(f"<li><strong>{item}:</strong> {desc}</li>" for item, desc in conhecimentos)}
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
            {''.join(f"<li><strong>{item}:</strong> {desc}</li>" for item, desc in cursos)}
        </ul>
    </div>

    {"<div class='section'><h2>Soft Skills</h2><ul>" + ''.join(f"<li>{skill}</li>" for skill in soft_skills) + "</ul></div>" if soft_skills else ""}

    <div class="section">
        <h2>Projetos Relevantes</h2>
        <ul>
            {''.join(f"<li><strong>{p['title']}</strong> — Tags: {', '.join(tags)} — <a href='{p['link']}' target='_blank'>Ver projeto</a></li>" for p, tags in projetos)}

        </ul>
    </div>
</body>
</html>
"""
    return html

# Salva o HTML e abre no navegador
def salvar_html(html):
    path = "curriculo_gerado.html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    messagebox.showinfo("Sucesso", "Currículo HTML gerado com sucesso!")
    webbrowser.open("file://" + os.path.abspath(path))

# Gera o PDF a partir do HTML salvo
def salvar_pdf(html):
    path_html = os.path.abspath("curriculo_gerado.html")
    path_pdf = os.path.abspath("curriculo_gerado.pdf")
    with open(path_html, "w", encoding="utf-8") as f:
        f.write(html)
    try:
        pdfkit.from_file(path_html, path_pdf, configuration=pdf_config)
        messagebox.showinfo("PDF Gerado", f"PDF salvo com sucesso:\n{path_pdf}")
        webbrowser.open("file://" + path_pdf)
    except Exception as e:
        messagebox.showerror("Erro ao gerar PDF", str(e))
