class Empresa:
    def __init__(self, nome):
        self.__nome = nome
        self.__funcionarios = []
        self.__projetos = []

    @property
    def nome(self):
        return self.__nome

    @property
    def funcionarios(self):
        return list(self.__funcionarios)

    @property
    def projetos(self):
        return list(self.__projetos)

    def adicionar_funcionario(self, funcionario):
        if not funcionario:
            raise ValueError("O funcionário não pode ser nulo.")
        if funcionario in self.__funcionarios:
            raise ValueError("Funcionário já está na lista.")

        self.__funcionarios.append(funcionario)

    def adicionar_projeto(self, projeto):
        if not projeto:
            raise ValueError("O projeto não pode ser nulo.")
        if projeto in self.__projetos:
            raise ValueError("Projeto já está na lista.")

        self.__projetos.append(projeto)

    def vincular_funcionario_projeto(self, funcionario, projeto):
        if funcionario not in self.__funcionarios:
            raise ValueError("Funcionário não pertence a esta empresa.")
        if projeto not in self.__projetos:
            raise ValueError("Projeto não pertence a esta empresa")

        projeto.adicionar_funcionario(funcionario)
        funcionario.adicionar_projeto(projeto)
