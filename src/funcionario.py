class Funcionario:
    def __init__(self, nome):
        self.nome = nome
        self.projetos = []
        
    def adicionar_projeto(self, projeto):
        if not projeto:
            raise ValueError("O projeto não pode ser nulo.")
        if projeto in self.projetos:
            raise ValueError("Projeto já está na lista.")

        self.projetos.append(projeto)