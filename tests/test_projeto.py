import unittest
from projeto import Projeto

class TestProjeto(unittest.TestCase):
    def setUp(self):
        self.__projeto = Projeto("INE5455")

    def test_criar_projeto_com_nome_valido(self):
        self.assertEqual("INE5455", self.__projeto.nome)
        
    def test_criar_projeto_sem_funcionarios(self):
        self.assertEqual(0, len(self.__projeto.funcionarios))
