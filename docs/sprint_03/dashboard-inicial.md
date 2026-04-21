# 🔗 Issue relacionada
Issue #14

## 📖 Descrição
Este documento apresenta a implementação da primeira versão da visualização do sistema utilizando Streamlit e Plotly.

O objetivo é construir um dashboard funcional com dados simulados, permitindo o desenvolvimento independente das demais etapas do projeto, como coleta, filtragem e armazenamento de dados.

## 🎯 Objetivo
Criar um dashboard inicial que permita visualizar informações sobre proposições legislativas, utilizando dados simulados para validação da interface e das funcionalidades.

## 📚 Funcionalidades implementadas

Estrutura do dashboard
Layout com sidebar (menu e filtros) e área principal de visualização

Filtros
Filtro por categoria
Filtro por partido
Filtro por casa legislativa

Indicadores (cards)
Total de proposições
Total de categorias
Total de parlamentares

Visualizações
Gráfico de barras: proposições por categoria
Gráfico de linha: evolução ao longo do tempo
Tabela: ranking de parlamentares mais ativos
Gráfico de pizza: distribuição por partido

Tabela de dados
Exibição das proposições com base nos filtros aplicados

## 💻 Aplicação no Projeto
No projeto de monitoramento legislativo sobre proteção de crianças na internet, o dashboard permite:

Visualizar rapidamente o volume de proposições por categoria
Analisar tendências ao longo do tempo
Identificar parlamentares mais ativos
Explorar dados de forma interativa por meio de filtros

Essa visualização será integrada futuramente com dados reais provenientes da pipeline de coleta, filtragem e classificação.

## 🛠️ Tecnologias utilizadas
Python
Streamlit
Pandas
Plotly

## 🛠️ Tarefas práticas
Criação de dados simulados (data_fake.csv)
Implementação do dashboard em Streamlit
Estruturação da interface com sidebar e conteúdo principal
Criação dos gráficos e tabelas
Organização do código para futura integração com banco de dados

## ✅ Resultado esperado
Dashboard funcional com dados simulados
Interface inicial estruturada
Base pronta para integração com PostgreSQL

## 💡 Aprendizados
A implementação do dashboard permitiu compreender como estruturar uma interface de visualização de dados de forma simples e eficiente.

Além disso, foi possível validar a lógica de apresentação das informações antes da integração com dados reais, facilitando o desenvolvimento incremental do projeto.
