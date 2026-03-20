# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Atuação do FinGuide |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_usuario.json` | JSON | Personalizar recomendações |
| `dicas_financeiras.json` | JSON | Sugerir dicas adequadas ao perfil |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |


---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

A pasta `produtos_financeiros` e `perfil_cliente` foram, respectivamente, alteradas juntamente com os seus dados para `dicas_financeiras` e `perfil_usuario` para ter maior compatibilidade com o tema escohlido que, apesar de também fazer parte da área de finanças, tem como próposito auxiliar o usuário com seus gastos e melhorar sua saúde financeira.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Existem duas possibilidades: injetar os dados diretamente no prompt ou carregar os arquivos via código:

```python
import pandas as pd
import json

# CSVs
historico = pd.read_csv('data/historico_atendimento.csv')
transacoes = pd.read_csv('data/transacoes.csv')

# JSONs
with open('data/perfil_usuario.json', 'r', encoding='utf-8') as f:
    perfil = json.load(f)

with open('data/dicas_financeiras.json', 'r', encoding='utf-8') as f:
    produtos = json.load(f)
```


### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

É possível "injetar" os dados no prompt, garantindo que o agente tenha um melhor direcionamento. Para soluções mais robustas, o ideal é que essas informações sejam carregadas dinamicamente para ganhar flexibilidade.

```text
INFORMAÇÕES DO USUARIO:
[
  {
    "id_usuario": "USR001",
    "dados_pessoais": {
      "nome": "Lucas Mendes",
      "idade": 29,
      "cidade": "São Paulo",
      "estado": "SP",
      "escolaridade": "superior_completo",
      "estado_civil": "solteiro",
      "dependentes": 0
    }
  }
]

PERFIL DO USUARIO:
{
  "perfil_financeiro": {
    "renda_mensal_liquida": 3500,
    "fonte_renda": "CLT",
    "estabilidade_emprego": "estavel",
    "possui_reserva_emergencia": false,
    "meses_reserva_atual": 0,
    "possui_investimentos": false,
    "possui_imovel": false,
    "possui_veiculo": true,
    "score_credito": 620
  },
  "perfil_comportamental": {
    "tipo_perfil": "gastador_involuntario",
    "maior_dificuldade": "nao_saber_para_onde_vai_o_dinheiro",
    "motivacao_principal": "alivio_do_estresse_financeiro",
    "disciplina_financeira": "baixa",
    "conhecimento_financeiro": "basico",
    "aberto_a_investir": true,
    "prefere_comunicacao": "chat_texto",
    "horario_preferido_interacao": "noite"
  }
}


TRANSACOES DO USUARIO:
id_transacao,id_usuario,data,descricao,categoria,subcategoria,valor,tipo,forma_pagamento,parcelas,essencial
TRX001,USR001,2024-11-01,Aluguel novembro,moradia,aluguel,-1200.00,debito,transferencia,1,sim
TRX002,USR001,2024-11-01,Conta de luz,moradia,energia_eletrica,-148.30,debito,debito_automatico,1,sim
TRX003,USR001,2024-11-02,Supermercado Extra,alimentacao,supermercado,-312.40,debito,cartao_debito,1,sim
TRX004,USR001,2024-11-03,iFood - Hambúrguer,alimentacao,delivery,-54.90,debito,cartao_credito,1,nao
TRX005,USR001,2024-11-04,Uber - Trabalho,transporte,aplicativo_transporte,-23.50,debito,cartao_credito,1,sim
TRX006,USR001,2024-11-05,Netflix,lazer,streaming,-55.90,debito,cartao_credito,1,nao
TRX007,USR001,2024-11-05,Spotify,lazer,streaming,-21.90,debito,cartao_credito,1,nao
TRX008,USR001,2024-11-06,Farmácia - Remédio,saude,farmacia,-87.60,debito,cartao_debito,1,sim
TRX009,USR001,2024-11-07,iFood - Pizza,alimentacao,delivery,-72.00,debito,cartao_credito,1,nao

DICAS PARA INSTRUIR O USUARIO:
{
  "versao": "1.0",
  "descricao": "Base de conhecimento de orientações e dicas financeiras do FinGuide AI. Usada para personalizar recomendações conforme perfil e contexto do usuário.",
  "categorias": [
    {
      "id": "CAT001",
      "categoria": "controle_de_gastos",
      "perfis_alvo": [
        "gastador_involuntario",
        "iniciante_consciente",
        "endividado_em_recuperacao"
      ],
      "nivel_conhecimento": "basico",
      "dicas": [
        {
          "id": "DIC001",
          "titulo": "Método 50-30-20",
          "descricao": "Divida sua renda líquida em três blocos: 50% para necessidades (moradia, alimentação, transporte, saúde), 30% para desejos (lazer, restaurantes, assinaturas) e 20% para poupança e pagamento de dívidas. É um ponto de partida simples e eficaz para quem nunca fez controle financeiro.",
          "quando_aplicar": "primeiro_contato_sem_historico_financeiro",
          "exemplo_pratico": "Renda de R$3.000: R$1.500 para necessidades, R$900 para desejos, R$600 para poupar ou quitar dívidas.",
          "tags": [
            "orcamento",
            "metodo",
            "iniciante"
          ]
        }
      ]
    }
  ]
}

```
---

## Exemplo de contexto montado:
```
Dados do Usuario:
- Nome: João Silva
- Perfil: Moderado
- Idade: 29
- Cidade: São Paulo
- Estado": SP
- Escolaridade: Superior completo
- Estado civil: Solteiro
- Dependentes: 0
- Renda mensal líquida: R$ 5.000

Perfil comportamental do usuário:
 - Tipo perfil: Gastador involuntario
 - Maior Dificuldade: Nao saber para onde vai o dinheiro
 - Motivacao Principal: Alivio do estresse financeiro
 - Disciplina_financeira": Baixa
 - Conhecimento financeiro: Básico

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
- 04/11: Transporte - R$ 23,90
- 08/11: Aluguel - R$ 1200
...
```
