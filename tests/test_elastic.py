# Teste SIMPLES de conexão com Elasticsearch
import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch

# Carregar variáveis do .env
load_dotenv()

def test_elastic_connection():
    """Teste SIMPLES de conexão com Elasticsearch"""
    
    print("🔍 Testando conexão com Elasticsearch...")
    
    # Pegar configurações do .env
    host = os.getenv('ELASTICSEARCH_HOST')
    port = int(os.getenv('ELASTICSEARCH_PORT', 443))
    api_key = os.getenv('ELASTICSEARCH_API_KEY')
    use_ssl = os.getenv('ELASTICSEARCH_USE_SSL', 'True').lower() == 'true'
    
    print(f"Host: {host}")
    print(f"Porta: {port}")
    print(f"SSL: {use_ssl}")
    print(f"API Key: {api_key[:10]}..." if api_key else "API Key: NÃO CONFIGURADA")
    
    try:
        # Criar cliente Elasticsearch
        es = Elasticsearch(
            [f"https://{host}:{port}"],
            api_key=api_key,
            verify_certs=True
        )
        
        # Testar conexão
        info = es.info()
        
        print("✅ CONEXÃO SUCESSO!")
        print(f"Versão do Elasticsearch: {info['version']['number']}")
        print(f"Nome do cluster: {info['cluster_name']}")
        
        return True
        
    except Exception as e:
        print(f"❌ ERRO na conexão: {e}")
        return False

if __name__ == "__main__":
    test_elastic_connection() 