import streamlit as st
import requests

st.set_page_config(page_title="Clasificador de Mensajes", layout="centered")
st.title("Clasificador de Mensajes")
st.write("Clasifica múltiples frases en: Urgente, Moderado o Normal")

texto_entrada = st.text_area("Escribe tus mensajes (uno por línea):", height=200)

if st.button("Clasificar"):
    frases = [line.strip() for line in texto_entrada.splitlines() if line.strip() != ""]
    
    if not frases:
        st.warning("Por favor, escribe al menos una frase.")
    else:
        try:
            response = requests.post("http://localhost:8000/clasificar", json={"frases": frases})
            if response.status_code == 200:
                resultados = response.json()
                for i, resultado in enumerate(resultados):
                    st.markdown(f"### Mensaje {i+1}")
                    st.markdown(f"**Texto:** {resultado['mensaje']}")
                    st.success(f"Clasificación: {resultado['clasificacion']}  \nConfianza: {resultado['confianza']:.2%}")
            else:
                st.error(f"Error {response.status_code}: No se pudo clasificar las frases.")
        except Exception as e:
            st.error(f"No se pudo conectar al servidor FastAPI.\n\n{e}")
