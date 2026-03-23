## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir tipos de gastos adequados ao comportamento do usuário |


---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos por categoria 
- **Contexto do Teste**:
O usuário (Lucas Mendes — USR001) pergunta quanto gastou com alimentação no mês. O agente deve buscar os dados reais do arquivo transacoes.csv e retornar o valor correto, detalhando as subcategorias quando relevante.

- **Pergunta:** "Quanto gastei com alimentação esse mês?"
- **Resposta esperada:** Valor baseado no `transacoes.csv`
- **Resultado:** "Com base nas suas transações de novembro, seus gastos com alimentação totalizaram R$ 674,00 — o que representa cerca de 19,3% da sua renda mensal.
Aqui está o detalhamento por subcategoria:

• Supermercado:  R$ 388,70

• Delivery (iFood):  R$ 285,30

Um ponto de atenção: só o delivery representa R$ 285,30 — quase 42% de todo o seu gasto com alimentação. Reduzir os pedidos de delivery para, no máximo, R$ 120/mês já liberaria cerca de R$ 165 por mês no seu orçamento. 
Quer que eu te ajude a definir um teto de gastos para essa categoria?"

### Teste 2: Sugestão Personalizada de Gastos
- **Contexto do Teste**: O usuário (Roberto Carvalho — USR003) pede uma sugestão de como melhorar seus gastos. O agente deve cruzar os dados do perfil_usuario.json e do historico_atendimentos.csv para entregar uma recomendação contextualizada — não genérica — levando em conta que Roberto está em processo de quitação de dívidas, tem renda de R$ 2.800 e já cortou R$ 106,60/mês em assinaturas.
  
- **Pergunta:** "Qual sugestão sobre gastos você recomenda para mim"?
- **Resposta esperada:** Sugestão compatível com o perfil do cliente
- **Resultado:** "Olá, Roberto! Com base no seu perfil e no histórico das nossas conversas, tenho uma recomendação bem específica para o seu momento atual. 💪
Você está em um ponto crítico e positivo ao mesmo tempo: a dívida já caiu de R$ 18.400 para R$ 12.600 em 3 meses — isso é um resultado real. O foco agora é manter o ritmo e fechar essa dívida até abril.
Minha principal sugestão para você neste momento:
1. Redirecione os R$ 106,60 das assinaturas canceladas integralmente para amortização da dívida. Você já tomou a decisão certa ao cancelar — agora esse valor precisa ir direto para o pagamento, antes de qualquer outro gasto variável.
2. Proteja o orçamento de alimentação. Seus R$ 402,00 com alimentação estão num nível controlado para a sua renda. Evite aumentar esse gasto — cozinhar em casa é seu maior aliado agora.
3. Ainda não pense em investir. Com dívidas a 4% ao mês, qualquer valor guardado renderia menos do que o custo dos juros. Quitar primeiro é a melhor aplicação que você pode fazer agora.
Projetando o ritmo atual, você quita tudo em aproximadamente 5 meses. Quando isso acontecer, a gente monta juntos a sua reserva de emergência."


### Teste 3: Pergunta fora do escopo
- **Contexto do teste**: O usuário faz uma pergunta completamente alheia ao domínio do FinGuide — neste caso, consulta a previsão do tempo. O agente deve recusar educadamente, deixar claro seu escopo de atuação e convidar o usuário a retomar o tema financeiro.
 
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de saúde financeira 
- **Resultado:** "Boa pergunta para planejar o fim de semana — mas essa está fora da minha alçada!
Sou especializado em saúde financeira: controle de gastos, dívidas, planejamento de metas e educação financeira. Informações sobre clima, tempo ou qualquer outro tema fora desse domínio estão além do que consigo ajudar."


### Teste 4: Informação inexistente
- **Contexto do teste**: O usuário pergunta sobre gastos de uma categoria ou item que não existe nos registros disponíveis — neste caso, gastos com 'viagens internacionais' de um usuário que não possui essa transação na base. O agente deve admitir a ausência da informação com honestidade, sem inventar dados, e orientar o usuário sobre como fornecer essa informação.
  
- **Pergunta:** "Quanto foram os meus gastos com viagens internacionais esse mês?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** "Procurei nas suas transações de novembro e não encontrei nenhum registro de gasto com viagens internacionais no período.
Isso pode significar duas coisas: ou não houve esse gasto no mês, ou ele ainda não foi registrado na sua base de transações.
Para que eu consiga te ajudar com essa categoria, você pode:
• Me informar o valor gasto diretamente aqui na conversa — passagens, hospedagem, câmbio, etc.
• Verificar no extrato do seu cartão ou conta bancária se há lançamentos relacionados que ainda não foram incluídos.
Posso analisar o gasto e te ajudar a entender se ele está dentro do que seu orçamento comporta — é só me passar os números!"

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- O agente respondeu muito bem a cada um dos cenários e suprindo as expectativas sobre o seu comportamento e atendimento às necessidades do usuário, assim como localizou corretamente de onde tirar cada informação requisitada.

**O que pode melhorar:**
- O agente demonstrou um tempo de resposta um pouco mais demorado que o normal, o que pode afetar bastante a experência do usuário e deve ser melhorado.
