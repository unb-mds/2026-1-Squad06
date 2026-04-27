# 📅 Sprint Planning – Sprint 04

## 📆 Data
26/04/2026

## 👥 Participantes
- Clara
- Lucas
- João Paulo
- Otávio
- Gabriella
- Edvaldo

---

## 🎯 Objetivo da Sprint

Avançar na consolidação da base do sistema, refinando as implementações iniciais de cada etapa do pipeline e garantindo que todas as áreas estejam preparadas para integração futura.

O foco desta sprint não é integrar totalmente o sistema ainda, mas garantir que cada módulo esteja mais robusto, consistente e alinhado ao formato de dados definido pelo grupo.

---

## 🧠 Contexto da Sprint

Na sprint anterior, o grupo iniciou o desenvolvimento técnico com:

- implementação inicial da coleta;
- criação do filtro por palavras-chave;
- estruturação da classificação;
- configuração do banco de dados;
- criação do dashboard com dados simulados.

Agora, o objetivo é melhorar essas implementações e preparar o sistema para integração.

---

## 🔄 Fluxo do sistema

```text
Coleta → Filtro → Classificação → Armazenamento → Visualização 


# 📋 Tarefas definidas por área
## 🟦 Coleta
Responsáveis: Lucas e João Paulo 
**Atividades**
- [ ] Revisar o script de coleta implementado;
[ ] Garantir consumo correto das APIs;
[ ] Melhorar estrutura dos dados retornados;
[ ] Padronizar nomes dos campos;
[ ] Garantir que todos os registros tenham os campos mínimos necessários;
[ ] Atualizar o arquivo dados_brutos.json.
**Entrega esperada**
[ ] Script de coleta funcionando de forma mais estável;
[ ] Arquivo JSON consistente e padronizado.

## 🟩 Filtro
Responsável: João Paulo
**Atividades**
[ ] Refinar lista de palavras-chave;
[ ] Melhorar lógica de filtragem;
[ ] Garantir normalização correta dos textos;
[ ] Evitar perda de dados relevantes;
[ ] Gerar versão atualizada de dados_filtrados.json.
**Entrega esperada**
[ ] Filtro mais preciso;
[ ] Redução de dados irrelevantes.

## 🟪 Classificação
Responsáveis: Gabriella e Otávio
**Atividades**
[ ] Validar categorias definidas;
[ ] Ajustar lógica de classificação;
[ ] Implementar versão inicial mais consistente (mesmo que ainda simples);
[ ] Adicionar campo de confiança (confianca);
[ ] Gerar dados_classificados.json.
**Entrega esperada**
[ ] Dados classificados com maior coerência;
[ ] Estrutura pronta para futura integração com IA.

## 🟧 Armazenamento
Responsável: Edvaldo
**Atividades**
[ ] Revisar estrutura da tabela proposicoes;
[ ] Garantir compatibilidade com os dados classificados;
[ ] Testar inserção de dados no banco;
[ ] Validar conexão com PostgreSQL;
[ ] Ajustar tipos de dados se necessário.
**Entrega esperada**
[ ] Banco estruturado corretamente;
[ ] Inserção de dados funcionando.

## 🟥 Visualização
Responsável: Clara
**Atividades**
[ ] Revisar dashboard inicial;
[ ] Melhorar layout (organização visual);
[ ] Ajustar gráficos existentes;
[ ] Garantir funcionamento com dados simulados;
[ ] Preparar função futura para leitura do banco;
[ ] Organizar código (separar funções, limpeza).
**Entrega esperada**
[ ] Dashboard mais organizado e funcional;
[ ] Interface pronta para integração com dados reais.

# 🔗 Contrato de dados
Todas as etapas devem respeitar o seguinte formato mínimo:
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

# ⚠️ Dependências
Cada módulo ainda pode trabalhar com dados simulados;
Não é obrigatório integração completa nesta sprint;
Prioridade é garantir consistência entre os módulos.

# 🧪 Estratégia de desenvolvimento
Trabalhar com arquivos JSON intermediários;
Testar cada módulo separadamente;
Ajustar inconsistências de dados;
Realizar commits frequentes;
Documentar evolução das etapas.

# 📊 Evolução esperada
Antes:
Módulos iniciais funcionando separadamente
Depois:
Módulos mais robustos e prontos para integração

# ✅ Definition of Done
A sprint será considerada concluída se:
[ ] a coleta estiver estável;
[ ] o filtro estiver mais preciso;
[ ] a classificação estiver estruturada;
[ ] o banco estiver funcionando;
[ ] o dashboard estiver melhor organizado;
[ ] o formato de dados estiver padronizado;
[ ] as issues estiverem atualizadas.

# 🚀 Próxima Sprint
Na próxima sprint, o foco será:
integração do pipeline completo;
substituição de dados simulados por dados reais;
conexão do dashboard com o banco;
testes do sistema de ponta a ponta.

#💬 Observações
Esta sprint tem papel fundamental na organização do projeto, garantindo que todas as partes estejam consistentes antes da integração completa do sistema.
