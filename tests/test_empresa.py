import unittest
from empresa import Empresa

class TestEmpresa(unittest.TestCase):
    def test_criar_empresa_com_nome_valido(self):
        nome = "W"
        empresa = Empresa(nome)
        self.assertEqual(empresa.nome, nome)
        
