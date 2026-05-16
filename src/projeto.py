class Projeto:
    def __init__(self, nome):
        self.__nome = nome
        self.__funcionarios = []

    @property
    def nome(self):
        return self.__nome

    @property
    def funcionarios(self):
        return list(self.__funcionarios)

    def adicionar_funcionario(self, funcionario):
        if not funcionario:
            raise ValueError("O funcionário não pode ser nulo.")
        if funcionario in self.__funcionarios:
            raise ValueError("Funcionário já está na lista.")

        self.__funcionarios.append(funcionario)
