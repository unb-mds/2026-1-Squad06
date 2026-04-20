# 📅 Sprint Planning – Sprint 02


## 📆 Data
18/04/2026


## 👥 Participantes
- Clara  
- Otávio  
- João Paulo  
- Gabriella  
- Lucas  
- Edvaldo  


---


## 🎯 Objetivo da Sprint


Iniciar o desenvolvimento técnico do sistema com base na arquitetura definida (Pipes and Filters), implementando as primeiras versões de cada etapa do pipeline e permitindo que todas as áreas avancem de forma paralela.


---


## 🧠 Estrutura do Projeto


O sistema segue o fluxo:


Coleta → Filtro → Classificação → Armazenamento → Visualização


Cada etapa é independente, permitindo desenvolvimento simultâneo entre os integrantes.


---


## 📋 Tarefas definidas por área


### 🟦 Coleta (Responsável: Lucas e João Paulo)
- [ ] Implementar script para consumir APIs da Câmara e Senado  
- [ ] Realizar requisições HTTP com requests  
- [ ] Coletar dados de proposições legislativas  
- [ ] Salvar saída em `dados_brutos.json`  


**Entrega esperada:**
- Arquivo JSON com dados reais  
- Script funcional de coleta  


---


### 🟩 Filtro (Responsável: João Paulo)
- [ ] Ler `dados_brutos.json`  
- [ ] Normalizar texto (minúsculas + remoção de acentos)  
- [ ] Definir lista de palavras-chave  
- [ ] Filtrar proposições relevantes  
- [ ] Salvar saída em `dados_filtrados.json`  


**Entrega esperada:**
- Redução significativa do volume de dados  
- Script funcional de filtragem  


---


### 🟪 Classificação (Responsável: Gabriella)
- [ ] Ler `dados_filtrados.json`  
- [ ] Definir categorias do projeto:
  - Cyberbullying  
  - Privacidade  
  - Tempo de tela  
  - Conteúdo inapropriado  
  - Educação digital  
- [ ] Implementar classificação inicial (pode ser simples)  
- [ ] Preparar integração futura com IA (NLP)  
- [ ] Salvar saída em `dados_classificados.json`  


**Entrega esperada:**
- Dados categorizados  
- Estrutura pronta para IA futura  


---


### 🟧 Armazenamento (Responsável: Edvaldo)
- [ ] Configurar banco PostgreSQL (Docker)  
- [ ] Criar tabela `proposicoes`  
- [ ] Definir estrutura de dados (id, ementa, autor, categoria, etc.)  
- [ ] Implementar conexão Python com banco (psycopg2)  
- [ ] Inserir dados classificados no banco  


**Entrega esperada:**
- Banco funcionando  
- Dados persistidos e organizados  


---


### 🟥 Visualização (Responsável: Clara)
- [ ] Criar dashboard inicial com Streamlit  
- [ ] Implementar layout básico (sidebar + conteúdo)  
- [ ] Utilizar dados simulados (mock) para desenvolvimento inicial  
- [ ] Criar gráficos iniciais:
  - Proposições por categoria  
  - Evolução ao longo do tempo  
  - Ranking de parlamentares  
- [ ] Preparar integração futura com banco de dados  


**Entrega esperada:**
- Dashboard funcional com dados fake  
- Interface inicial estruturada  


---


## 🔗 Dependências entre áreas


- Coleta → gera `dados_brutos.json`  
- Filtro → depende da Coleta  
- Classificação → depende do Filtro  
- Armazenamento → depende da Classificação  
- Visualização → depende do Armazenamento  


⚠️ Importante:
Apesar das dependências, todas as áreas podem iniciar o desenvolvimento utilizando dados simulados.


---


## 🧪 Estratégia de desenvolvimento


Para evitar bloqueios entre equipes:


- Utilizar arquivos JSON como contrato de dados  
- Definir formato padrão de dados entre etapas  
- Desenvolver componentes de forma independente  
- Usar dados mock para testes e prototipação  


---


## 📊 Formato padrão de dados (definido pelo grupo)


```json
{
  "id_externo": "",
  "ementa": "",
  "autor": "",
  "partido": "",
  "estado": "",
  "data_apresentacao": "",
  "categoria": "",
  "confianca": 0.0
}
