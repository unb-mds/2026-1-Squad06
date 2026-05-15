
import json
import unicodedata


PALAVRAS_CHAVE = [
    "crianca",
    "adolescente",
    "menor",
    "internet",
    "digital",
    "online",
    "cyberbullying",
    "redes sociais",
    "lgpd",
    "marco civil",
    "privacidade",
    "aplicativo",
    "eca",
    "conteudo inapropriado",
    "tempo de tela",
]


def normalizar(texto: str) -> str:
   
    #Converte o texto para minúsculas e remove acentos.

    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return texto


def contem_palavra_chave(ementa: str) -> bool:
   
    #Verifica se a ementa contém alguma das palavras-chave.
    #Retorna True se encontrar ao menos uma, False caso contrário.
    
    ementa_normalizada = normalizar(ementa)
    for palavra in PALAVRAS_CHAVE:
        if normalizar(palavra) in ementa_normalizada:
            return True
    return False


def filtrar(proposicoes: list[dict]) -> list[dict]:
    
    #Recebe a lista de proposições brutas e retorna
    #apenas as que contêm palavras-chave relevantes.
    
    return [p for p in proposicoes if contem_palavra_chave(p.get("ementa", ""))]