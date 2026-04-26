## Visão geral

Este arquivo define a estrutura do banco de dados PostgreSQL utilizado pelo sistema de monitoramento legislativo. Ele deve ser executado uma única vez para preparar o ambiente antes de qualquer inserção de dados.

---

## Pré-requisitos

- PostgreSQL 14+ instalado localmente **ou** Docker (recomendado)
- Acesso a um terminal com `psql` disponível

---

## Como executar

### 1. Crie o banco de dados

```bash
psql -U postgres -c "CREATE DATABASE monitoramento_legislativo;"
```

### 2. Execute o schema

```bash
psql -U postgres -d monitoramento_legislativo -f schema.sql
```

Se tudo correr bem, você verá:

```
DROP TABLE
CREATE TABLE
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
```

---

## Estrutura da tabela `proposicoes`

| Campo               | Tipo        | Descrição                                      |
|---------------------|-------------|------------------------------------------------|
| `id`                | SERIAL      | Identificador automático (chave primária)      |
| `id_externo`        | VARCHAR(50) | Identificador original — ex: `PL-1234/2024`   |
| `ementa`            | TEXT        | Texto descritivo da proposição                 |
| `autor`             | VARCHAR(255)| Nome do parlamentar autor                      |
| `partido`           | VARCHAR(50) | Partido político do autor                      |
| `estado`            | VARCHAR(2)  | Sigla do estado do autor — ex: `SP`, `MG`     |
| `casa`              | VARCHAR(20) | `Câmara` ou `Senado`                           |
| `data_apresentacao` | DATE        | Data de protocolo da proposição                |
| `categoria`         | VARCHAR(100)| Tema identificado pela IA — ex: `cyberbullying`|
| `confianca`         | FLOAT       | Pontuação de confiança da classificação (0–1)  |
| `coletado_em`       | TIMESTAMP   | Preenchido automaticamente na inserção         |

---

## Restrições aplicadas

- `id_externo` é **único** — impede que a mesma proposição seja inserida duas vezes
- `casa` só aceita os valores `'Câmara'` ou `'Senado'`
- `confianca` deve estar entre `0` e `1`
- `coletado_em` é preenchido automaticamente com a data e hora da inserção

---

## Índices criados

Quatro índices foram criados para acelerar as consultas feitas pelo Dashboard:

| Índice            | Campo               | Motivo                                      |
|-------------------|---------------------|---------------------------------------------|
| `idx_categoria`   | `categoria`         | Filtrar proposições por tema                |
| `idx_casa`        | `casa`              | Filtrar por Câmara ou Senado                |
| `idx_data`        | `data_apresentacao` | Ordenar e filtrar por período               |
| `idx_confianca`   | `confianca`         | Filtrar por nível de confiança da IA        |

---

## Observações

- O comando `DROP TABLE IF EXISTS proposicoes` no início do script remove a tabela caso ela já exista. Isso é útil durante o desenvolvimento, mas **deve ser removido em produção** para não apagar dados reais.
- Na **Release 1**, os dados chegam via arquivo `.json` gerado pelo módulo de Classificação. A partir da **Release 2**, os módulos passarão a se comunicar diretamente pelo banco, sem arquivo intermediário.

