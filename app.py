# Professor DUTRA - Flask Básico
import os
from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
from elasticsearch import Elasticsearch
import openai

# Carregar variáveis do .env
load_dotenv()

app = Flask(__name__)

# Configurar Elasticsearch
def get_elasticsearch_client():
    """Criar cliente Elasticsearch"""
    host = os.getenv('ELASTICSEARCH_HOST')
    port = int(os.getenv('ELASTICSEARCH_PORT', 443))
    api_key = os.getenv('ELASTICSEARCH_API_KEY')
    
    return Elasticsearch(
        [f"https://{host}:{port}"],
        api_key=api_key,
        verify_certs=True
    )

# Configurar OpenAI
def setup_openai():
    """Configurar OpenAI"""
    api_key = os.getenv('OPENAI_API_KEY')
    openai.api_key = api_key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/status')
def status():
    """Rota para mostrar status do projeto"""
    status_info = {
        "projeto": "Professor DUTRA - Hub de Legislação de Trânsito",
        "fase_atual": "FASE 1 - COMPLETA ✅",
        "proxima_fase": "FASE 2 - Sistema de Busca Inteligente 🚧",
        "progresso_geral": "16.7% (1 de 6 fases)",
        "status_servicos": {
            "flask": "✅ Funcionando",
            "elasticsearch": "✅ Conectado",
            "openai": "✅ Integrado"
        },
        "rotas_disponiveis": [
            "/ - Página inicial",
            "/status - Status do projeto",
            "/test-elastic - Teste Elasticsearch",
            "/test-openai - Teste OpenAI"
        ],
        "próximos_passos": [
            "Sistema de busca básico (Elasticsearch + OpenAI)",
            "Interface web simples (HTML/CSS)",
            "Autenticação básica",
            "Testes de funcionalidade"
        ]
    }
    return jsonify(status_info)

@app.route('/test-elastic')
def test_elastic():
    """Rota para testar conexão com Elasticsearch"""
    try:
        es = get_elasticsearch_client()
        info = es.info()
        
        return jsonify({
            "status": "success",
            "message": "Conexão com Elasticsearch OK!",
            "version": info['version']['number'],
            "cluster": info['cluster_name']
        })
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Erro na conexão: {str(e)}"
        }), 500

@app.route('/test-openai')
def test_openai():
    """Rota para testar conexão com OpenAI"""
    try:
        setup_openai()
        
        # Teste simples - perguntar sobre legislação de trânsito
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Diga apenas: 'Professor DUTRA - OpenAI funcionando!'"}
            ],
            max_tokens=50
        )
        
        return jsonify({
            "status": "success",
            "message": "Conexão com OpenAI OK!",
            "response": response.choices[0].message.content,
            "model": "gpt-3.5-turbo"
        })
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Erro na conexão: {str(e)}"
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 