"""
Modelo para gerenciamento de médicos no sistema.
Fornece funcionalidades para criar, ler, atualizar e deletar médicos no banco de dados.
"""

from models.database import Database

class Medico:
    """
    Classe para gerenciar os médicos no sistema.
    Implementa operações CRUD (Create, Read, Update, Delete) para médicos.
    """
    
    def __init__(self):
        """
        Inicializa a classe Medico com uma conexão ao banco de dados.
        """
        self.db = Database()
    
    def listar_todos(self):
        """
        Lista todos os médicos cadastrados no sistema.
   
        """
        query = "SELECT * FROM medicos ORDER BY nome ASC"
        return self.db.execute_query(query)

    
    def buscar_por_id(self, medico_id):
        """
        Busca um médico pelo seu ID.
        
        """
        query = "SELECT * FROM medicos WHERE id = %s"
        return self.db.execute_single(query, (medico_id,))
    
    def buscar_por_especialidade(self, especialidade):
        """
        Busca médicos por especialidade.
        
        """
        query = "SELECT id, nome FROM medicos WHERE especialidade = %s"
        return self.db.execute_query(query, (especialidade,))
    
    def listar_especialidades(self):
        """
        Lista todas as especialidades médicas disponíveis.
        
        """
        query = "SELECT DISTINCT especialidade as nome FROM medicos"
        return self.db.execute_query(query)
    
    def obter_dias_atendimento(self, medico_id):
        """
        Obtém os dias de atendimento de um médico.
        
        """
        query = "SELECT dias_atendimento FROM medicos WHERE id = %s"
        resultado = self.db.execute_single(query, (medico_id,))
        if not resultado:
            return []
        return resultado['dias_atendimento'].split(',') if resultado['dias_atendimento'] else []
    
    def obter_horarios_atendimento(self, medico_id):
        """
        Obtém os horários de atendimento de um médico.
        
        """
        query = "SELECT horarios_atendimento FROM medicos WHERE id = %s"
        resultado = self.db.execute_single(query, (medico_id,))
        if not resultado:
            return []
        return resultado['horarios_atendimento'].split(',') if resultado['horarios_atendimento'] else []
    
    def cadastrar(self, nome, crm, especialidade, dias, horarios):
        """
        Cadastra um novo médico no sistema.
        
        """
        dias_str = ",".join(dias)
        horarios_str = ",".join(horarios)
        
        query = """
            INSERT INTO medicos (nome, CRM, especialidade, dias_atendimento, horarios_atendimento)
            VALUES (%s, %s, %s, %s, %s)
        """
        return self.db.execute_non_query(query, (nome, crm, especialidade, dias_str, horarios_str))
    
    def atualizar(self, medico_id, dias, horarios):
        """
        Atualiza os dias e horários de atendimento de um médico.
        
        """
        dias_str = ",".join(dias)
        horarios_str = ",".join(horarios)
        
        query = """
            UPDATE medicos
            SET dias_atendimento = %s,
                horarios_atendimento = %s
            WHERE id = %s
        """
        return self.db.execute_non_query(query, (dias_str, horarios_str, medico_id))
    
    def deletar(self, medico_id):
        """
        Deleta um médico do sistema.
        
        """
        # Primeiro, deletar agendamentos vinculados para manter integridade referencial
        query_agendamentos = "DELETE FROM agendamentos WHERE medico_id = %s"
        self.db.execute_non_query(query_agendamentos, (medico_id,))
        
        # Depois, deletar o médico
        query_medico = "DELETE FROM medicos WHERE id = %s"
        return self.db.execute_non_query(query_medico, (medico_id,))
