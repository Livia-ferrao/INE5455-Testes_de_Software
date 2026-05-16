import unittest
from funcionario import Funcionario
from projeto import Projeto

class TestFuncionario(unittest.TestCase):
    def setUp(self):
        self.__funcionario = Funcionario("José")

    def test_criar_funcionario_com_nome_valido(self):
        self.assertEqual("José", self.__funcionario.nome)

    def test_nao_criar_funcionario_com_nome_vazio(self):
        with self.assertRaises(ValueError):
            Funcionario("")

    def test_criar_funcionario_sem_projetos(self):
        self.assertEqual(0, len(self.__funcionario.projetos))
        
    def test_adicionar_projeto_no_funcionario(self):
        projeto = Projeto("INE5429")
        self.__funcionario.adicionar_projeto(projeto)

        self.assertEqual(1, len(self.__funcionario.projetos))
        self.assertIn(projeto, self.__funcionario.projetos)
    
    def test_adicionar_multiplos_projetos_no_funcionario(self):
        projeto1 = Projeto("INE5429")
        projeto2 = Projeto("INE5455")

        self.__funcionario.adicionar_projeto(projeto1)
        self.__funcionario.adicionar_projeto(projeto2)

        self.assertEqual(2, len(self.__funcionario.projetos))
        self.assertIn(projeto1, self.__funcionario.projetos)
        self.assertIn(projeto2, self.__funcionario.projetos)

    def test_nao_adicionar_projeto_nulo_no_funcionario(self):
        with self.assertRaises(ValueError):
            self.__funcionario.adicionar_projeto(None)
            
    def test_nao_adicionar_projeto_duplicado_no_funcionario(self):
        projeto = Projeto("INE5455")
        
        self.__funcionario.adicionar_projeto(projeto)
        
        with self.assertRaises(ValueError):
            self.__funcionario.adicionar_projeto(projeto)