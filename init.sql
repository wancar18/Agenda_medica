-- Tabela de médicos
CREATE TABLE IF NOT EXISTS medicos (
                                       id INT AUTO_INCREMENT PRIMARY KEY,
                                       nome VARCHAR(100) NOT NULL,
    CRM VARCHAR(20) NOT NULL,
    especialidade VARCHAR(100) NOT NULL,
    dias_atendimento TEXT,
    horarios_atendimento TEXT
    );

-- Tabela de agendamentos
CREATE TABLE IF NOT EXISTS agendamentos (
                                            id INT AUTO_INCREMENT PRIMARY KEY,
                                            nome_paciente VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) NOT NULL,
    especialidade VARCHAR(100) NOT NULL,
    medico_id INT NOT NULL,
    dia VARCHAR(20) NOT NULL,
    hora VARCHAR(10) NOT NULL,
    FOREIGN KEY (medico_id) REFERENCES medicos(id)
    );

-- Inserir médicos de exemplo
INSERT INTO medicos (nome, CRM, especialidade, dias_atendimento, horarios_atendimento) VALUES
                                                                                           ('Dr. Carlos Silva', '12345-SP', 'Cardiologia', 'Segunda-feira,Quarta-feira,Sexta-feira', '08:00,09:00,10:00,11:00,14:00,15:00,16:00'),
                                                                                           ('Dra. Ana Oliveira', '23456-SP', 'Pediatria', 'Segunda-feira,Terça-feira,Quinta-feira', '08:30,09:30,10:30,14:30,15:30,16:30'),
                                                                                           ('Dr. Roberto Santos', '34567-SP', 'Ortopedia', 'Terça-feira,Quinta-feira,Sábado', '07:00,08:00,09:00,10:00,11:00'),
                                                                                           ('Dra. Juliana Costa', '45678-SP', 'Dermatologia', 'Segunda-feira,Quarta-feira,Sexta-feira', '13:00,14:00,15:00,16:00,17:00'),
                                                                                           ('Dr. Marcelo Lima', '56789-SP', 'Clínica Geral', 'Segunda-feira,Terça-feira,Quarta-feira,Quinta-feira,Sexta-feira', '08:00,09:00,10:00,11:00,14:00,15:00,16:00,17:00');

-- Inserir agendamentos de exemplo
INSERT INTO agendamentos (nome_paciente, cpf, especialidade, medico_id, dia, hora) VALUES
                                                                                       ('João Pereira', '12345678901', 'Cardiologia', 1, 'Segunda-feira', '09:00'),
                                                                                       ('Maria Souza', '23456789012', 'Pediatria', 2, 'Terça-feira', '09:30'),
                                                                                       ('Pedro Almeida', '34567890123', 'Ortopedia', 3, 'Quinta-feira', '10:00'),
                                                                                       ('Fernanda Gomes', '45678901234', 'Dermatologia', 4, 'Quarta-feira', '14:00'),
                                                                                       ('Ricardo Martins', '56789012345', 'Clínica Geral', 5, 'Sexta-feira', '15:00');