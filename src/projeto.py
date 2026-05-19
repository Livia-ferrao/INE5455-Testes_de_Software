from ocorrencia import Ocorrencia


class Projeto:
    def __init__(self, nome):
        if not nome or not str(nome).strip():
            raise ValueError("O nome não pode ser vazio ou nulo.")

        self.__nome = nome.strip()
        self.__funcionarios = []
        self.__ocorrencias = []

    @property
    def nome(self):
        return self.__nome

    @property
    def funcionarios(self):
        return list(self.__funcionarios)
    
    @property
    def ocorrencias(self):
        return list(self.__ocorrencias)

    def adicionar_funcionario(self, funcionario):
        if not funcionario:
            raise ValueError("O funcionário não pode ser nulo.")
        if funcionario in self.__funcionarios:
            raise ValueError("Funcionário já está na lista.")

        self.__funcionarios.append(funcionario)
        
    def adicionar_ocorrencia(self, ocorrencia: Ocorrencia):
        if not ocorrencia:
            raise ValueError("A ocorrência não pode ser nula.")
        if ocorrencia in self.__ocorrencias:
            raise ValueError("Ocorrência já está na lista.")
            
        if ocorrencia.responsavel not in self.funcionarios:
            raise ValueError("O funcionário responsável pela ocorrência deve estar cadastrado no projeto.")

        self.__ocorrencias.append(ocorrencia)
