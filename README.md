# 🔍 Letirotau-IA-Hunter: Exploración de Info Sensible relacionada con IA.

A menudo realizando Pentesting, detectamos joyas de la corona en las primeras fases de los procesos usando OSINT, un significativo número de oportunidades aumentan, cuando por olvido o descuido de algún equipo, la información queda expuesta a los atacantes.  Ahora, la búsqueda se amplía para abarcar los potenciales trozos de información expuestos como resultado del desarrollo de IAs, chatbots o sistemas de mensajería automatizados.

Este script automatiza **búsquedas avanzadas** en **Google, Bing, DuckDuckGo, Yahoo y Baidu** para detectar información sensible expuesta en un dominio o plataforma. Utiliza **Dorks de seguridad** para encontrar credenciales, API Keys, configuraciones de IA, desarrollo de modelos, entrenamiento de LLMs, claves de APIs de OpenAI, Hugging Face, y configuraciones de despliegue de modelos.


## 🚀 Características

✅ **Soporte para más de 40 Dorks específicos RELACIONADOS CON IA** (API Keys, Configs, Credenciales, etc.) 

✅ **Carga dorks personalizados desde un archivo externo** (dorks.txt). 

✅ **Búsqueda automatizada motores de búsqueda** para obtener mejores resultados.  (adiciona los que quieras)

✅ **Soporte para Tor y Proxychains para anonimizar búsquedas.**

✅ **Integración con SerpAPI para evitar bloqueos y afiando resultados.**

✅ **Análisis de contenido HTML para detectar credenciales filtradas.**

✅ **Clasificación de hallazgos con GPT-4 para evaluar la criticidad de la información expuesta.**

✅ **Optimizado para pentesters y OSINT**, proporcionando información útil de inmediato.  

✅ **Ejecución rápida y sencilla**

--

## 📌 Instalación

Clona el repositorio y entra en la carpeta:

```bash
git clone https://github.com/tuusuario/GitDorker-IA.git
cd GitDorker-IA

Instalar dependencias necesarias: pip install -r requirements.txt

**Usando Tor, instálalo con**
sudo apt install tor  # En Linux
brew install tor  # En macOS
choco install tor  # En Windows (con Chocolatey)

🔹Load and shoot
python letirotau.py --target yourhouse.com

🔹 Ejecutar con Tor
proxychains python letirotau.py --target yourhouse.com --tor

🔹 Ejecutar con SerpAPI (para evitar bloqueos):
python letirotau.py --target yourhouse.com --serpapi

🔹 Mixed Drinks:
proxychains python script.py --target yourhouse.com --tor --serpapi


🛡️ Advertencia Legal

Este script está destinado exclusivamente para fines educativos y auditorías de seguridad con autorización.
No debe utilizarse para actividades ilegales o sin el consentimiento del propietario del dominio.

--
#👨‍💻Creado por la Division81 del Grupo Oruss💡
--
