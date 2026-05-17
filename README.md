# 🛡️ Guard.IA - Monitoramento Legislativo Inteligente

O **Guard.IA** é uma plataforma de inteligência de dados projetada para monitorar, filtrar e classificar proposições legislativas da Câmara dos Deputados e do Senado Federal que impactam a proteção da infância e adolescência no ambiente digital.

Este projeto é desenvolvido na disciplina de **Métodos de Desenvolvimento de Software (MDS)** da Universidade de Brasília (UnB).

---

## 🏗️ Arquitetura do Sistema

O sistema segue o padrão **Pipes and Filters**, garantindo que cada etapa do processamento seja independente e escalável:

1.  **Coleta:** Scripts que consomem APIs abertas da Câmara e do Senado.
2.  **Filtro:** Processamento de limpeza e seleção por palavras-chave relevantes.
3.  **Classificação (IA):** Categorização temática usando modelos de NLP (BERT).
4.  **Armazenamento:** Persistência dos dados em banco de dados **PostgreSQL**.
5.  **Visualização:** Dashboard interativo construído com **Streamlit**.

---

## 🚀 Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Banco de Dados:** PostgreSQL (via Docker)
* **Interface/BI:** Streamlit & Plotly
* **IA/NLP:** Hugging Face (BERT-base-portuguese)
* **Infraestrutura:** Docker & GitHub Actions

---

## 📂 Estrutura de Pastas

```text
/
├── back/           # Lógica do Pipeline (Coleta, Filtro, Classificação, Banco)
├── front/          # Interface do Usuário (Dashboard)
├── data/           # Arquivos de intercâmbio (JSON) e Checkpoints
├── docs/           # Documentação do projeto e ADRs
└── GEMINI.md       # Constituição e Regras Técnicas do Projeto
