<<<<<<< HEAD
<<<<<<< HEAD
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
=======
This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
>>>>>>> dev-Frontend
=======
# Guard.IA

Sistema de monitoramento legislativo voltado à proteção de crianças e adolescentes no ambiente digital.

---

## Sobre o projeto

O Guard.IA é um projeto desenvolvido na disciplina de **Métodos de Desenvolvimento de Software (MDS)** da Universidade de Brasília (UnB).

O objetivo do sistema é acompanhar proposições legislativas relacionadas à proteção de crianças e adolescentes na internet, permitindo a coleta, filtragem, classificação, armazenamento e visualização de dados legislativos de forma organizada e acessível.

O projeto busca apoiar análises sobre segurança digital, legislação e políticas públicas relacionadas ao ambiente virtual.

---

## Funcionalidades

- Coleta de proposições legislativas
- Filtragem por palavras-chave
- Classificação por temas
- Armazenamento dos dados
- Dashboard de visualização
- Métricas de produtividade da equipe
- Publicação automática via GitHub Pages

---

## Tecnologias utilizadas

### Front-end
- HTML5
- CSS3
- JavaScript

### Dashboard
- Streamlit
- Pandas
- Plotly

### Back-end e scripts
- Python 3.11+

### Controle de versão
- Git
- GitHub

### Integração contínua
- GitHub Actions

---

## Estrutura do projeto

```text
2026-1-Guard.IA
├── .github/workflows/
├── dashboard/
├── docs/
├── filtro/
├── grupo5-guard.ia/
├── LICENSE
└── README.md
>>>>>>> 10acd005c09734d2d32f040b3dce7f900b3fa932
