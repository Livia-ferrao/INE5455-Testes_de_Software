from enum import Enum

class Estado(Enum):
    ABERTA = "aberta"
    FECHADA = "fechada"

class Prioridade(Enum):
    BAIXA = "baixa"
    MEDIA = "media"
    ALTA = "alta"

class TipoOcorrencia(Enum):
    TAREFA = "tarefa"
    BUG = "bug"
    REFATORACAO = "refatoracao"