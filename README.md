# 🛡️ Guard.IA - Monitoramento Legislativo Inteligente

O **Guard.IA** é uma plataforma de inteligência de dados projetada para monitorar, filtrar e classificar proposições legislativas da Câmara dos Deputados e do Senado Federal que impactam a proteção da infância e adolescência no ambiente digital.

Este projeto é desenvolvido na disciplina de Métodos de Desenvolvimento de Software (MDS) da Universidade de Brasília (UnB).

---

# 🏗️ Arquitetura do Sistema

O sistema segue o padrão **Pipes and Filters**, garantindo que cada etapa do processamento seja independente:

- **Coleta:** Scripts Python que consomem APIs da Câmara e Senado.
- **Filtro:** Processamento de limpeza e seleção por palavras-chave.
- **Classificação (IA):** Categorização temática usando modelos BERT (Release 2).
- **Armazenamento:** Persistência em banco de dados PostgreSQL via Docker.
- **Visualização:** Dashboard interativo construído com Streamlit.

---

# 📂 Estrutura de Pastas

```plaintext
/
├── back/           # Lógica do Pipeline (Coleta, Filtro, Classificação, Banco)
├── front/          # Interface do Usuário (Dashboard)
├── data/           # Arquivos de intercâmbio (JSON) e Checkpoints
├── docs/           # Documentação do projeto e ADRs
└── GEMINI.md       # "Constituição" e Regras Técnicas do Projeto
```

---

# 🚀 Como Executar

## 1. Preparação do Ambiente

```bash
# Clone o repositório
git clone https://github.com/unb-mds/2026-1-Guard.IA.git

# Entre na pasta do projeto
cd 2026-1-Guard.IA

# Configure o ambiente virtual (VENV)
python -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows
.\venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

---

## 2. Infraestrutura e Coleta

```bash
# Sobe o banco de dados PostgreSQL
docker-compose up -d

# Executa a carga histórica da Câmara
python back/coleta/coletor_camara.py

# Executa a carga histórica do Senado
python back/coleta/coletor_senado.py
```

---

# 🛠️ Guia de Sobrevivência no Git (Obrigatório)

Para evitar conflitos de merge e perda de código, siga este fluxo sempre que for trabalhar.

---

## 1. Verificações Iniciais

### ✅ Branch Correta

Nunca trabalhe na `main`.

Use sempre a branch:

```bash
dev-projeto
```

Confira sua branch atual:

```bash
git branch
```

O asterisco (`*`) deve estar em `dev-projeto`.

---

### ✅ Fetch (A Espiadinha)

Antes de começar, veja se alguém da equipe subiu alterações novas:

```bash
git fetch origin
git status
```

Se aparecer algo como:

```plaintext
Your branch is behind 'origin/dev-projeto'
```

você precisa fazer um `pull`.

---

# 🔄 Fluxo de Trabalho Seguro

## 1. PULL

Atualize seu código local:

```bash
git pull origin dev-projeto
```

---

## 2. TRABALHE

Implemente suas alterações normalmente.

---

## 3. ADD & COMMIT

Salve suas alterações localmente:

```bash
git add .

git commit -m "feat(modulo): descricao curta do que foi feito"
```

Exemplo:

```bash
git commit -m "feat(coleta): adiciona coletor da API do Senado"
```

---

## 4. PUSH

Envie suas alterações para o GitHub:

```bash
git push origin dev-projeto
```

---

# ⚠️ Dica Importante

Se o `push` falhar:

1. Faça um novo `pull`
2. Resolva os conflitos de merge
3. Faça commit das correções
4. Tente o `push` novamente

---

# 🧱 Tecnologias Utilizadas

- Python
- PostgreSQL
- Docker
- Streamlit
- Transformers / BERT
- APIs da Câmara dos Deputados
- APIs do Senado Federal

---

# 📌 Objetivo do Projeto

O Guard.IA busca automatizar o monitoramento legislativo relacionado à segurança digital de crianças e adolescentes, permitindo:

- acompanhamento automatizado de projetos de lei;
- filtragem inteligente de conteúdo;
- categorização temática via IA;
- visualização simplificada dos dados legislativos;
- apoio a pesquisas e iniciativas de proteção digital.

---

# ⚖️ Licença

Este projeto está sob a licença **MIT**.

---

# 👥 Equipe

**Equipe Guard.IA — UnB Gama — 2026**
