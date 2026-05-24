from enums import Estado, Prioridade, TipoOcorrencia
from funcionario import Funcionario

class Ocorrencia:
    def __init__(self, chave: str, resumo: str, responsavel: Funcionario, prioridade: Prioridade, tipo: TipoOcorrencia):
        if not chave:
            raise ValueError("A chave não pode ser vazia ou nula.")
        
        if not resumo:
            raise ValueError("O resumo não pode ser vazio ou nulo.")
        
        if not responsavel:
            raise ValueError("O responsavel não pode ser vazio ou nulo.")
        
        if not prioridade:
            raise ValueError("A prioridade não pode ser vazia ou nula.")
        
        if not tipo:
            raise ValueError("O tipo não pode ser vazio ou nulo.")

        self.__chave = chave
        self.__resumo = resumo
        self.__responsavel = responsavel
        self.__prioridade = prioridade
        self.__tipo = tipo
        self.__estado = Estado.ABERTA

    @property
    def chave(self):
        return self.__chave

    @property
    def resumo(self):
        return self.__resumo
    
    @property
    def responsavel(self):
        return self.__responsavel
    
    @property
    def prioridade(self):
        return self.__prioridade
    
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def estado(self):
        return self.__estado

    def esta_aberta(self):
        return self.__estado == Estado.ABERTA

    def esta_fechada(self):
        return self.__estado == Estado.FECHADA

    def fechar(self):
        if self.esta_fechada():
            raise ValueError("A ocorrência já está fechada.")
        self.__estado = Estado.FECHADA

    def alterar_prioridade(self, nova_prioridade):
        if nova_prioridade is None:
            raise ValueError("A nova prioridade não pode ser nula.")

        if self.esta_fechada():
            raise ValueError("Não é possível alterar a prioridade de uma ocorrência fechada.")

        self.__prioridade = nova_prioridade