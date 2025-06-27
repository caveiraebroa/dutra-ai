# Professor DUTRA - Testes de Configuração
# Testes básicos para verificar se a configuração está funcionando

import pytest
import os
from app import create_app, db
from config import get_config

class TestConfig:
    """Testes para configurações da aplicação"""
    
    def test_app_creation(self):
        """Testar se a aplicação Flask é criada corretamente"""
        app = create_app('testing')
        assert app is not None
        assert app.config['TESTING'] is True
        assert app.config['DEBUG'] is True
    
    def test_development_config(self):
        """Testar configurações de desenvolvimento"""
        config = get_config()
        assert config.DEBUG is True
        assert config.TESTING is False
        assert config.LOG_LEVEL == 'DEBUG'
    
    def test_production_config(self):
        """Testar configurações de produção"""
        # Simular ambiente de produção
        os.environ['FLASK_ENV'] = 'production'
        config = get_config()
        assert config.DEBUG is False
        assert config.TESTING is False
        assert config.LOG_LEVEL == 'WARNING'
        # Restaurar ambiente
        os.environ['FLASK_ENV'] = 'development'
    
    def test_secret_key(self):
        """Testar se a secret key está configurada"""
        app = create_app('testing')
        assert app.config['SECRET_KEY'] is not None
        assert len(app.config['SECRET_KEY']) > 10
    
    def test_elasticsearch_config(self):
        """Testar configurações do Elasticsearch"""
        app = create_app('testing')
        assert 'ELASTICSEARCH_HOST' in app.config
        assert 'ELASTICSEARCH_PORT' in app.config
        assert 'ELASTICSEARCH_API_KEY' in app.config
    
    def test_openai_config(self):
        """Testar configurações da OpenAI"""
        app = create_app('testing')
        assert 'OPENAI_API_KEY' in app.config
        assert 'OPENAI_MODEL' in app.config
    
    def test_extensions_loaded(self):
        """Testar se as extensões Flask estão carregadas"""
        app = create_app('testing')
        
        # Verificar se as extensões estão inicializadas
        assert hasattr(app, 'extensions')
        assert 'login_manager' in app.extensions
        assert 'sqlalchemy' in app.extensions
        assert 'migrate' in app.extensions
        assert 'cache' in app.extensions
        assert 'csrf' in app.extensions

class TestAppContext:
    """Testes com contexto da aplicação"""
    
    @pytest.fixture
    def app(self):
        """Fixture para criar aplicação de teste"""
        app = create_app('testing')
        return app
    
    @pytest.fixture
    def client(self, app):
        """Fixture para criar cliente de teste"""
        return app.test_client()
    
    def test_home_page(self, client):
        """Testar se a página inicial responde"""
        # Por enquanto retorna 404 pois não temos rotas ainda
        response = client.get('/')
        assert response.status_code in [404, 200]  # 404 por enquanto
    
    def test_app_config(self, app):
        """Testar configurações da aplicação"""
        assert app.config['TESTING'] is True
        assert app.config['WTF_CSRF_ENABLED'] is False 