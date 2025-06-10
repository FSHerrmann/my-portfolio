import openai
import json
import os

def classify_email_content(api_key, email_body):
    client = openai.OpenAI(api_key=api_key)
    prompt = f"""
    Analyze the following email body from a job application process.
    Extract the following information and return it ONLY as a valid JSON object:
    1. "company_name": The name of the company.
    2. "job_role": The specific job role or title.
    3. "status": The current status of the application.
    4. "interview_date": The date of a scheduled interview.
    5. "interview_time": The time of a scheduled interview.

    The possible values for "status" are: "Applied", "Assessment", "Interview_HR", "Interview_Technical", "Offer", "Rejected", "Other".

    If the email is about scheduling an interview, please extract the date and time.
    - Return the date in YYYY-MM-DD format (e.g., 2025-06-10).
    - Return the time in HH:MM format (24-hour clock, e.g., 14:30).
    
    If any piece of information (including date or time) is not present, its value should be "Not Found".

    Here is the email body to analyze:
    ---
    {email_body}
    ---
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # ou "gpt-3.5-turbo" se preferir
            messages=[
                {"role": "system", "content": "You are a helpful assistant for classifying job application emails."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )
        json_response_text = response.choices[0].message.content.strip()
        json_response_text = json_response_text.replace("```json", "").replace("```", "")
        classified_data = json.loads(json_response_text)
        return classified_data
    except Exception as e:
        print(f"--- An unexpected error occurred during AI classification: {e} ---")
        return None
