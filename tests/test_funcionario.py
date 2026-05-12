import unittest
from funcionario import Funcionario

class TestFuncionario(unittest.TestCase):
    def test_criar_funcionario_com_nome_valido(self):
        nome = "José"
        func = Funcionario(nome)
        self.assertEqual(func.nome, nome)