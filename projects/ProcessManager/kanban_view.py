# kanban_view.py (versão simplificada e estável)
import PySimpleGUI as sg
from dateutil import parser as date_parser
from datetime import datetime
from PySimpleGUI import Push

sg.theme("DarkGray1")

def create_card(application):
    # Esta função está correta e não precisa de mudanças
    company = application.get('company_name', 'N/A')
    role = application.get('job_role', 'N/A')
    status = application.get('status', 'Other')
    interview_date = application.get('interview_date', 'Not Found')
    formatted_date = application.get('formatted_date', '-')

    if interview_date != "Not Found":
        etapa_info = f"{status} / {interview_date}"
    else:
        etapa_info = status

    if status in ['Rejected']: status_color = '#E57373'
    elif status in ['Applied', 'Other']: status_color = '#B0BEC5'
    else: status_color = '#81C784'
        
    BACKGROUND_COLOR = '#F5F5F5'
    TEXT_COLOR = '#212121'
    SUBTEXT_COLOR = '#757575'

    card_layout = [
        [
            sg.Text('●', font=("Helvetica", 18), text_color=status_color, background_color=BACKGROUND_COLOR), 
            sg.Text(company, font=("Helvetica", 14, "bold"), background_color=BACKGROUND_COLOR, text_color=TEXT_COLOR),
            Push(background_color=BACKGROUND_COLOR),
            sg.Text(formatted_date, font=("Helvetica", 9), background_color=BACKGROUND_COLOR, text_color=SUBTEXT_COLOR)
        ],
        [sg.Text(etapa_info, font=("Helvetica", 10, 'italic'), background_color=BACKGROUND_COLOR, text_color=SUBTEXT_COLOR, pad=((25,0),0))],
        [sg.Text(role, font=("Helvetica", 11), background_color=BACKGROUND_COLOR, text_color=TEXT_COLOR, pad=((25,0),(5,0)))],
    ]
    
    return sg.Frame('', card_layout, pad=(10,10), expand_x=True, background_color=BACKGROUND_COLOR, border_width=1)


def create_window(applications):
    """Cria e exibe a janela com a lista de cartões (sem atualização automática)."""
    
    # Processa e ordena as aplicações pela data do e-mail
    for app in applications:
        try:
            app['datetime_obj'] = date_parser.parse(app.get('date', ''))
            app['formatted_date'] = app['datetime_obj'].strftime('%d/%m/%Y')
        except (ValueError, TypeError):
            app['datetime_obj'] = datetime.min
            app['formatted_date'] = '-'
            
    sorted_applications = sorted(applications, key=lambda x: x['datetime_obj'], reverse=True)

    # Cria a lista de layouts dos cartões
    card_list_layout = [[create_card(app)] for app in sorted_applications]

    main_layout = [
        [sg.Text("All Job Applications", font=("Helvetica", 16, "bold"))],
        [sg.Column(card_list_layout, scrollable=True, vertical_scroll_only=True, expand_x=True, expand_y=True)]
    ]

    window = sg.Window("Job Application Manager", main_layout, resizable=True, finalize=True, size=(450, 600))

    # Loop de eventos simples
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
            
    window.close()