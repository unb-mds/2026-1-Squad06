# Issue relacionada
Issue #15

# Descrição
Este documento apresenta o levantamento de requisitos do sistema de monitoramento legislativo.

# Objetivo
Definir os requisitos funcionais e não funcionais do sistema.

# 1. Visão geral do sistema

O sistema tem como finalidade monitorar automaticamente projetos de lei e outras proposições legislativas relacionadas à proteção de crianças e adolescentes na internet, identificando temas como cyberbullying, privacidade de dados, tempo de tela, conteúdo inapropriado e educação digital. Para isso, o sistema deve coletar dados públicos da Câmara dos Deputados e do Senado Federal, filtrar proposições relevantes, classificá-las por tema, armazená-las em banco de dados e disponibilizá-las em um portal visual acessível ao usuário.

# 2. Stakeholders

Os principais interessados no sistema são:

cidadãos que desejam acompanhar proposições legislativas sobre infância e ambiente digital;
pesquisadores e estudantes que queiram analisar tendências legislativas;
equipe de desenvolvimento do projeto;
docentes e avaliadores da disciplina;
usuários finais que consumirão o dashboard.

# 3. Requisitos funcionais
## RF01 — Coleta de proposições

O sistema deve coletar automaticamente dados de proposições legislativas das APIs públicas da Câmara dos Deputados e do Senado Federal. A documentação do projeto já prevê essas duas fontes como base da etapa de coleta.

## RF02 — Coleta periódica

O sistema deve permitir uma carga inicial histórica e depois realizar coletas periódicas de novas proposições. O planejamento técnico prevê uma primeira execução com dados desde 2023 e execuções seguintes diárias.

## RF03 — Armazenamento temporário dos dados brutos

Na primeira release, o sistema deve salvar os dados coletados em arquivo JSON intermediário, no formato dados_brutos.json.

## RF04 — Filtragem por palavras-chave

O sistema deve filtrar as proposições coletadas com base em palavras-chave relacionadas ao tema do projeto, descartando os registros não relevantes. O planejamento define essa etapa como uma redução de volume antes da classificação por IA.

## RF05 — Normalização de texto

O sistema deve converter textos para minúsculas e remover acentos antes da comparação com palavras-chave, para evitar perda de resultados por variação textual.

## RF06 — Geração de arquivo filtrado

O sistema deve gerar um arquivo dados_filtrados.json contendo apenas as proposições consideradas relevantes.

## RF07 — Classificação temática

O sistema deve classificar as proposições filtradas em categorias temáticas relacionadas ao problema do projeto. As categorias já previstas incluem cyberbullying e assédio online, privacidade e proteção de dados, tempo de tela e dependência digital, conteúdo inapropriado e educação digital.

## RF08 — Pontuação de confiança

O sistema deve atribuir uma pontuação de confiança à categoria atribuída pela classificação.

## RF09 — Geração de arquivo classificado

O sistema deve produzir um arquivo dados_classificados.json com os dados já enriquecidos pelos campos de categoria e confiança.

## RF10 — Persistência em banco de dados

O sistema deve armazenar os dados processados em banco PostgreSQL, mantendo os registros prontos para consulta pelo dashboard.

## RF11 — Estrutura mínima de dados

O sistema deve persistir, no mínimo, os seguintes atributos de cada proposição: id_externo, ementa, autor, partido, estado, casa, data_apresentacao, categoria, confianca e coletado_em.

## RF12 — Dashboard interativo

O sistema deve disponibilizar um portal web interativo para consulta dos dados processados. Essa é a função principal da etapa de visualização.

## RF13 — Visualização por categoria

O dashboard deve mostrar a quantidade de proposições por tema/categoria em gráfico de barras.

## RF14 — Evolução temporal

O dashboard deve mostrar a evolução das proposições ao longo do tempo em gráfico de linha.

## RF15 — Ranking de parlamentares

O dashboard deve exibir os parlamentares mais ativos em ranking ou tabela.

## RF16 — Distribuição por partido

O dashboard deve mostrar a distribuição das proposições por partido, por exemplo em gráfico de pizza.

## RF17 — Distribuição por estado/região

