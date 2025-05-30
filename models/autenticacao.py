"""
Módulo de autenticação para o sistema de agendamento médico.
Fornece funcionalidades para gerenciar o login e sessão de usuários.
"""

from config.config import USUARIO_ADMIN, SENHA_ADMIN

class Autenticacao:
    """
    Classe para gerenciar a autenticação de usuários no sistema.
    """
    
    @staticmethod
    def verificar_credenciais(usuario, senha):
        """
        Verifica se as credenciais fornecidas são válidas.

        """
        return usuario == USUARIO_ADMIN and senha == SENHA_ADMIN
