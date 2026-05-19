from enum import Enum

class Estado(Enum):
    ABERTO = "aberto"
    FECHADO = "fechado"

class Prioridade(Enum):
    BAIXA = "baixa"
    MEDIA = "media"
    ALTA = "alta"

class Tipo(Enum):
    TAREFA = "tarefa"
    BUG = "bug"
    REFATORACAO = "refatoracao"