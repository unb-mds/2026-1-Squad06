API é a sigla para Application Programming Interface. Em termos simples, é um conjunto de regras e protocolos que permite que diferentes softwares se comuniquem entre si.
A API é como se fosse um intermediário que recebe solicitações, leva para o sistema que processa e traz a resposta de volta de forma organizada e padronizada.
Dentre as principais APIs pesquisaras no mercado temos:

### **SUPABASE**

Supabase é uma plataforma backend-as-a-service que vem ganhando enorme adoção na comunidade. É construído sobre PostgreSQL e oferece uma experiência completa para desenvolvedores .

Principais características:

 - Banco de dados PostgreSQL gerenciado com acesso SQL direto 
- API REST e GraphQL auto-geradas via PostgREST
- Subscriptions em tempo real (WebSockets)
- Autenticação e armazenamento de arquivos integrados
- Row Level Security (RLS) no nível do banco de dados

É uma plataforma indicada para devs com experiência em SQL e que desejam ter controle total sobre o banco de dados em tempo real.

### **Xano** 

O Xano evoluiu significativamente e se posiciona como uma plataforma completa que unifica API, banco de dados e lógica de negócio em um único ambiente.

Principais características:

- Banco de dados PostgreSQL gerenciado
- Geração instantânea de endpoints REST
- "Function Stack" para lógica personalizada (visual + código + IA)
- Suporte a MCP (Model Context Protocol) para agentes de IA
- RBAC, SOC 2, GDPR e HIPAA compliance

Entretanto tem uma curva de aprendizado alta para iniciantes e não é tão flexível quanto SQL.

### **Hasura**
O Hasura é conhecido por poder gerar um API do tipo GraphQL em qualquer banco de dados PostgreSQL.

**Principais características:**

- Introspecta o schema do banco e gera API GraphQL automaticamente
- Filtros, ordenação, paginação e agregações prontos
- Subscriptions em tempo real (WebSockets)

Uma boa opção para projetos que precisam de dashboards ao vivo entretanto não é muito recomendada para desenvolvedores que não possuem uma estrutura de banco de dados já existente.

### **Directus**
O directus se descreve como um data engine, ele usa qualquer banco de dados SQL e gera APIs REST e possui uma interface de administração.
**Principais características:** 

- Suporta PostgreSQL, MySQL, SQLite, OracleDB, SQL Server
- Trabalha sobre schema existente (sem migrações)
- Interface administrativa para não-técnicos

Uma boa opção para para desenvolvedores que precisam de uma API sobre banco de dados SQL ja existentes.

### **DreamFactory**
O DreamFactory é uma plataforma open-source que gera APIs REST automaticamente a partir de mais de 20 fontes de dados, dentre eles estão bancos SQL e NoSQL.

**Principais características:**

- Geração instantânea de APIs REST com Swagger/OpenAI
- Suporte a 20+ bancos de dados
- Conversão SOAP para REST
 
Uma alternativa para desenvolvedores que nao querem codificar manualmente suas APIs e que querem apresentar diversos bancos de dados rapidamente, entretanto tem um foco muito grande em REST.
---
*Documentação baseada na issue [#11](https://github.com/unb-mds/2026-1-Squad06/issues/11)*
