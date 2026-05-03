import requests
url = "https://dadosabertos.camara.leg.br/api/v2/proposicoes"
headers = {"Accept": "application/json"}
proposicoes = []
pagina = 1
while True:
    params = {
        "dataInicio": "2023-01-01",
        "ordem": "ASC",
        "ordenarPor": "id",
        "pagina": pagina, 
        "itens": 100,
        
        
        }
    response = requests.get(url, headers=headers, params=params)
    dados = response.json()

    if not dados["dados"]:
        break

    for prop in dados["dados"]:
        proposicao = {
        "id_externo": f"CAMARA-{prop['id']}",
        "ementa": prop["ementa"],
        "autor" : "A pesquisar",
        "partido": "A pesquisar",
        "estado": "A pesquisar",
        "casa": "Câmara",
        "dataApresentacao": prop["dataApresentacao"]
                    }
        proposicoes.append(proposicao)
    print(f"Página {pagina} coletada...")
    pagina += 1
    if pagina >= 3:
        break


for p in proposicoes:
    print(p["id_externo"], p["ementa"], p["autor"], p["partido"], p["estado"], p["casa"],  p["dataApresentacao"])