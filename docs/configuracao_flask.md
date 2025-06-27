# Configuração do Flask - Professor DUTRA

## Visão Geral

Este documento explica como o Flask foi configurado no Professor DUTRA, incluindo todas as extensões, configurações de ambiente e sistema de logs.

## Estrutura de Configuração

### 1. Arquivo de Configurações (`config.py`)

O arquivo `config.py` contém todas as configurações da aplicação organizadas por ambiente:

#### **Configurações Base (Config)**
- **Flask**: Secret key, ambiente, debug
- **Elasticsearch**: Host, porta, SSL, API key
- **OpenAI**: API key, modelo
- **Banco de Dados**: URL de conexão
- **Email**: Configurações SMTP
- **APIs de Notícias**: GNews e NewsAPI
- **Debug**: Controles para dashboard do desenvolvedor
- **Sessão**: Configurações de segurança
- **Upload**: Limites de arquivo
- **Cache**: Configurações de cache

#### **Configurações por Ambiente**

##### **DevelopmentConfig**
- Debug ativo
- Logs detalhados
- Elasticsearch local
- Configurações de desenvolvimento

##### **ProductionConfig**
- Debug desabilitado
- Logs mínimos
- Configurações de segurança
- Cache otimizado

##### **TestingConfig**
- Banco em memória
- CSRF desabilitado
- Configurações para testes

### 2. Factory da Aplicação (`app/__init__.py`)

O arquivo `app/__init__.py` implementa o padrão **Application Factory**:

#### **Função `create_app()`**
- Cria a aplicação Flask
- Carrega configurações baseadas no ambiente
- Inicializa todas as extensões
- Registra blueprints
- Configura handlers de erro

#### **Função `setup_logging()`**
- Configura sistema de logs estruturados
- Logs em arquivo e console
- Formato JSON para fácil parsing
- Níveis de log configuráveis

#### **Função `initialize_extensions()`**
- Flask-Login: Autenticação de usuários
- Flask-SQLAlchemy: ORM para banco de dados
- Flask-Migrate: Migrações de banco
- Flask-Caching: Sistema de cache
- Flask-WTF: Proteção CSRF

#### **Função `register_blueprints()`**
- Registra todos os blueprints da aplicação
- Organiza rotas por funcionalidade
- Prefixos de URL configuráveis

#### **Função `register_error_handlers()`**
- Handlers personalizados para erros 404 e 500
- Logs de erro estruturados
- Rollback de transações em caso de erro

## Extensões Flask Configuradas

### 1. **Flask-Login** 👤
- **Função**: Gerenciar autenticação de usuários
- **Configuração**: Login view, mensagens, categorias
- **Benefícios**: Sessões seguras, decorators para proteção

### 2. **Flask-SQLAlchemy** 🗄️
- **Função**: ORM para banco de dados relacional
- **Configuração**: URL de conexão, pool de conexões
- **Benefícios**: Interface Python para banco de dados

### 3. **Flask-Migrate** 🔄
- **Função**: Migrações de banco de dados
- **Configuração**: Integração com SQLAlchemy
- **Benefícios**: Controle de versão do banco

### 4. **Flask-Caching** ⚡
- **Função**: Sistema de cache
- **Configuração**: Tipo de cache, timeout
- **Benefícios**: Performance otimizada

### 5. **Flask-WTF** 🛡️
- **Função**: Formulários seguros com CSRF protection
- **Configuração**: Chave secreta, validação
- **Benefícios**: Proteção contra ataques CSRF

## Sistema de Logs

### **Configuração**
- **Formato**: JSON estruturado
- **Destinos**: Arquivo (`logs/dutra.log`) e console
- **Níveis**: DEBUG, INFO, WARNING, ERROR
- **Rotação**: Configurável por ambiente

### **Estrutura dos Logs**
```json
{
  "timestamp": "2024-01-01T10:00:00Z",
  "level": "INFO",
  "name": "dutra",
  "message": "Professor DUTRA iniciado com sucesso!"
}
```

### **Logs por Ambiente**
- **Desenvolvimento**: DEBUG (logs detalhados)
- **Produção**: WARNING (logs mínimos)
- **Teste**: DEBUG (logs para debugging)

## Variáveis de Ambiente

### **Arquivo `.env`**
O arquivo `.env` contém todas as configurações sensíveis:

```bash
# Flask
SECRET_KEY=dutra-ia-secret-key-2024-super-segura-e-unica
FLASK_ENV=development
FLASK_DEBUG=True

# Elasticsearch
ELASTICSEARCH_HOST=professor-dutra-d99e7d.es.us-central1.gcp.elastic.cloud
ELASTICSEARCH_PORT=443
ELASTICSEARCH_USE_SSL=True
ELASTICSEARCH_API_KEY=TnQtY21KY0JEeVJWNUxUTmpNc206bVcxNmNLOHlrbmw5eXlZTkFibHBWQQ==
ELASTICSEARCH_PROJECT_ID=d99e7d0edd0a4cc69b38e5c75efb8421

# OpenAI
OPENAI_API_KEY=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
OPENAI_MODEL=gpt-3.5-turbo

# APIs de Notícias
GNEWS_API_KEY=715eee72a8075265700c93c67cfa1750
NEWSAPI_API_KEY=d5a5fac8e6de4e5e81ac5b3042e59f7b

# Debug
DEBUG_MODE=True
LOG_LEVEL=DEBUG
SHOW_ERROR_DETAILS=True
```

### **Segurança**
- Arquivo `.env` não é versionado (`.gitignore`)
- Template disponível em `env_template.txt`
- Chaves sensíveis protegidas

## Configurações de Segurança

### **Sessões**
- **Cookie Secure**: False em desenvolvimento, True em produção
- **HttpOnly**: True (proteção XSS)
- **SameSite**: Lax (proteção CSRF)
- **Lifetime**: 1 hora

### **CSRF Protection**
- Habilitado em todos os formulários
- Desabilitado em testes
- Configuração automática via Flask-WTF

### **Upload de Arquivos**
- **Tamanho máximo**: 16MB
- **Tipos permitidos**: Configuráveis
- **Validação**: Automática

## Testes de Configuração

### **Arquivo `tests/test_config.py`**
Testes automatizados para verificar:

- Criação da aplicação
- Configurações por ambiente
- Secret key
- Configurações do Elasticsearch
- Configurações da OpenAI
- Extensões carregadas
- Resposta da aplicação

### **Execução dos Testes**
```bash
pytest tests/test_config.py -v
```

## Dashboard do Desenvolvedor

### **Configurações de Debug**
- **DEBUG_MODE**: Controle geral do modo debug
- **LOG_LEVEL**: Nível de detalhamento dos logs
- **SHOW_ERROR_DETAILS**: Exibir detalhes de erro

### **Funcionalidades Futuras**
- Interface web para controle de debug
- Logs em tempo real
- Métricas de performance
- Configurações dinâmicas

## Próximos Passos

Com o Flask configurado, estamos prontos para:

1. **Conexão com Elasticsearch** (Fase 1 - Item 3)
2. **Criação de rotas básicas** (Fase 1 - Item 4)
3. **Configuração da OpenAI** (Fase 1 - Item 5)
4. **Sistema de autenticação** (Fase 1 - Item 6)

---

**Status**: ✅ Flask configurado com todas as extensões necessárias!
**Próximo**: Conexão com Elasticsearch 