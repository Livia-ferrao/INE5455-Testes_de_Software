from ocorrencia import Ocorrencia
from enums import Prioridade, TipoOcorrencia

def criar_n_ocorrencias(funcionario, projeto, quantidade):
    for i in range(quantidade):
        ocorrencia = Ocorrencia(
            chave=f"BUG_{i}",
            resumo=f"Erro {i}",
            responsavel=funcionario,
            prioridade=Prioridade.ALTA,
            tipo=TipoOcorrencia.BUG
        )
        projeto.adicionar_ocorrencia(ocorrencia)