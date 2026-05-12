class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
        self.projetos = []
        
    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)