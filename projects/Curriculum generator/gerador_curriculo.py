import os
import webbrowser
from tkinter import messagebox
from weasyprint import HTML

def gerar_html(**dados):
    """Gera o código HTML completo do currículo, omitindo seções vazias."""
    dados_fixos = dados.get("dados_fixos", {})
    titulos = dados.get("titulos_secoes", {})
    conhecimentos = dados.get("conhecimentos", [])
    cursos = dados.get("cursos", [])
    soft_skills = dados.get("soft_skills", [])
    projetos = dados.get("projetos", [])
    idiomas = dados.get("idiomas", {})

    # ... (outros blocos de geração de HTML) ...

    html_bloco_projetos = ""
    if projetos:
        items_html = ""
        for projeto_info, tags in projetos:
            # --- LÓGICA DO LINK CONDICIONAL ADICIONADA AQUI ---
            link_html = ""
            if projeto_info.get("link"):  # Verifica se a chave 'link' existe e não está vazia
                link_html = f' - <a href="{projeto_info["link"]}">Ver Projeto</a>'
            
            items_html += f"""
            <li>
                <b>{projeto_info['title']}</b>{link_html}<br>
                <i>{projeto_info['description']}</i><br>
                <small><b>Tecnologias relevantes:</b> {', '.join(tags)}</small>
            </li>
            """
        html_bloco_projetos = f"<h2>{titulos.get('projetos', 'Projetos')}</h2><ul>{items_html}</ul>"

    # ... (resto da função e o template HTML) ...
    html_bloco_conhecimentos = ""
    if conhecimentos:
        items_html_conhecimentos = "".join(f"<li><b>{nome}:</b> {desc}</li>" for nome, desc in conhecimentos)
        html_bloco_conhecimentos = f"<h2>{titulos.get('conhecimentos', 'Conhecimentos')}</h2><ul>{items_html_conhecimentos}</ul>"

    html_bloco_cursos = ""
    if cursos:
        items_html_cursos = "".join(f"<li><b>{nome}:</b> {desc}</li>" for nome, desc in cursos)
        html_bloco_cursos = f"<h2>{titulos.get('cursos', 'Cursos')}</h2><ul>{items_html_cursos}</ul>"

    html_bloco_soft_skills = ""
    if soft_skills:
        items_html_soft_skills = "".join(f"<li>{skill}</li>" for skill in soft_skills)
        html_bloco_soft_skills = f"<h2>{titulos.get('soft_skills', 'Soft Skills')}</h2><ul>{items_html_soft_skills}</ul>"
    
    html_bloco_experiencia = ""
    experiencia_titulo = dados_fixos.get("experiencia_titulo")
    experiencia_pontos = dados_fixos.get("experiencia_pontos", [])
    if experiencia_titulo and experiencia_pontos:
        items_html_experiencia = "".join(f"<li>{ponto}</li>" for ponto in experiencia_pontos)
        html_bloco_experiencia = f"""
            <h2>{titulos.get('experiencia', 'Experiência Profissional')}</h2>
            <p><strong>{experiencia_titulo}</strong></p>
            <ul>
                {items_html_experiencia}
            </ul>
        """

    html_idiomas = ""
    for idioma, (nivel, desc) in idiomas.items():
        html_idiomas += f'<li><b>{idioma}:</b> {nivel} ({desc})</li>'

    html_completo = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Currículo - {dados_fixos.get('nome', 'Candidato')}</title>
        <style>
            /* Configuração de página A4 e margens */
            @page {{
                size: A4;
                margin: 15mm;
            }}

            /* Box sizing para evitar estouro */
            * {{
                box-sizing: border-box;
            }}

            body {{
                font-family: 'Helvetica Neue', Arial, sans-serif;
                line-height: 1.4;
                color: #333;
                margin: 0;
                padding: 0;
            }}

            .container {{
                width: 180mm;
                max-width: 100%;
                margin: auto;
                padding: 0;
            }}

            h1, h2 {{
                border-bottom: 2px solid #3498db;
                padding-bottom: 4px;
                color: #2c3e50;
                page-break-after: avoid;
            }}

            h1 {{
                text-align: center;
                border-bottom: none;
                margin-bottom: 4px;
            }}

            h2 {{
                margin-top: 20px;
                margin-bottom: 4px;
            }}

            #contato {{
                text-align: center;
                margin: -4px 0 12px;
                font-size: 1em;
            }}

            /* Quebra de linha e hifenização automática */
            p, li {{
                overflow-wrap: break-word;
                word-break: break-word;
                hyphens: auto;
            }}

            ul {{
                padding-left: 18px;
                list-style-type: square;
                margin: 4px 0;
            }}

            li {{
                margin-bottom: 6px;
            }}

            a {{
                color: #3498db;
                text-decoration: none;
            }}

            a:hover {{
                text-decoration: underline;
            }}

            small {{
                color: #555;
            }}

            p {{
                margin: 2px 0;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{dados_fixos.get('nome', '')}</h1>
            <p id="contato">
                {dados_fixos.get('email', '')} | {dados_fixos.get('telefone', '')}<br>
                <b>{dados_fixos.get('formacao', '')}</b>
            </p>

            <h2>{titulos.get('formacao_academica', 'Formação Principal')}</h2>
            <ul>{dados_fixos.get('formacao_detalhada', '')}</ul>
            
            <h2>{titulos.get('resumo', 'Resumo')}</h2>
            <p>{dados_fixos.get('resumo', '')}</p>
            
            {html_bloco_experiencia}

            {html_bloco_conhecimentos}
            
            {html_bloco_cursos}

            {html_bloco_projetos}

            {html_bloco_soft_skills}

            <h2>{titulos.get('idiomas', 'Idiomas')}</h2>
            <ul>{html_idiomas}</ul>
        </div>
    </body>
    </html>
    """
    return html_completo

def salvar_pdf(html):
    """Gera o PDF a partir da string HTML usando WeasyPrint e o abre no navegador."""
    path_pdf = os.path.abspath("curriculo_gerado.pdf")
    
    try:    
        HTML(string=html).write_pdf(path_pdf)
        messagebox.showinfo("PDF Gerado", f"PDF salvo com sucesso:\n{path_pdf}")
        webbrowser.open("file://" + path_pdf)
    except Exception as e:
        messagebox.showerror("Erro ao gerar PDF", f"Ocorreu um erro com o WeasyPrint:\n{str(e)}")
