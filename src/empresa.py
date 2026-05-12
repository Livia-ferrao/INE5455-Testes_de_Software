class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
        self.projetos = []
        
    def adicionar_funcionario(self, funcionario):
        if not funcionario:
            raise ValueError("O funcionário não pode ser nulo.")
        if funcionario in self.funcionarios:
            raise ValueError("Funcionário já está na lista.")

        self.funcionarios.append(funcionario)