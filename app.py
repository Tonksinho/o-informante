from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# --- BANCO DE DADOS ---
HISTORICO_PROVENTOS = [
    {"ticker": "VBBR3", "valor": 0.5000, "ano": 2025},
    {"ticker": "EGIE3", "valor": 1.2557, "ano": 2025},
    {"ticker": "JBSS3", "valor": 2.0000, "ano": 2025},
    {"ticker": "ORCL", "valor": 0.50, "ano": 2025},
    {"ticker": "ITX", "valor": 0.84, "ano": 2025}
]

DADOS_BILIONARIOS = {
    "Joesley": { "nome": "Joesley Batista", "moeda": "R$", "foto": "joesleybatista.webp", "ativos": [{"ticker": "JBSS3"}] },
    "Wesley": { "nome": "Wesley Batista", "moeda": "R$", "foto": "wesleybatista.webp", "ativos": [{"ticker": "JBSS3"}] },
    "Ronaldo": { "nome": "Ronaldo Cezar Coelho", "moeda": "R$", "foto": "ronaldocezar.webp", "ativos": [{"ticker": "VBBR3", "acoes": 59803436}] },
    "Fabio": { "nome": "Fabio Cury", "moeda": "R$", "foto": "fabiocury.jpg", "ativos": [{"ticker": "CURY3", "acoes": 94546195}] },
    "Marcelo": { "nome": "Marcelo Rodolfo Hahn", "moeda": "R$", "foto": "marcelohahn.webp", "ativos": [{"ticker": "BLAU3", "acoes": 147999999}] },
    "Larry": { "nome": "Larry Ellison", "moeda": "$", "foto": "larryellison.webp", "ativos": [{"ticker": "ORCL", "acoes": 1158232353}] },
    "Amancio": { "nome": "Amancio Ortega", "moeda": "€", "foto": "amancioortega.webp", "ativos": [{"ticker": "ITX", "acoes": 1848000315}] }
}

# --- ROTA DE TESTE (PÁGINA INICIAL) ---
@app.route('/')
def home():
    return "O SERVIDOR ESTA VIVO! Tente acessar /api/fortunas"

# --- ROTAS DA API ---
@app.route('/api/fortunas')
def pegar_fortunas():
    ano = int(request.args.get('ano', '2025'))
    res = []
    for chave, p in DADOS_BILIONARIOS.items():
        vpa = next((item['valor'] for item in HISTORICO_PROVENTOS if item['ticker'] == p['ativos'][0]['ticker'] and item['ano'] == ano), 0)
        ganho = vpa * p['ativos'][0].get('acoes', 250000000) # Simplificado para teste
        res.append({
            "nome": p["nome"],
            "renda_anual": f"{p['moeda']} {ganho/1e6:.1f}M",
            "media_mensal": f"{p['moeda']} {ganho/12/1e6:.1f}M",
            "vpa_info": f"{p['moeda']} {vpa:.2f}/ação",
            "foto": p["foto"]
        })
    return jsonify(res)

@app.route('/api/consolidado/<perfil>')
def pegar_consolidado(perfil):
    return jsonify({"status": "Rota consolidado ativa para " + perfil})

if __name__ == '__main__':
    app.run()
