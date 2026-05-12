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
        
    def adicionar_projeto(self, projeto):
        if not projeto:
            raise ValueError("O projeto não pode ser nulo.")
        if projeto in self.projetos:
            raise ValueError("Projeto já está na lista.")

        self.projetos.append(projeto)