class Ocorrencia:
    def __init__(self, chave, resumo):
        self.__chave = chave
        self.__resumo = resumo

    @property
    def chave(self):
        return self.__chave

    @property
    def resumo(self):
        return self.__resumo