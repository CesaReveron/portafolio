import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
MODEL = os.getenv("MODEL", "gpt-3.5-turbo")
API_URL = "https://api.openai.com/v1/chat/completions"

def generate_content(prompt, system_prompt=None):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    payload = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.7
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def analyze_log(log_content):
    prompt = f"""Analiza el siguiente log técnico e identifica:
1. Errores principales
2. Patrones de comportamiento
3. Posibles causas raíz
4. Recomendaciones

Log:
{log_content}"""

    system_prompt = "Eres un experto en diagnóstico técnico de sistemas."
    return generate_content(prompt, system_prompt)

def generate_documentation(data_summary):
    prompt = f"""Genera documentación técnica basada en este resumen de datos:

{data_summary}

Incluye:
- Descripción general
- Métricas principales
- Interpretación de resultados
- Conclusiones"""

    return generate_content(prompt)

if __name__ == "__main__":
    if not API_KEY:
        print("Error: API_KEY no configurada. Crea archivo .env con tu API_KEY")
    else:
        result = analyze_log("2026-05-13 10:00:00 ERROR Connection timeout\n2026-05-13 10:05:00 WARNING Retry attempt 1")
        print(result)