import unittest
from funcionario import Funcionario
from projeto import Projeto
from ocorrencia import Ocorrencia
from enums import Prioridade, TipoOcorrencia

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
            
    def test_total_ocorrencias_abertas_funcionario(self):
        projeto = Projeto("INE5455")
        projeto.adicionar_funcionario(self.__funcionario)
        self.__funcionario.adicionar_projeto(projeto)

        ocorrencia1 = Ocorrencia(chave="BUG_001", resumo="Erro login", responsavel=self.__funcionario, prioridade=Prioridade.ALTA, tipo=TipoOcorrencia.BUG)
        ocorrencia2 = Ocorrencia(chave="TASK_001", resumo="Criar tela", responsavel=self.__funcionario, prioridade=Prioridade.MEDIA, tipo=TipoOcorrencia.TAREFA)

        projeto.adicionar_ocorrencia(ocorrencia1)
        projeto.adicionar_ocorrencia(ocorrencia2)

        self.assertEqual(2, self.__funcionario.total_ocorrencias_abertas())
        
    def test_nao_contar_ocorrencias_fechadas(self):
        projeto = Projeto("INE5455")
        projeto.adicionar_funcionario(self.__funcionario)
        self.__funcionario.adicionar_projeto(projeto)

        ocorrencia = Ocorrencia(chave="BUG_001", resumo="Erro login", responsavel=self.__funcionario, prioridade=Prioridade.ALTA, tipo=TipoOcorrencia.BUG)
        projeto.adicionar_ocorrencia(ocorrencia)
        ocorrencia.fechar()

        self.assertEqual(0, self.__funcionario.total_ocorrencias_abertas())
        
    
    def test_funcionario_atingiu_limite_ocorrencias(self):
        projeto = Projeto("INE5455")
        projeto.adicionar_funcionario(self.__funcionario)
        self.__funcionario.adicionar_projeto(projeto)
        _criar_n_ocorrencias(self.__funcionario, projeto, 10)
    
        self.assertTrue(self.__funcionario.atingiu_limite_ocorrencias())

    def test_funcionario_nao_atingiu_limite_ocorrencias(self):
        projeto = Projeto("INE5455")
        projeto.adicionar_funcionario(self.__funcionario)
        self.__funcionario.adicionar_projeto(projeto)
        _criar_n_ocorrencias(self.__funcionario, projeto, 6)

        self.assertFalse(self.__funcionario.atingiu_limite_ocorrencias())


def _criar_n_ocorrencias(funcionario, projeto, quantidade):
    for i in range(quantidade):
        ocorrencia = Ocorrencia(
            chave=f"BUG_{i}",
            resumo=f"Erro {i}",
            responsavel=funcionario,
            prioridade=Prioridade.ALTA,
            tipo=TipoOcorrencia.BUG
        )
        projeto.adicionar_ocorrencia(ocorrencia)