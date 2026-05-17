import json
import os
from .database import execute_query

def carregar_dados_filtrados(caminho_arquivo: str):
    """Lê o arquivo JSON de dados filtrados."""
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: Arquivo {caminho_arquivo} não encontrado.")
        return []
    
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Erro ao ler JSON: {e}")
        return []

def proposicao_existe(id_externo: str) -> bool:
    """Verifica se uma proposição já existe no banco pelo id_externo."""
    query = "SELECT 1 FROM proposicoes WHERE id_externo = %s LIMIT 1;"
    result = execute_query(query, (id_externo,), fetch=True)
    return len(result) > 0

def salvar_proposicoes(proposicoes: list):
    """
    Salva uma lista de proposições no banco de dados.
    Implementa deduplicação obrigatória por id_externo.
    """
    total_inseridas = 0
    total_pulas = 0
    
    query = """
        INSERT INTO proposicoes (
            id_externo, ementa, autor, partido, estado, 
            casa, data_apresentacao, categoria, confianca
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    
    for p in proposicoes:
        id_ext = p.get('id_externo')
        
        # Deduplicação obrigatória
        if proposicao_existe(id_ext):
            total_pulas += 1
            continue
            
        params = (
            id_ext,
            p.get('ementa'),
            p.get('autor', 'A pesquisar'),
            p.get('partido', 'A pesquisar'),
            p.get('estado', 'A pesquisar'),
            p.get('casa'),
            p.get('data_apresentacao'),
            p.get('categoria'),
            p.get('confianca')
        )
        
        try:
            execute_query(query, params)
            total_inseridas += 1
        except Exception as e:
            print(f"Erro ao inserir proposição {id_ext}: {e}")
            
    print(f"Processamento concluído: {total_inseridas} inseridas, {total_pulas} duplicadas puladas.")
    return total_inseridas

def iniciar_armazenamento():
    """Função principal para rodar a etapa de armazenamento."""
    # Caminho definido no GEMINI.md
    caminho_json = os.path.join("grupo5-guard.ia-backend", "data", "dados_filtrados.json")
    
    print(f"Iniciando armazenamento a partir de: {caminho_json}")
    dados = carregar_dados_filtrados(caminho_json)
    
    if dados:
        salvar_proposicoes(dados)
    else:
        print("Nenhum dado para processar.")

if __name__ == "__main__":
    iniciar_armazenamento()
