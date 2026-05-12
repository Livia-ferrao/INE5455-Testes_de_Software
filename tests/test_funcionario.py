import unittest
from funcionario import Funcionario

class TestFuncionario(unittest.TestCase):
    def setUp(self):
        self.__funcionario = Funcionario("José")

    def test_criar_funcionario_com_nome_valido(self):
        self.assertEqual("José", self.__funcionario.nome)
        
    def test_criar_funcionario_sem_projetos(self):
        self.assertEqual(0, len(self.__funcionario.projetos))