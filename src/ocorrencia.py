from enums import Estado, Prioridade, Tipo
from funcionario import Funcionario

class Ocorrencia:
    def __init__(self, chave: str, resumo: str, responsavel: Funcionario, prioridade: Prioridade, tipo: Tipo):
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
        self.__status = Estado.ABERTO

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
    def status(self):
        return self.__status