from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# --- BANCO DE DADOS CONSOLIDADO (2019 - 2026) ---
HISTORICO_PROVENTOS = [
    # --- BRASIL (R$) ---
    # VIBRA (VBBR3)
    {"ticker": "VBBR3", "data": "16/12/2026", "valor": 0.7600, "ano": 2026},
    {"ticker": "VBBR3", "data": "27/02/2026", "valor": 0.3100, "ano": 2026},
    {"ticker": "VBBR3", "data": "28/11/2025", "valor": 0.5000, "ano": 2025},
    {"ticker": "VBBR3", "data": "29/08/2025", "valor": 0.2600, "ano": 2025},
    {"ticker": "VBBR3", "data": "30/05/2025", "valor": 0.2300, "ano": 2025},
    {"ticker": "VBBR3", "data": "27/02/2025", "valor": 0.4600, "ano": 2025},
    {"ticker": "VBBR3", "data": "29/11/2024", "valor": 0.3000, "ano": 2024},
    {"ticker": "VBBR3", "data": "30/08/2024", "valor": 0.3000, "ano": 2024},
    {"ticker": "VBBR3", "data": "29/05/2024", "valor": 0.4000, "ano": 2024},
    {"ticker": "VBBR3", "data": "29/02/2024", "valor": 0.4300, "ano": 2024},
    {"ticker": "VBBR3", "data": "28/02/2023", "valor": 0.3900, "ano": 2023},
    {"ticker": "VBBR3", "data": "30/05/2022", "valor": 0.1100, "ano": 2022},
    {"ticker": "VBBR3", "data": "23/12/2021", "valor": 0.1300, "ano": 2021},

    # ENGIE (EGIE3)
    {"ticker": "EGIE3", "data": "23/12/2025", "valor": 1.2557, "ano": 2025},
    {"ticker": "EGIE3", "data": "27/05/2025", "valor": 0.8166, "ano": 2025},
    {"ticker": "EGIE3", "data": "07/02/2025", "valor": 0.2189, "ano": 2025},
    {"ticker": "EGIE3", "data": "26/07/2024", "valor": 0.9975, "ano": 2024},
    {"ticker": "EGIE3", "data": "27/12/2023", "valor": 0.6716, "ano": 2023},
    {"ticker": "EGIE3", "data": "26/09/2023", "valor": 1.2739, "ano": 2023},
    {"ticker": "EGIE3", "data": "12/12/2022", "valor": 0.9198, "ano": 2022},

    # ENERGISA (ENGI11)
    {"ticker": "ENGI11", "data": "28/01/2025", "valor": 0.2188, "ano": 2025},
    {"ticker": "ENGI11", "data": "22/05/2024", "valor": 0.8166, "ano": 2024},
    {"ticker": "ENGI11", "data": "27/12/2023", "valor": 0.6716, "ano": 2023},

    # JBS (JBSS3)
    {"ticker": "JBSS3", "data": "17/06/2025", "valor": 1.0000, "ano": 2025},
    {"ticker": "JBSS3", "data": "14/05/2025", "valor": 2.0000, "ano": 2025},
    {"ticker": "JBSS3", "data": "15/01/2025", "valor": 1.0000, "ano": 2025},
    {"ticker": "JBSS3", "data": "07/10/2024", "valor": 2.0000, "ano": 2024},
    {"ticker": "JBSS3", "data": "29/06/2023", "valor": 1.0000, "ano": 2023},
    {"ticker": "JBSS3", "data": "24/11/2022", "valor": 1.0000, "ano": 2022},
    {"ticker": "JBSS3", "data": "24/11/2021", "valor": 1.0000, "ano": 2021},

    # CURY (CURY3)
    {"ticker": "CURY3", "data": "31/12/2026", "valor": 0.4545, "ano": 2026},
    {"ticker": "CURY3", "data": "23/12/2025", "valor": 1.8601, "ano": 2025},
    {"ticker": "CURY3", "data": "07/10/2025", "valor": 0.6852, "ano": 2025},
    {"ticker": "CURY3", "data": "10/07/2024", "valor": 0.9142, "ano": 2024},
    {"ticker": "CURY3", "data": "30/09/2022", "valor": 0.5154, "ano": 2022},
    {"ticker": "CURY3", "data": "16/12/2021", "valor": 0.1713, "ano": 2021},

    # BLAU (BLAU3)
    {"ticker": "BLAU3", "data": "15/12/2025", "valor": 0.6754, "ano": 2025},
    {"ticker": "BLAU3", "data": "10/07/2024", "valor": 0.1407, "ano": 2024},
    {"ticker": "BLAU3", "data": "17/04/2023", "valor": 0.1830, "ano": 2023},
    {"ticker": "BLAU3", "data": "29/12/2022", "valor": 0.1765, "ano": 2022},

    # --- USA: ORACLE (ORCL) - $ (Larry Ellison) ---
    {"ticker": "ORCL", "data": "23/01/2026", "valor": 0.50, "ano": 2026},
    {"ticker": "ORCL", "data": "23/10/2025", "valor": 0.50, "ano": 2025},
    {"ticker": "ORCL", "data": "24/07/2025", "valor": 0.50, "ano": 2025},
    {"ticker": "ORCL", "data": "23/04/2025", "valor": 0.50, "ano": 2025},
    {"ticker": "ORCL", "data": "23/01/2025", "valor": 0.40, "ano": 2025},
    {"ticker": "ORCL", "data": "24/10/2024", "valor": 0.40, "ano": 2024},
    {"ticker": "ORCL", "data": "25/07/2024", "valor": 0.40, "ano": 2024},
    {"ticker": "ORCL", "data": "24/04/2024", "valor": 0.40, "ano": 2024},
    {"ticker": "ORCL", "data": "25/01/2024", "valor": 0.40, "ano": 2024},
    {"ticker": "ORCL", "data": "26/10/2023", "valor": 0.40, "ano": 2023},
    {"ticker": "ORCL", "data": "26/07/2023", "valor": 0.40, "ano": 2023},
    {"ticker": "ORCL", "data": "24/04/2023", "valor": 0.40, "ano": 2023},
    {"ticker": "ORCL", "data": "24/01/2023", "valor": 0.32, "ano": 2023},
    {"ticker": "ORCL", "data": "25/10/2022", "valor": 0.32, "ano": 2022},
    {"ticker": "ORCL", "data": "26/07/2022", "valor": 0.32, "ano": 2022},
    {"ticker": "ORCL", "data": "21/04/2022", "valor": 0.32, "ano": 2022},
    {"ticker": "ORCL", "data": "19/01/2022", "valor": 0.32, "ano": 2022},
    {"ticker": "ORCL", "data": "26/10/2021", "valor": 0.32, "ano": 2021},
    {"ticker": "ORCL", "data": "29/07/2021", "valor": 0.32, "ano": 2021},
    {"ticker": "ORCL", "data": "22/04/2021", "valor": 0.32, "ano": 2021},
    {"ticker": "ORCL", "data": "21/01/2021", "valor": 0.24, "ano": 2021},

    # --- EUROPA: INDITEX (ITX) - € (Amancio Ortega) ---
    {"ticker": "ITX", "data": "03/11/2025", "valor": 0.84, "ano": 2025},
    {"ticker": "ITX", "data": "02/05/2025", "valor": 0.84, "ano": 2025},
    {"ticker": "ITX", "data": "04/11/2024", "valor": 0.77, "ano": 2024},
    {"ticker": "ITX", "data": "02/05/2024", "valor": 0.77, "ano": 2024},
    {"ticker": "ITX", "data": "02/11/2023", "valor": 0.60, "ano": 2023},
    {"ticker": "ITX", "data": "02/05/2023", "valor": 0.60, "ano": 2023},
    {"ticker": "ITX", "data": "02/11/2022", "valor": 0.465, "ano": 2022},
    {"ticker": "ITX", "data": "02/05/2022", "valor": 0.465, "ano": 2022},
    {"ticker": "ITX", "data": "02/11/2021", "valor": 0.35, "ano": 2021},
    {"ticker": "ITX", "data": "03/05/2021", "valor": 0.35, "ano": 2021},
]

