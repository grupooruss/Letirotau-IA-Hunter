import requests
import json
import argparse
import time

# PARSE ARGUMENTOS

def parse_args():
    parser = argparse.ArgumentParser(description="Dorking Tool para búsqueda en múltiples plataformas")
    parser.add_argument("--target", required=True, help="Dominio o plataforma donde realizar la búsqueda")
    return parser.parse_args()

# LISTA OPTIMIZADA DE DORKS BASADOS EN IA Y DESARROLLO DE MODELOS
if __name__ == "__main__":
    args = parse_args()
    target = args.target

    dorks = [
        "AWS_SECRET_ACCESS_KEY", "DB_PASSWORD", "FIREBASE_API_KEY", "GOOGLE_APPLICATION_CREDENTIALS",
        "filename:.env", "filename:id_rsa", "filename:.git-credentials", "filename:config",
        "filename:.npmrc", "filename:settings.py", "filename:.dockercfg", "filename:.htpasswd",
        "filename:shadow", "filename:ssh_config", "filename:passwd", "filename:secrets.json",
        "password", "private_key", "access_token", "api_key", "client_secret",
        "AI API Key", "Chatbot API Key", "Whatsapp API", "telegram_bot_token",
        "filename:.chatbot_config", "filename:messaging_secrets", "AI model credentials",
        "openai_api_key", "llm_model_secret", "huggingface_token", "mlflow_credentials",
        "tensorflow_model_weights", "pytorch_model.pth", "bert_config.json",
        "gpt_training_data", "dataset_sensitive.csv", "confidential_finetune.json",
        "system_prompt", "hidden_prompt", "ai_model_deployment_config",
        "chatbot_memory_storage", "conversational_logs", "ai_inference_api",
        "vector_database_keys", "embedding_model_secrets", "secure_ai_tuning"
    ]

    search_engines = {
        "Google": "https://www.google.com/search?q=site:{}+{}",
        "Bing": "https://www.bing.com/search?q=site:{}+{}",
        "DuckDuckGo": "https://duckduckgo.com/html/?q=site:{}+{}",
        "Yahoo": "https://search.yahoo.com/search?p=site:{}+{}",
        "Baidu": "https://www.baidu.com/s?wd=site:{}+{}"
    }

    def perform_search(engine, url):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                print(f"[+] {engine} respondió correctamente para la búsqueda: {url}")
            else:
                print(f"[-] {engine} devolvió código de estado {response.status_code} para {url}")
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Error en la solicitud a {engine}: {e}")

    print(f"=== Iniciando búsqueda en {target} ===")
    for dork in dorks:
        for engine, base_url in search_engines.items():
            search_url = base_url.format(target, dork)
            print(f"\n[VERBOSE] Buscando en {engine}: {search_url}")
            perform_search(engine, search_url)
            time.sleep(2)  # Evitar bloqueos por múltiples solicitudes rápidas

# Division81 - Grupo Oruss Team.