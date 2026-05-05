# 🛡️ Guard.IA - Monitoramento Legislativo Inteligente

O **Guard.IA** é uma plataforma de inteligência de dados projetada para monitorar, filtrar e classificar proposições legislativas (Câmara e Senado) que impactam a proteção da infância e adolescência.

## 🏗️ Arquitetura do Projeto
Este projeto utiliza a arquitetura **Pipes and Filters** para garantir a escalabilidade e a separação de responsabilidades no processamento dos dados:

1.  **Coleta (Iniciador):** Scripts em Python que buscam dados nas APIs do Governo.
2.  **Filtro:** Processamento inicial para limpeza de ruídos.
3.  **Classificação (IA):** Uso do modelo BERT para classificar projetos críticos.
4.  **Armazenamento:** Persistência em banco de dados PostgreSQL.
5.  **Visualização:** Dashboard interativo construído em **Streamlit**.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
* Python 3.10 ou superior
* Virtualenv (Recomendado)

### 1. Configuração do Ambiente
No terminal, na raiz do projeto:
```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente
# No Windows:
.\venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

# Instalar dependências
pip install -r grupo5-guard.ia/dashboard/requirements.txt