# --- PERFIS DOS BILIONÁRIOS ---
DADOS_BILIONARIOS = {
    "Joesley": { "nome": "Joesley Batista", "moeda": "R$", "foto": "joesleybatista.webp", "ativos": [{"ticker": "JBSS3"}] },
    "Wesley": { "nome": "Wesley Batista", "moeda": "R$", "foto": "wesleybatista.webp", "ativos": [{"ticker": "JBSS3"}] },
    "Ronaldo": {
        "nome": "Ronaldo Cezar Coelho", "moeda": "R$", "foto": "ronaldocezar.webp",
        "ativos": [
            {"ticker": "EGIE3", "acoes": 41938027}, 
            {"ticker": "VBBR3", "acoes": 59803436},
            {"ticker": "ENGI11", "acoes": 25000000}
        ]
    },
    "Fabio": { "nome": "Fabio Cury", "moeda": "R$", "foto": "fabiocury.jpg", "ativos": [{"ticker": "CURY3", "acoes": 94546195}] },
    "Marcelo": { "nome": "Marcelo Rodolfo Hahn", "moeda": "R$", "foto": "marcelohahn.webp", "ativos": [{"ticker": "BLAU3", "acoes": 147999999}] },
    "Larry": { "nome": "Larry Ellison", "moeda": "$", "foto": "larryellison.webp", "ativos": [{"ticker": "ORCL", "acoes": 1158232353}] },
    "Amancio": { "nome": "Amancio Ortega", "moeda": "€", "foto": "amancioortega.webp", "ativos": [{"ticker": "ITX", "acoes": 1848000315}] }
}

