import json
import pandas as pd
import requests
import streamlit as st

# ============= CONFIGURAÇÃO ===============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "llama3"

# ============= CARREGAR DADOS =============
perfil = json.load(open('./data/perfil_usuario.json'))
usuario = perfil[0]
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimentos_1.csv')
dicas = json.load(open('./data/dicas_financeiras.json'))

# ============== MONTAR CONTEXTO ===========
contexto = f"""
USUARIO: {usuario['dados_pessoais']['nome']}, {usuario['dados_pessoais']['idade']} anos
CIDADE: {usuario['dados_pessoais']['cidade']} - {usuario['dados_pessoais']['estado']}
PERFIL: {usuario['perfil_comportamental']['tipo_perfil']}
RENDA: R$ {usuario['perfil_financeiro']['renda_mensal_liquida']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

DICAS FINANCEIRAS:
{json.dumps(dicas, indent=2, ensure_ascii=False)}
"""

# ============== SYTEM PROMPT ===============
SYSTEM_PROMPT = """Você é o FinGuide, ou Finn um agente financeiro inteligente especializado em saúde financeira e cujo objetivo é educar e instruir com usuários com seus gastos e ajudar a mander uma boa saúde financeira.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos;
2. Nunca invente informações financeiras;
3. Se não souber algo, admita e ofereça alternativas;
4. Linguagem simples e educativa, sempre garatindo que todas as dúvidas sejam sanadas;
5. Sempre esclareça todo o conteúdo necessário para que o usuário entenda mais sobre a área e tenha mais entendimento sobre o que perguntar.
6. Nunca responda infomações fora do contexto de saúde financeira.
"""

# ================ CHAMAR OLLAMA ===============
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO,"prompt": prompt, "stream": False })
    return r.json()['response']

#============== INTERFACE =====================
st.title("Olá! Sou FinGuide, seu educador financeiro 💸")

if pergunta := st.chat_input("Sua dúvida sobre saúde financeira..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta)) 
