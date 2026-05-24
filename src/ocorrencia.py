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

    def fechar(self):
        if self.__estado == Estado.FECHADA:
            raise ValueError("A ocorrência já está fechada.")
        self.__estado = Estado.FECHADA

    def alterar_prioridade(self, nova_prioridade):
        if nova_prioridade is None:
            raise ValueError("A nova prioridade não pode ser nula.")

        if self.__estado == Estado.FECHADA:
            raise ValueError("Não é possível alterar a prioridade de uma ocorrência fechada.")

        self.__prioridade = nova_prioridade
    
    def alterar_responsavel(self, novo_responsavel):
        if novo_responsavel is None:
            raise ValueError("O novo responsável não pode ser nulo.")

        if self.__estado == Estado.FECHADA:
            raise ValueError("Não é possível alterar o responsável de uma ocorrência fechada.")
        
        if novo_responsavel == self.__responsavel:
            raise ValueError("O novo responsável deve ser diferente do atual.")

        self.__responsavel = novo_responsavel