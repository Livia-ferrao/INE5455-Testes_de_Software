import unittest
from projeto import Projeto

class TestProjeto(unittest.TestCase):
    def test_criar_projeto_com_nome_valido(self):
        nome = "INE5455"
        projeto = Projeto(nome)
        self.assertEqual(nome, projeto.nome)