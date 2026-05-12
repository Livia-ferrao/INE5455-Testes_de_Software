import unittest
from empresa import Empresa

class TestEmpresa(unittest.TestCase):
    def setUp(self):
        self.__empresa = Empresa("W")

    def test_criar_empresa_com_nome_valido(self):
        self.assertEqual(self.__empresa.nome, "W")
        
    def test_criar_empresa_sem_funcionarios(self):
        self.assertEqual(len(self.__empresa.funcionarios), 0)

    def test_criar_empresa_sem_projetos(self):
        self.assertEqual(len(self.__empresa.projetos), 0)
