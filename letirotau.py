import asyncio
import aiohttp
import requests
import argparse
import re
import openai
from fake_useragent import UserAgent
from stem import Signal
from stem.control import Controller

# Configurar API Keys
OPENAI_API_KEY = "TU_OPENAI_API_KEY"
SERPAPI_KEY = "TU_SERPAPI_KEY"

HEADERS = {"User-Agent": UserAgent().random}

# Cargar Dorks desde un archivo externo
def load_dorks(file_path="dorks.txt"):
    """Carga dorks desde un archivo de texto"""
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        return [
            "AWS_SECRET_ACCESS_KEY", "DB_PASSWORD", "GOOGLE_APPLICATION_CREDENTIALS",
            "filename:.env", "filename:id_rsa", "openai_api_key", "huggingface_token"
        ]

DORKS = load_dorks()

# URLs de los motores de búsqueda con consultas dinámicas
SEARCH_ENGINES = {
    "Google": "https://www.google.com/search?q=site:{}+{}",
    "Bing": "https://www.bing.com/search?q=site:{}+{}",
    "DuckDuckGo": "https://duckduckgo.com/html?q=site:{}+{}",
    "Yahoo": "https://search.yahoo.com/search?p=site:{}+{}",
    "Baidu": "https://www.baidu.com/s?wd=site:{}+{}"
}

def switch_tor_ip():
    """Solicita una nueva IP en la red Tor"""
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="torpassword")
        controller.signal(Signal.NEWNYM)

async def fetch(session, url, use_tor=False):
    """Realiza solicitudes asíncronas a los motores de búsqueda"""
    try:
        proxy = "socks5h://127.0.0.1:9050" if use_tor else None
        async with session.get(url, headers=HEADERS, timeout=10, proxy=proxy) as response:
            return await response.text()
    except Exception as e:
        return f"Error al acceder a {url}: {e}"

async def search_dork(target, dork, use_tor=False):
    """Ejecuta la búsqueda del dork en todos los motores de búsqueda"""
    async with aiohttp.ClientSession() as session:
        tasks = []
        for engine, base_url in SEARCH_ENGINES.items():
            url = base_url.format(target, dork)
            tasks.append(fetch(session, url, use_tor))
        results = await asyncio.gather(*tasks)
        return {engine: result for engine, result in zip(SEARCH_ENGINES.keys(), results)}

def search_with_serpapi(target, dork):
    """Realiza búsqueda con SerpAPI para evitar bloqueos"""
    url = "https://serpapi.com/search"
    params = {
        "q": f"site:{target} {dork}",
        "engine": "google",
        "api_key": SERPAPI_KEY
    }
    try:
        response = requests.get(url, params=params, headers=HEADERS)
        return response.json().get("organic_results", [])
    except Exception as e:
        return f"Error en SerpAPI: {e}"

def extract_sensitive_data(html_content):
    """Busca credenciales expuestas en el contenido HTML"""
    patterns = {
        "AWS_SECRET_ACCESS_KEY": r"(?i)aws_secret_access_key\s*=\s*['\"]?([A-Za-z0-9/+]{40})['\"]?",
        "OPENAI_API_KEY": r"sk-[A-Za-z0-9]{48}",
        "HUGGINGFACE_TOKEN": r"hf_[A-Za-z0-9]{40}"
    }
    matches = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, html_content)
        if match:
            matches[key] = match.group(1)
    return matches

def classify_result_with_gpt(text):
    """Clasifica los hallazgos con GPT-4 para determinar si son sensibles"""
    openai.api_key = OPENAI_API_KEY
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "Clasifica este contenido como sensible o no: " + text}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error en clasificación con GPT: {e}"

async def main(target, use_tor=False, use_serpapi=False):
    """Ejecuta la búsqueda de dorks, analiza los resultados y los clasifica"""
    print(f"\n🔍 Iniciando búsqueda en: {target} 🔍\n")
    for dork in DORKS:
        print(f"🔎 Buscando: {dork} en {target}...\n")
        
        # Buscar con SerpAPI si está habilitado
        if use_serpapi:
            serpapi_results = search_with_serpapi(target, dork)
            print(f"📌 [SerpAPI] {len(serpapi_results)} resultados encontrados.")
        
        # Buscar en motores de búsqueda tradicionales
        results = await search_dork(target, dork, use_tor)
        for engine, html_content in results.items():
            print(f"🌐 [{engine}] Analizando resultados...")
            extracted_data = extract_sensitive_data(html_content)
            if extracted_data:
                for key, value in extracted_data.items():
                    classification = classify_result_with_gpt(value)
                    print(f"🚨 Posible {key} encontrado: {value}")
                    print(f"📌 Clasificación: {classification}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dorking avanzado en motores de búsqueda")
    parser.add_argument("--target", required=True, help="Dominio o plataforma a analizar")
    parser.add_argument("--tor", action="store_true", help="Usar Tor para anonimizar búsquedas")
    parser.add_argument("--serpapi", action="store_true", help="Usar SerpAPI para evitar bloqueos")
    args = parser.parse_args()
    
    asyncio.run(main(args.target, args.tor, args.serpapi))


# Creado por la |Division81| - Grupo Oruss