import unittest
from projeto import Projeto
from funcionario import Funcionario

class TestProjeto(unittest.TestCase):
    def setUp(self):
        self.__projeto = Projeto("INE5455")

    def test_criar_projeto_com_nome_valido(self):
        self.assertEqual("INE5455", self.__projeto.nome)
        
    def test_criar_projeto_sem_funcionarios(self):
        self.assertEqual(0, len(self.__projeto.funcionarios))

    def test_adicionar_funcionario_no_projeto(self):
        funcionario = Funcionario("José")
        self.__projeto.adicionar_funcionario(funcionario)

        self.assertEqual(1, len(self.__projeto.funcionarios))
        self.assertIn(funcionario, self.__projeto.funcionarios)
        
    def test_adicionar_multiplos_funcionarios_no_projeto(self):
        funcionario1 = Funcionario("José")
        funcionario2 = Funcionario("Maria")

        self.__projeto.adicionar_funcionario(funcionario1)
        self.__projeto.adicionar_funcionario(funcionario2)

        self.assertEqual(2, len(self.__projeto.funcionarios))
        self.assertIn(funcionario1, self.__projeto.funcionarios)
        self.assertIn(funcionario2, self.__projeto.funcionarios)