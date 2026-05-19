import unittest
from ocorrencia import Ocorrencia


class TestEmpresa(unittest.TestCase):
    def setUp(self):
        self.__ocorrencia = Ocorrencia(chave="ID1", resumo="Ocorrencia referente ao ID1")

    def test_cria_ocorrencia_com_chave_e_resumo(self):
        self.assertEqual("ID1", self.__ocorrencia.chave)
        self.assertEqual("Ocorrencia referente ao ID1", self.__ocorrencia.resumo)