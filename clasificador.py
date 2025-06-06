from transformers import pipeline

classificador = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def clasificar_mensajes(textos):
    etiquetas = ["Urgente", "Moderado", "Normal"]
    resultados = []

    # Si es string, lo convertimos en lista
    if isinstance(textos, str):
        textos = [textos]

    for texto in textos:
        resultado = classificador(texto, etiquetas)
        resultados.append({
            "mensaje": texto,
            "clasificacion": resultado["labels"][0],
            "confianza": resultado["scores"][0]
        })

    return resultados
