"""
Arquivo de configuração do sistema de agendamento médico.
Contém constantes e configurações globais utilizadas em todo o sistema.
"""
import os
# Configurações do Flask
SECRET_KEY = 'chavesecreta123'  # Chave secreta para gerenciamento de sessão

# Configurações do banco de dados
DB_CONFIG = {
    'host': os.environ.get('DB_HOST'),
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
    'database': os.environ.get('DB_NAME')
}

# Credenciais de acesso ao sistema administrativo
USUARIO_ADMIN = 'admin'
SENHA_ADMIN = '123'

# Constantes do sistema
DIAS_DA_SEMANA = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']
