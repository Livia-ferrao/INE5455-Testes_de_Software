import unittest
from empresa import Empresa
from funcionario import Funcionario

class TestEmpresa(unittest.TestCase):
    def setUp(self):
        self.__empresa = Empresa("W")

    def test_criar_empresa_com_nome_valido(self):
        self.assertEqual("W", self.__empresa.nome)
        
    def test_criar_empresa_sem_funcionarios(self):
        self.assertEqual(0, len(self.__empresa.funcionarios))

    def test_criar_empresa_sem_projetos(self):
        self.assertEqual(0, len(self.__empresa.projetos))
        
    def test_adicionar_funcionario_na_empresa(self):
        funcionario = Funcionario("José")
        self.__empresa.adicionar_funcionario(funcionario)
        self.assertEqual(1, len(self.__empresa.funcionarios))
        self.assertIn(funcionario, self.__empresa.funcionarios)
