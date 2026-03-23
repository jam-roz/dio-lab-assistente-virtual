# 💰 FinGuide AI — Assistente Virtual de Saúde Financeira

> Projeto desenvolvido como parte do desafio prático da [DIO](https://www.dio.me/) — Construção de Agentes de IA com base de conhecimento estruturada - GenAI Dados Bradesco.

---

## 📌 Sobre o Projeto

O **FinGuide AI** é um assistente virtual conversacional especializado em **saúde financeira pessoal**. Seu objetivo é ajudar usuários a entenderem para onde vai o dinheiro, organizar gastos por categoria, identificar padrões prejudiciais e traçar planos concretos para sair de dívidas ou atingir metas financeiras.

Diferente de uma busca genérica na internet, o FinGuide cruza o perfil do usuário, seu histórico de atendimentos e suas transações reais para entregar orientações personalizadas — democratizando um tipo de acompanhamento que antes só era acessível por meio de consultores financeiros pagos.

---

## 🎯 Problema que o Agente Resolve

Mais de 70 milhões de brasileiros estão inadimplentes — e grande parte deles não tem controle sobre os próprios gastos. O problema raramente é **quanto** se ganha, mas **como** o dinheiro é gerido no dia a dia, sem consciência e sem acompanhamento.

O FinGuide resolve isso sendo um parceiro financeiro acessível, empático e disponível 24h: o usuário descreve sua situação, e o agente orienta com base em dados reais e boas práticas de finanças pessoais.

---

## 🧠 Persona do Agente

| Atributo | Descrição |
|---|---|
| **Nome** | FinGuide (Finn, no informal) |
| **Especialidade** | Saúde financeira pessoal |
| **Personalidade** | Empático, direto, educativo e sem julgamentos |
| **Tom** | Semiformal — próximo e humano, porém confiável |
| **Comportamento** | Consultivo-motivacional: faz perguntas, explica o raciocínio, celebra progressos |

---

## 🗂️ Estrutura do Projeto

```
finguide-ai/
│
├── assets
│
├── docs/
│   ├── 01-documentacao-agente.md         # Documentação completa do agente
│   ├── 02-base-conhecimento.md           # Todos os dados e inforações usadas pelo agente
│   ├── 03-prompt.md                      # Instruções do agente
│   ├── 04-metricas.md                    # Avaliação, métricas e critérios de teste        
│   └── 05-pitch.md                       # Conclusões finais e demonstração do projeto
│
├── data/
│   ├── historico_atendimentos.csv        # Histórico de conversas anteriores
│   ├── perfil_usuario.json               # Perfis comportamentais e financeiros
│   ├── dicas_financeiras.json            # Base de orientações por categoria e perfil
│   └── transacoes.csv                    # Transações financeiras dos usuários
│
└── src/
│    ├── app.py                            # Código do agente
│    ├── requirements.txt                  # Requerimentos do projeto
│
└── README.MD
```

---

## 📚 Base de Conhecimento

A inteligência do FinGuide é alimentada por quatro arquivos estruturados que, em conjunto, permitem respostas personalizadas e contextualizadas:

### `historico_atendimentos.csv`
Registra todas as interações anteriores entre o agente e os usuários. Contém tema da conversa, sentimento do usuário, resumo do atendimento, ação recomendada e status de conclusão.

**Utilização:** contextualizar o histórico do usuário e identificar evolução ao longo do tempo — por exemplo, perceber que uma dívida caiu de R$ 18.400 para R$ 12.600 em três meses e ajustar a orientação de acordo.

---

### `perfil_usuario.json`
Armazena o perfil completo de cada usuário: dados pessoais, situação financeira (renda, dívidas, score de crédito, reserva de emergência), perfil comportamental (tipo de perfil, disciplina, nível de conhecimento) e metas ativas.

**Utilização:** personalizar recomendações conforme o momento financeiro de cada pessoa. Um usuário `endividado_em_recuperacao` recebe orientações diferentes de um `organizador_em_evolucao`, mesmo que a pergunta seja idêntica.

**Tipos de perfil mapeados:**
- `gastador_involuntario` — gasta sem perceber, não sabe para onde vai o dinheiro
- `organizador_em_evolucao` — disciplinado, quer aprender a investir
- `endividado_em_recuperacao` — foco total em quitar dívidas
- `iniciante_consciente` — primeiro emprego, construindo base financeira
- `consolidado_com_pontos_cegos` — boa renda, mas com comportamentos prejudiciais

---

### `dicas_financeiras.json`
Base de conhecimento com orientações, estratégias e conceitos financeiros categorizados por tema e perfil-alvo. Inclui quando aplicar cada dica, exemplos práticos e tags para facilitar o cruzamento com o contexto do usuário.

**Categorias cobertas:**
- Controle de gastos (método 50-30-20, registro diário, auditoria de assinaturas)
- Dívidas (método Avalanche, método Bola de Neve, renegociação, cheque especial)
- Reserva de emergência (quanto guardar, onde guardar)
- Planejamento e metas (metas SMART, pague-se primeiro)
- Investimentos básicos (poupança vs. CDB vs. Tesouro Direto, PGBL vs. VGBL)

**Utilização:** selecionar a orientação mais adequada ao perfil e ao momento do usuário, evitando respostas genéricas.

---

### `transacoes.csv`
Registro detalhado de movimentações financeiras dos usuários: data, descrição, categoria, subcategoria, valor, tipo (débito/crédito), forma de pagamento e flag de essencialidade.

**Utilização:** analisar padrões de gastos, calcular totais por categoria e identificar comportamentos específicos — como percentual elevado de delivery, compras parceladas excessivas ou uso recorrente de cheque especial.

**Categorias de transação mapeadas:** moradia, alimentação, transporte, saúde, lazer, educação, vestuário, dívidas, poupança, investimentos e compras.

---

## 💬 Exemplos de Interação

### Interação típica — usuário sem controle financeiro

> **Usuário:** Ganho R$ 3.500 por mês mas sempre fico no zero a zero. Não sei pra onde vai meu dinheiro.
>
> **FinGuide:** Você não está sozinho nisso. O primeiro passo é simples: registre todos os gastos por 30 dias — sem julgamentos, só para enxergar. Só de registrar, a maioria das pessoas já reduz os gastos em cerca de 15% no primeiro mês...

### Interação com dado real da base

> **Usuário:** Quanto gastei com alimentação esse mês?
>
> **FinGuide:** Suas transações de novembro mostram R$ 674,00 em alimentação — sendo R$ 388,70 em supermercado e R$ 285,30 em delivery. O delivery representa 42% do total. Reduzir para R$ 120/mês liberaria cerca de R$ 165 no orçamento...

### Edge case — pergunta fora do escopo

> **Usuário:** Qual a previsão do tempo para o final de semana?
>
> **FinGuide:** Essa está fora da minha alçada! Sou especializado em saúde financeira. Para o clima, o Climatempo ou o Google te ajudam melhor. Mas já que o fim de semana se aproxima — que tal verificarmos seus gastos com lazer esse mês?

---

## ⚠️ Limitações Declaradas

O FinGuide foi projetado com fronteiras claras de responsabilidade:

- ❌ Não realiza diagnósticos financeiros formais nem substitui um CFP (planejador financeiro certificado)
- ❌ Não acessa contas bancárias, aplicativos ou dados financeiros reais
- ❌ Não recomenda investimentos específicos com base em perfil de risco
- ❌ Não realiza cálculos jurídicos de dívidas — orienta a buscar Procon ou advogado
- ❌ Não garante resultados — os resultados dependem do comportamento e disciplina do usuário
- ❌ Não armazena histórico entre sessões — cada conversa parte do contexto fornecido
- ❌ Não trata questões de saúde mental com profundidade clínica

---

## 🧪 Cenários de Teste e Avaliação

| # | Cenário | Comportamento Esperado |
|---|---|---|
| TC-01 | "Quanto gastei com alimentação?" | Retornar valor baseado em `transacoes.csv` com detalhamento por subcategoria |
| TC-02 | "Qual sugestão de gastos você recomenda pra mim?" | Recomendação personalizada cruzando perfil + histórico + transações |
| TC-03 | "Qual a previsão do tempo?" | Informar que o escopo é exclusivamente educação financeira |
| TC-04 | "Quanto são os gastos de XYZ?" (dado inexistente) | Admitir ausência da informação e orientar como fornecê-la |

Cada cenário é avaliado por critérios de: precisão dos dados, personalização, ausência de alucinação, tom adequado e redirecionamento construtivo.

---

## 🚀 Inovação e Impacto

O FinGuide é inovador não pela tecnologia em si, mas pelo **problema de acesso** que resolve: orientação financeira personalizada e contínua, disponível para qualquer pessoa, a qualquer hora, sem custo de consultoria.

**Impacto individual:** redução do estresse financeiro e retomada do controle sobre o próprio dinheiro.

**Impacto familiar:** hábitos financeiros saudáveis se multiplicam dentro do núcleo familiar.

**Impacto sistêmico:** em escala, contribui para redução de inadimplência e aumento da educação financeira da população.

---

## 🛠️ Tecnologias e Ferramentas

- **Interface do agente**: Biblioteca Streamlit
- **LLM e verão**: Ollama (local) - llama3
- **Base de conhecimento:** arquivos `.csv` e `.json` estruturados
- **Linguagem de programação:** Python para aplicação do programa 

---

## 👤 Autor

Desenvolvido como projeto prático do curso de Inteligência Artificial da **DIO — Digital Innovation One** com parceria do Banco Bradesco.

---

> *"O FinGuide não substitui um consultor financeiro — ele garante que qualquer pessoa tenha acesso a um ponto de partida confiável para cuidar do próprio dinheiro."*
