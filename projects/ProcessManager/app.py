# app.py (VERSÃO FINAL - COM CORREÇÃO PARA SALVAR DATAS)
from email_reader import fetch_and_process_emails
from kanban_view import create_window 
import getpass
import json
import os
# --- 1. IMPORTAMOS AS FERRAMENTAS DE DATA ---
from datetime import datetime, date

from dotenv import load_dotenv
import os

load_dotenv()  # Carrega o .env

email_user = os.getenv('EMAIL_USER')
email_pass = os.getenv('EMAIL_PASS')
openai_api_key = os.getenv('OPENAI_API_KEY')

print(f"EMAIL_USER: {email_user}")
print(f"EMAIL_PASS: {email_pass}")
print(f"OPENAI_API_KEY: {openai_api_key}")



DATA_FILE = "applications.json"

# --- 2. CRIAMOS NOSSA FUNÇÃO "TRADUTORA" ---
def json_serializer(obj):
    """Tradutor para objetos que o JSON não entende por padrão."""
    # Se o objeto for do tipo datetime ou date...
    if isinstance(obj, (datetime, date)):
        # ...converta-o para uma string no formato padrão ISO (ex: '2025-06-05T22:54:00')
        return obj.isoformat()
    # Se for qualquer outro tipo de objeto que ele não entende, levante o erro padrão.
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")


# Em app.py

def load_data():
    """Carrega os dados das candidaturas do arquivo JSON de forma segura."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                # Tenta carregar o arquivo
                return json.load(f)
        except json.JSONDecodeError:
            # Se o arquivo estiver corrompido/vazio, avisa e retorna uma lista vazia
            print(f"WARNING: '{DATA_FILE}' is corrupted or empty. Starting fresh.")
            return []
    else:
        # Se o arquivo não existe, apenas retorna uma lista vazia
        return []

def save_data(applications):
    """Salva a lista completa de candidaturas no arquivo JSON."""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        # --- 3. USAMOS NOSSO "TRADUTOR" AO SALVAR ---
        # O parâmetro 'default' diz ao json.dump para usar nossa função
        # para qualquer tipo de dado que ele não reconheça.
        json.dump(applications, f, ensure_ascii=False, indent=4, default=json_serializer)


def main():
    """Fluxo principal: Carregar -> Buscar Apenas Novos -> Combinar -> Exibir -> Salvar."""
    
    all_applications = load_data()
    print(f"INFO: Loaded {len(all_applications)} applications from '{DATA_FILE}'.")

    credentials = {
    'user': email_user,
    'pass': email_pass,
    'api_key': openai_api_key
}

    if not credentials['pass'] or not credentials['api_key']:
        print("Credentials not provided. Skipping email check.")
        newly_found_apps = []
    else:
        newly_found_apps = fetch_and_process_emails(credentials, all_applications)

    if not credentials['pass'] or not credentials['api_key']:
        print("Credentials not provided. Skipping email check.")
        newly_found_apps = []
    else:
        newly_found_apps = fetch_and_process_emails(credentials, all_applications)

    if newly_found_apps:
        # Adiciona apenas as novas aplicações à lista principal
        all_applications.extend(newly_found_apps)
    
    if all_applications:
        print(f"\nLaunching window with {len(all_applications)} total applications...")
        create_window(all_applications)
        
        print("\nINFO: Window closed. Saving all data...")
        save_data(all_applications) # Salva a lista completa ao fechar
    else:
        print("\nNo applications to display. Exiting.")
        return
    
    print("\n--- Application Closed. Goodbye! ---")

if __name__ == '__main__':
    main()