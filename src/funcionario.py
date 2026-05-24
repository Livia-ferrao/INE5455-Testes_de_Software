class Funcionario:
    def __init__(self, nome):
        if not nome or not str(nome).strip():
            raise ValueError("O nome não pode ser vazio ou nulo.")

        self.__nome = nome.strip()
        self.__projetos = []
        self.__limite_ocorrencias_abertas = 10

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

    def total_ocorrencias_abertas(self):
        total = 0

        for projeto in self.__projetos:
            for ocorrencia in projeto.ocorrencias:
                if ocorrencia.responsavel == self and ocorrencia.esta_aberta():
                    total += 1

        return total

    def atingiu_limite_ocorrencias(self):
        return self.total_ocorrencias_abertas() >= self.__limite_ocorrencias_abertas
