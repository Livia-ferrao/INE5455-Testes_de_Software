import unittest
from ocorrencia import Ocorrencia
from funcionario import Funcionario
from enums import Prioridade, Tipo, Estado

class TestOcorrencia(unittest.TestCase):
    def setUp(self):
        self.__jose = Funcionario("José")
        self.__ocorrencia = Ocorrencia(
            chave="ID1",
            resumo="Ocorrencia referente ao ID1",
            responsavel=self.__jose,
            prioridade=Prioridade.ALTA,
            tipo=Tipo.BUG,
        )

    def test_cria_ocorrencia_valida(self):
        self.assertEqual("ID1", self.__ocorrencia.chave)
        self.assertEqual("Ocorrencia referente ao ID1", self.__ocorrencia.resumo)
        self.assertEqual(self.__jose, self.__ocorrencia.responsavel)
        self.assertEqual(Prioridade.ALTA, self.__ocorrencia.prioridade)
        self.assertEqual(Tipo.BUG, self.__ocorrencia.tipo)
        self.assertEqual(Estado.ABERTO, self.__ocorrencia.status)

    def test_nao_cria_ocorrencia_com_chave_vazia(self):
        with self.assertRaises(ValueError):
            Ocorrencia(chave="", resumo="Nao vazio", responsavel=self.__jose, prioridade=Prioridade.BAIXA, tipo=Tipo.BUG)

    def test_nao_cria_ocorrencia_com_resumo_vazio(self):
        with self.assertRaises(ValueError):
            Ocorrencia(chave="ID0", resumo="", responsavel=self.__jose, prioridade=Prioridade.BAIXA, tipo=Tipo.BUG)

    def test_nao_cria_ocorrencia_com_responsavel_vazio(self):
        with self.assertRaises(ValueError):
            Ocorrencia(chave="ID0", resumo="Nao vazio", responsavel=None, prioridade=Prioridade.BAIXA, tipo=Tipo.BUG)

    def test_nao_cria_ocorrencia_com_prioridade_vazia(self):
          with self.assertRaises(ValueError):
            Ocorrencia(chave="ID0", resumo="Nao vazio", responsavel=self.__jose, prioridade=None, tipo=Tipo.BUG)

    def test_nao_cria_ocorrencia_com_tipo_vazio(self):
        with self.assertRaises(ValueError):
            Ocorrencia(chave="ID0", resumo="Nao vazio", responsavel=self.__jose, prioridade=Prioridade.BAIXA, tipo=None)

    def test_fechar_ocorrencia(self):
        self.__ocorrencia.fechar_ocorrencia()
        self.assertEqual(Estado.FECHADO, self.__ocorrencia.status)