O dashboard deve apresentar a distribuição das proposições por estado ou região, com possibilidade de uso de mapa do Brasil.

## RF18 — Exploração intuitiva dos dados

O usuário deve conseguir explorar os dados de forma visual e intuitiva por meio do dashboard.

# 4. Requisitos não funcionais
## RNF01 — Arquitetura modular

O sistema deve ser implementado em arquitetura Pipes and Filters, permitindo que cada etapa do pipeline funcione de forma independente.

## RNF02 — Facilidade de manutenção

Cada etapa deve poder ser modificada ou substituída sem quebrar as demais etapas do sistema.

## RNF03 — Testabilidade

O sistema deve facilitar testes independentes para cada etapa do pipeline.

## RNF04 — Uso de tecnologias definidas

O sistema deve utilizar Python 3.10+ nas etapas de coleta, filtro e classificação; PostgreSQL no banco de dados; Streamlit e Plotly no dashboard; e Docker/GitHub Actions na infraestrutura planejada.

## RNF05 — Acessibilidade de execução

O dashboard deve ser executável localmente por comando simples, conforme previsto com streamlit run dashboard.py.

## RNF06 — Eficiência de processamento

O sistema deve reduzir o volume de dados antes da etapa de IA, para evitar custo computacional desnecessário. O filtro existe justamente para isso.

## RNF07 — Compatibilidade com hardware limitado

A etapa de classificação deve prever alternativa de modelo mais leve para ambientes com pouca memória RAM.

## RNF08 — Evolução incremental

A solução não deve assumir que os arquivos JSON intermediários serão permanentes, pois a documentação já define que eles são solução de Release 1 e que depois a comunicação entre etapas deve migrar para o banco PostgreSQL.

# 5. Regras de negócio
## RN01

Uma proposição só segue para a etapa de classificação se passar pelo filtro de relevância por palavras-chave.

## RN02

A etapa de coleta não deve aplicar filtro, classificação ou análise; ela deve apenas buscar e salvar os dados brutos.

## RN03

A classificação deve atribuir apenas uma categoria principal e uma pontuação de confiança para cada proposição, na forma inicialmente proposta.

## RN04

O dashboard deve consumir dados já processados e persistidos, não devendo repetir do zero as etapas de coleta, filtro e classificação a cada acesso do usuário.

# 6. Requisitos de dados

O sistema deve trabalhar com dados legislativos contendo, no mínimo:

identificador externo da proposição;
ementa ou descrição textual;
autor;
partido;
estado;
casa legislativa;
data de apresentação;
categoria;
confiança da classificação;
data de coleta no sistema.

# 7. Restrições do projeto
As fontes de dados devem ser as APIs públicas da Câmara e do Senado.
A primeira release deve priorizar coleta, filtro e armazenamento, deixando classificação e dashboard completo para evolução posterior.
A visualização deve, preferencialmente, ser feita com Streamlit, evitando complexidade desnecessária de frontend tradicional.
O banco definido para o projeto é PostgreSQL.

# 8. Histórias de usuário
## HU01

Como cidadão, eu quero visualizar proposições por tema para entender quais assuntos estão sendo mais discutidos no Legislativo.

## HU02

Como pesquisador, eu quero acompanhar a evolução das proposições ao longo do tempo para identificar tendências legislativas.

## HU03

Como usuário, eu quero ver quais parlamentares mais apresentam proposições relacionadas ao tema para compreender os atores mais atuantes.

## HU04

Como analista, eu quero consultar a distribuição por partido e estado para comparar o comportamento legislativo entre grupos políticos e regiões.

## HU05

Como equipe do projeto, eu quero que os dados sejam coletados e processados automaticamente para evitar busca manual em sites governamentais.

# 9. Priorização inicial
**Alta prioridade**
Coleta das proposições
Filtro por palavras-chave
Estrutura do banco
Persistência em PostgreSQL
**Média prioridade**
Classificação por IA/NLP
Dashboard com gráficos principais
**Baixa prioridade**
Identificação de novos temas
Melhorias visuais e refinamentos avançados do portal

Essa priorização está alinhada com o planejamento técnico, que coloca coleta, filtro e armazenamento como prioridades da Release 1, e classificação/visualização completa como evolução seguinte.
