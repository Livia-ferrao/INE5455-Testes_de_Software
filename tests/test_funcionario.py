import unittest
from funcionario import Funcionario
from projeto import Projeto

class TestFuncionario(unittest.TestCase):
    def setUp(self):
        self.__funcionario = Funcionario("José")

    def test_criar_funcionario_com_nome_valido(self):
        self.assertEqual("José", self.__funcionario.nome)
        
    def test_criar_funcionario_sem_projetos(self):
        self.assertEqual(0, len(self.__funcionario.projetos))
        
    def test_adicionar_projeto_no_funcionario(self):
        projeto = Projeto("INE5429")
        self.__funcionario.adicionar_projeto(projeto)

        self.assertEqual(1, len(self.__funcionario.projetos))
        self.assertIn(projeto, self.__funcionario.projetos)
    