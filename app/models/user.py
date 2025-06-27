# Professor DUTRA - Modelo de Usuário
# Modelo básico para autenticação com Flask-Login

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager

class User(UserMixin, db.Model):
    """Modelo de usuário para autenticação"""
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    user_type = db.Column(db.String(20), default='client')  # 'admin' ou 'client'
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    def __init__(self, username, email, name, password, user_type='client'):
        self.username = username
        self.email = email
        self.name = name
        self.password_hash = generate_password_hash(password)
        self.user_type = user_type
    
    def set_password(self, password):
        """Define a senha do usuário"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Verifica se a senha está correta"""
        return check_password_hash(self.password_hash, password)
    
    def is_admin(self):
        """Verifica se o usuário é administrador"""
        return self.user_type == 'admin'
    
    def __repr__(self):
        return f'<User {self.username}>'

@login_manager.user_loader
def load_user(user_id):
    """Função necessária para o Flask-Login carregar usuários"""
    return User.query.get(int(user_id)) 