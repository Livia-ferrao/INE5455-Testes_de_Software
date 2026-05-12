class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
        
    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)