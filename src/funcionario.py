class Funcionario:
    def __init__(self, nome):
        if not nome or not str(nome).strip():
            raise ValueError("O nome não pode ser vazio ou nulo.")

        self.__nome = nome.strip()
        self.__projetos = []

    @property
    def nome(self):
        return self.__nome

    @property
    def projetos(self):
        return list(self.__projetos)

    def adicionar_projeto(self, projeto):
        if not projeto:
            raise ValueError("O projeto não pode ser nulo.")
        if projeto in self.__projetos:
            raise ValueError("Projeto já está na lista.")

        self.__projetos.append(projeto)