def formatar_valor(valor, moeda):
    if valor >= 1e9: return f"{moeda} {valor/1e9:.2f}B"
    return f"{moeda} {valor/1e6:.1f}M"

def calcular_dados_ano(chave, ano_alvo):
    p = DADOS_BILIONARIOS[chave]
    total = 0.0
    vpa_ref = 0.0
    for item in p["ativos"]:
        ticker = item["ticker"]
        # Lógica JBS
        if ticker == "JBSS3":
            qtd = 250044325 if ano_alvo >= 2025 else 500088650
        else:
            qtd = item.get("acoes", 0)
        
        vpa_ano = sum([prov["valor"] for prov in HISTORICO_PROVENTOS if prov["ticker"] == ticker and prov["ano"] == ano_alvo])
        total += (vpa_ano * qtd)
        vpa_ref = vpa_ano
    return total, vpa_ref

@app.route('/api/fortunas')
def pegar_fortunas():
    ano = int(request.args.get('ano', '2025'))
    res = []
    for chave in DADOS_BILIONARIOS:
        p = DADOS_BILIONARIOS[chave]
        ganho, vpa = calcular_dados_ano(chave, ano)
        res.append({
            "nome": p["nome"],
            "renda_anual": formatar_valor(ganho, p["moeda"]),
            "media_mensal": formatar_valor(ganho / 12, p["moeda"]),
            "vpa_info": f"{p['moeda']} {vpa:.2f}/ação",
            "foto": p["foto"]
        })
    return jsonify(res)

@app.route('/api/consolidado/<perfil>')
def pegar_consolidado(perfil):
    chave_real = next((k for k in DADOS_BILIONARIOS if k.lower() == perfil.lower()), None)
    if not chave_real: return jsonify({"erro": "404"}), 404
    
    p = DADOS_BILIONARIOS[chave_real]
    anos = [2021, 2022, 2023, 2024, 2025]
    historico = []
    total_acumulado = 0.0
    for ano in anos:
        ganho, _ = calcular_dados_ano(chave_real, ano)
        total_acumulado += ganho
        historico.append({"ano": ano, "valor": formatar_valor(ganho, p["moeda"])})
    
    return jsonify({
        "nome": p["nome"],
        "ticker": p["ativos"][0]["ticker"] if len(p["ativos"]) == 1 else "MULTI ASSETS",
        "historico": historico,
        "total_geral": formatar_valor(total_acumulado, p["moeda"]),
        "foto": p["foto"]
    })

if __name__ == '__main__':
    app.run()
