import unittest
from funcionario import Funcionario

class TestFuncionario(unittest.TestCase):
    def test_criar_funcionario_com_nome_valido(self):
        nome = "José"
        func = Funcionario(nome)
        self.assertEqual(nome, func.nome)
        
    def test_criar_funcionario_sem_projetos(self):
        self.assertEqual(0, len(self.__funcionario.projetos))