# Professor DUTRA - Script de Verificação de Configuração
# Script para verificar se todas as configurações estão funcionando

import os
import sys
from dotenv import load_dotenv

def check_env_file():
    """Verificar se o arquivo .env existe e está configurado"""
    print("🔍 Verificando arquivo .env...")
    
    if not os.path.exists('.env'):
        print("❌ Arquivo .env não encontrado!")
        print("📝 Crie o arquivo .env na raiz do projeto com as seguintes variáveis:")
        print()
        print("# Flask")
        print("SECRET_KEY=dutra-ia-secret-key-2024-super-segura-e-unica")
        print("FLASK_ENV=development")
        print("FLASK_DEBUG=True")
        print()
        print("# Elasticsearch")
        print("ELASTICSEARCH_HOST=professor-dutra-d99e7d.es.us-central1.gcp.elastic.cloud")
        print("ELASTICSEARCH_PORT=443")
        print("ELASTICSEARCH_USE_SSL=True")
        print("ELASTICSEARCH_API_KEY=TnQtY21KY0JEeVJWNUxUTmpNc206bVcxNmNLOHlrbmw5eXlZTkFibHBWQQ==")
        print("ELASTICSEARCH_PROJECT_ID=d99e7d0edd0a4cc69b38e5c75efb8421")
        print()
        print("# OpenAI")
        print("OPENAI_API_KEY=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")
        print("OPENAI_MODEL=gpt-3.5-turbo")
        print()
        print("# APIs de Notícias")
        print("GNEWS_API_KEY=715eee72a8075265700c93c67cfa1750")
        print("NEWSAPI_API_KEY=d5a5fac8e6de4e5e81ac5b3042e59f7b")
        print()
        print("# Debug")
        print("DEBUG_MODE=True")
        print("LOG_LEVEL=DEBUG")
        print("SHOW_ERROR_DETAILS=True")
        return False
    
    print("✅ Arquivo .env encontrado!")
    return True

def check_environment_variables():
    """Verificar se as variáveis de ambiente estão carregadas"""
    print("\n🔍 Verificando variáveis de ambiente...")
    
    # Carregar variáveis de ambiente
    load_dotenv()
    
    # Lista de variáveis obrigatórias
    required_vars = [
        'SECRET_KEY',
        'ELASTICSEARCH_HOST',
        'ELASTICSEARCH_API_KEY',
        'OPENAI_API_KEY',
        'GNEWS_API_KEY',
        'NEWSAPI_API_KEY'
    ]
    
    missing_vars = []
    
    for var in required_vars:
        value = os.environ.get(var)
        if value:
            # Mostrar apenas os primeiros caracteres por segurança
            masked_value = value[:10] + "..." if len(value) > 10 else value
            print(f"✅ {var}: {masked_value}")
        else:
            print(f"❌ {var}: NÃO CONFIGURADA")
            missing_vars.append(var)
    
    if missing_vars:
        print(f"\n⚠️  {len(missing_vars)} variáveis não estão configuradas!")
        return False
    
    print("\n✅ Todas as variáveis de ambiente estão configuradas!")
    return True

def check_flask_config():
    """Verificar se a configuração do Flask está funcionando"""
    print("\n🔍 Verificando configuração do Flask...")
    
    try:
        from config import get_config
        
        config = get_config()
        
        print(f"✅ Ambiente: {config.FLASK_ENV}")
        print(f"✅ Debug: {config.DEBUG}")
        print(f"✅ Secret Key: {'Configurada' if config.SECRET_KEY else 'NÃO CONFIGURADA'}")
        print(f"✅ Elasticsearch Host: {config.ELASTICSEARCH_HOST}")
        print(f"✅ OpenAI Model: {config.OPENAI_MODEL}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao carregar configuração: {e}")
        return False

def check_app_creation():
    """Verificar se a aplicação Flask pode ser criada"""
    print("\n🔍 Verificando criação da aplicação Flask...")
    
    try:
        from app import create_app
        
        app = create_app('testing')
        
        print("✅ Aplicação Flask criada com sucesso!")
        print(f"✅ Configuração: {app.config['ENV']}")
        print(f"✅ Debug: {app.config['DEBUG']}")
        print(f"✅ Testing: {app.config['TESTING']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao criar aplicação: {e}")
        return False

def main():
    """Função principal do script"""
    print("🚀 Professor DUTRA - Verificação de Configuração")
    print("=" * 50)
    
    # Verificar arquivo .env
    env_ok = check_env_file()
    
    if not env_ok:
        print("\n❌ Configuração incompleta. Corrija os problemas acima.")
        return
    
    # Verificar variáveis de ambiente
    vars_ok = check_environment_variables()
    
    if not vars_ok:
        print("\n❌ Variáveis de ambiente incompletas. Corrija os problemas acima.")
        return
    
    # Verificar configuração do Flask
    config_ok = check_flask_config()
    
    if not config_ok:
        print("\n❌ Configuração do Flask com problemas. Corrija os problemas acima.")
        return
    
    # Verificar criação da aplicação
    app_ok = check_app_creation()
    
    if not app_ok:
        print("\n❌ Criação da aplicação com problemas. Corrija os problemas acima.")
        return
    
    print("\n🎉 TODAS AS VERIFICAÇÕES PASSARAM!")
    print("✅ O Professor DUTRA está pronto para a próxima fase!")
    print("\n📋 Próximos passos:")
    print("1. Conexão com Elasticsearch")
    print("2. Criação de rotas básicas")
    print("3. Configuração da OpenAI")
    print("4. Sistema de autenticação")

if __name__ == "__main__":
    main() 