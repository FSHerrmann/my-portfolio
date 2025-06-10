# email_reader.py (versão final com múltiplas buscas simples)
import imaplib, email, traceback
from email.header import decode_header
from ai_classifier import classify_email_content 

def get_email_content(message_bytes):
    # Esta função não muda
    msg = email.message_from_bytes(message_bytes)
    subject_header = decode_header(msg["Subject"])
    subject = ""
    for text, charset in subject_header:
        if isinstance(text, bytes):
            subject += text.decode(charset if charset else "utf-8")
        else:
            subject += text
    sender = msg.get("From")
    date = msg.get("Date")
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))
            if content_type == "text/plain" and "attachment" not in content_disposition:
                try:
                    charset = part.get_content_charset() or "utf-8"
                    body = part.get_payload(decode=True).decode(charset)
                    break 
                except: pass
    else:
        try:
            charset = msg.get_content_charset() or "utf-8"
            body = msg.get_payload(decode=True).decode(charset)
        except: pass
    return {"subject": subject, "sender": sender, "date": date, "body": body}

def fetch_and_process_emails(credentials, existing_applications):
    """Busca e-mails usando múltiplas buscas simples e processa apenas os novos."""
    IMAP_SERVER = "imap.gmail.com"
    newly_processed_apps = []

    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(credentials['user'], credentials['pass'])
        mail.select("inbox")

        keywords = [
            "vaga", "entrevista", "inscricao", "candidatura", "agendamento",
            "confirmacao", "processo seletivo", "assessment", "teste",
            "desafio", "retorno", "feedback", "proxima etapa", "application",
            "job", "career", "selection", "recrutamento", "contratacao",
            "curriculo", "cv", "resume", "hiring", "selecao", "triagem",
            "aprovacao", "proposta", "reprovacao"
        ]

        
        # --- NOVA LÓGICA DE BUSCA ---
        all_server_ids = set() # Usamos um set para evitar IDs duplicados automaticamente
        print(f"INFO: Performing {len(keywords)} individual searches...")

        for keyword in keywords:
            # Para cada palavra-chave, fazemos uma busca simples
            search_criteria_str = f'(TEXT "{keyword}")'
            search_criteria_bytes = search_criteria_str.encode('utf-8')
            
            status, messages = mail.search(None, search_criteria_bytes)
            
            if status == 'OK' and messages[0]:
                # Adicionamos os IDs encontrados ao nosso conjunto
                ids = {email_id.decode() for email_id in messages[0].split()}
                all_server_ids.update(ids)
        
        print(f"INFO: Total unique email IDs found on server: {len(all_server_ids)}")

        saved_ids = {app.get('email_id') for app in existing_applications}
        new_ids_to_process = all_server_ids - saved_ids

        if not new_ids_to_process:
            print("INFO: No new emails found on the server to process.")
        else:
            print(f"INFO: Found {len(new_ids_to_process)} new emails to process.")
            for email_id_str in new_ids_to_process:
                email_id_bytes = email_id_str.encode()
                status, msg_data = mail.fetch(email_id_bytes, "(RFC822)")
                if status == "OK":
                    for response_part in msg_data:
                        if isinstance(response_part, tuple):
                            email_content = get_email_content(response_part[1])
                            if email_content["body"]:
                                classified_data = classify_email_content(credentials['api_key'], email_content["body"])
                                if classified_data:
                                    classified_data['email_id'] = email_id_str
                                    classified_data['date'] = email_content['date']
                                    newly_processed_apps.append(classified_data)
                            break
        mail.logout()
    except Exception as e:
        print(f"ERROR during email fetch: {e}")
        # Se um erro ocorrer, é importante retornar a lista vazia
        # para não apagar os dados existentes no app.py
        return []
    
    return newly_processed_apps