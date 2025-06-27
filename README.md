# Professor DUTRA - Hub de Legislação de Trânsito

A primeira IA especialista em legislação de trânsito brasileira.

## Sobre o Projeto

O Professor DUTRA é um sistema inteligente de busca e consulta de legislação de trânsito brasileira, desenvolvido com tecnologias modernas para oferecer uma experiência única e eficiente.

## Tecnologias Utilizadas

- **Backend**: Python + Flask
- **Banco de Dados**: Elasticsearch (busca semântica e vetorial)
- **IA**: OpenAI GPT (processamento de linguagem natural)
- **Frontend**: HTML, CSS, JavaScript
- **Deploy**: Google Cloud Platform

## Estrutura do Projeto

```
dutra-ia/
├── app/                    # Código principal da aplicação
│   ├── models/            # Modelos de dados
│   ├── routes/            # Rotas da aplicação
│   ├── services/          # Lógica de negócio
│   ├── utils/             # Funções utilitárias
│   └── static/            # Arquivos estáticos
├── templates/             # Templates HTML
├── tests/                 # Testes automatizados
├── scripts/               # Scripts utilitários
├── docs/                  # Documentação
├── requirements.txt       # Dependências Python
├── app.py                # Aplicação Flask principal
├── .env                  # Variáveis de ambiente
└── README.md             # Este arquivo
```

## Instalação e Configuração

### Pré-requisitos

- Python 3.8+
- Elasticsearch 8.x
- Conta OpenAI (API Key)

### Passos para Instalação

1. **Clone o repositório**
   ```bash
   git clone [url-do-repositorio]
   cd dutra-ia
   ```

2. **Crie um ambiente virtual**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente**
   - Crie o arquivo `.env` com suas configurações:
   ```
   ELASTICSEARCH_HOST=seu-host-elasticsearch
   ELASTICSEARCH_PORT=443
   ELASTICSEARCH_API_KEY=sua-api-key-elasticsearch
   OPENAI_API_KEY=sua-api-key-openai
   ```

5. **Execute a aplicação**
   ```bash
   python app.py
   ```

## Status do Desenvolvimento

### ✅ FASE 1 - FUNDAÇÃO E ESTRUTURA BASE (COMPLETA)

1. **✅ Estrutura de diretórios** - Criada com organização profissional
2. **✅ Configuração Flask** - Aplicação básica funcionando
3. **✅ Conexão Elasticsearch** - Testada e funcionando
4. **✅ Rotas básicas** - Endpoints de teste criados
5. **✅ Integração OpenAI** - Testada e funcionando

### 🚧 FASE 2 - SISTEMA DE BUSCA INTELIGENTE (PRÓXIMA)

1. **Sistema de busca básico** (Elasticsearch + OpenAI)
2. **Interface web simples** (HTML/CSS)
3. **Autenticação básica**
4. **Testes de funcionalidade**

### 📋 FASE 3 - SISTEMA DE USUÁRIOS E AUTENTICAÇÃO
### 📊 FASE 4 - DASHBOARD ADMINISTRATIVO
### 🎨 FASE 5 - DASHBOARD DO CLIENTE
### 🚀 FASE 6 - DEPLOY E OTIMIZAÇÃO

## Testes de Funcionalidade

### Testar Elasticsearch
```bash
curl http://localhost:5000/test-elastic
```

### Testar OpenAI
```bash
curl http://localhost:5000/test-openai
```

## Funcionalidades

### Para Administradores
- Dashboard completo com métricas
- Gerenciamento de usuários
- Configurações do sistema
- Relatórios e análises

### Para Clientes
- Busca inteligente na legislação
- Interface intuitiva e responsiva
- Histórico de consultas
- Favoritos e personalização

## Desenvolvimento

### Estrutura de Fases

1. **Fase 1**: Fundação e Estrutura Base ✅
2. **Fase 2**: Sistema de Busca Inteligente 🚧
3. **Fase 3**: Sistema de Usuários e Autenticação
4. **Fase 4**: Dashboard Administrativo
5. **Fase 5**: Dashboard do Cliente
6. **Fase 6**: Deploy e Otimização

### Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Contato

Para dúvidas ou sugestões, entre em contato através do email: [seu-email@exemplo.com]

---

**Professor DUTRA** - Revolucionando a consulta de legislação de trânsito brasileira! 🚗📚 