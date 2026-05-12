import unittest
from empresa import Empresa

class TestEmpresa(unittest.TestCase):
    def test_criar_empresa_com_nome_valido(self):
        nome = "W"
        empresa = Empresa(nome)
        self.assertEqual(empresa.nome, nome)
        
    def test_criar_empresa_sem_funcionarios(self):
        empresa = Empresa("W")
        self.assertEqual(len(empresa.funcionarios), 0)

    def test_criar_empresa_sem_projetos(self):
        empresa = Empresa("W")
        self.assertEqual(len(empresa.projetos), 0)
