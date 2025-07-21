
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Toolkit SEO con IA", layout="wide")
st.title("🛠️ Toolkit SEO con Inteligencia Artificial")

# Entrada de API Key
api_key = st.text_input("🔑 Ingresa tu API Key de OpenAI", type="password")

# Validación
if not api_key:
    st.warning("Ingresa tu API Key para usar las herramientas.")
    st.stop()

client = OpenAI(api_key=api_key)

# Menú de herramientas
tool = st.sidebar.selectbox("Selecciona una herramienta SEO", [
    "1️⃣ Generador de artículos SEO",
    "2️⃣ Generador de meta descripciones",
    "3️⃣ Analizador SEO de contenido",
    "4️⃣ Extractor de palabras clave",
    "5️⃣ Generador de imágenes con IA"
])

# Herramienta 1: Generador de artículos
if tool == "1️⃣ Generador de artículos SEO":
    st.subheader("📝 Generador de artículos")
    keyword = st.text_input("Palabra clave")
    if st.button("Generar artículo"):
        with st.spinner("Generando..."):
            try:
                respuesta = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Eres un redactor SEO profesional."},
                        {"role": "user", "content": f"Escribe un artículo optimizado para SEO sobre '{keyword}' con introducción, subtítulos y conclusión."}
                    ],
                    temperature=0.7,
                    max_tokens=1000
                )
                contenido = respuesta.choices[0].message.content
                st.text_area("Artículo generado", value=contenido, height=400)
            except Exception as e:
                st.error(f"❌ Error: {e}")

# Herramienta 2: Meta descripción
elif tool == "2️⃣ Generador de meta descripciones":
    st.subheader("🧩 Meta descripción SEO")
    tema = st.text_input("Tema del sitio o artículo")
    if st.button("Generar descripción"):
        with st.spinner("Generando..."):
            try:
                respuesta = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Eres un experto en SEO y marketing digital."},
                        {"role": "user", "content": f"Escribe una meta descripción atractiva y optimizada para SEO sobre: {tema}"}
                    ],
                    temperature=0.7,
                    max_tokens=150
                )
                contenido = respuesta.choices[0].message.content
                st.text_area("Meta descripción generada", value=contenido, height=100)
            except Exception as e:
                st.error(f"❌ Error: {e}")

# Herramienta 3: Analizador SEO
elif tool == "3️⃣ Analizador SEO de contenido":
    st.subheader("🔍 Analizador SEO de texto")
    texto = st.text_area("Pega el contenido que quieres analizar")
    if st.button("Analizar"):
        with st.spinner("Analizando..."):
            try:
                respuesta = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Eres un auditor SEO profesional."},
                        {"role": "user", "content": f"Analiza este texto desde el punto de vista SEO y ofrece sugerencias: {texto}"}
                    ],
                    temperature=0.6,
                    max_tokens=500
                )
                contenido = respuesta.choices[0].message.content
                st.text_area("Informe SEO", value=contenido, height=300)
            except Exception as e:
                st.error(f"❌ Error: {e}")

# Herramienta 4: Extractor de palabras clave
elif tool == "4️⃣ Extractor de palabras clave":
    st.subheader("🔑 Palabras clave principales")
    texto = st.text_area("Introduce un texto para extraer keywords")
    if st.button("Extraer keywords"):
        with st.spinner("Extrayendo..."):
            try:
                respuesta = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Eres un experto en análisis semántico SEO."},
                        {"role": "user", "content": f"Extrae las palabras clave principales de este texto y clasifícalas por importancia: {texto}"}
                    ],
                    temperature=0.5,
                    max_tokens=300
                )
                contenido = respuesta.choices[0].message.content
                st.text_area("Palabras clave extraídas", value=contenido, height=200)
            except Exception as e:
                st.error(f"❌ Error: {e}")

# Herramienta 5: Generador de imágenes con DALL·E
elif tool == "5️⃣ Generador de imágenes con IA":
    st.subheader("🎨 Generador de imágenes con IA (DALL·E)")
    prompt = st.text_input("Describe la imagen que quieres generar")
    if st.button("Generar imagen"):
        with st.spinner("Generando imagen..."):
            try:
                image = client.images.generate(
                    model="dall-e-3",
                    prompt=prompt,
                    n=1,
                    size="1024x1024"
                )
                url = image.data[0].url
                st.image(url, caption="Imagen generada con DALL·E")
            except Exception as e:
                st.error(f"❌ Error: {e}")
