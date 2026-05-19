class Ocorrencia:
    def __init__(self, chave, resumo):
        if not chave:
            raise ValueError("A chave não pode ser vazia ou nula.")

        self.__chave = chave
        self.__resumo = resumo

    @property
    def chave(self):
        return self.__chave

    @property
    def resumo(self):
        return self.__resumo