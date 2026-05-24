import unittest
from projeto import Projeto
from funcionario import Funcionario
from ocorrencia import Ocorrencia
from enums import Prioridade, TipoOcorrencia
from helpers import criar_n_ocorrencias


class TestProjeto(unittest.TestCase):
    def setUp(self):
        self.__projeto = Projeto("INE5455")

    def test_criar_projeto_com_nome_valido(self):
        self.assertEqual("INE5455", self.__projeto.nome)

    def test_nao_criar_projeto_com_nome_vazio(self):
        with self.assertRaises(ValueError):
            Projeto("")

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

    def test_nao_adicionar_funcionario_nulo_no_projeto(self):
        with self.assertRaises(ValueError):
            self.__projeto.adicionar_funcionario(None)

    def test_nao_adicionar_funcionario_duplicado_no_projeto(self):
        funcionario = Funcionario("José")

        self.__projeto.adicionar_funcionario(funcionario)

        with self.assertRaises(ValueError):
            self.__projeto.adicionar_funcionario(funcionario)

    def test_criar_projeto_sem_ocorrencias(self):
        self.assertEqual(0, len(self.__projeto.ocorrencias))
    
    def test_adicionar_ocorrencia_ao_projeto(self):
        jose = Funcionario("José")
        self.__projeto.adicionar_funcionario(jose)

        ocorrencia_bug_login = Ocorrencia(chave="BUG_001", resumo="Erro ao realizar login",  responsavel=jose, prioridade=Prioridade.MEDIA, tipo=TipoOcorrencia.BUG)
        self.__projeto.adicionar_ocorrencia(ocorrencia_bug_login)

        self.assertEqual(1, len(self.__projeto.ocorrencias))
        self.assertIn(ocorrencia_bug_login, self.__projeto.ocorrencias)
        
    def test_adicionar_multiplas_ocorrencias_no_projeto(self):
        jose = Funcionario("José")
        self.__projeto.adicionar_funcionario(jose)

        ocorrencia_bug_login = Ocorrencia(chave="BUG_001", resumo="Erro ao realizar login", responsavel=jose, prioridade=Prioridade.MEDIA, tipo=TipoOcorrencia.BUG)
        ocorrencia_tarefa_emails = Ocorrencia(chave="TASK_001", resumo="Configurar envio de emails", responsavel=jose, prioridade=Prioridade.ALTA, tipo=TipoOcorrencia.TAREFA)
        ocorrencia_refatoracao_excecoes = Ocorrencia(chave="REF_001", resumo="Padronizar exceções", responsavel=jose, prioridade=Prioridade.BAIXA, tipo=TipoOcorrencia.REFATORACAO)
        ocorrencia_data_incorreta = Ocorrencia(chave="BUG_002", resumo="Data aparece em formato incorreto", responsavel=jose, prioridade=Prioridade.MEDIA, tipo=TipoOcorrencia.BUG)

        self.__projeto.adicionar_ocorrencia(ocorrencia_bug_login)
        self.__projeto.adicionar_ocorrencia(ocorrencia_tarefa_emails)
        self.__projeto.adicionar_ocorrencia(ocorrencia_refatoracao_excecoes)
        self.__projeto.adicionar_ocorrencia(ocorrencia_data_incorreta)

        self.assertEqual(4, len(self.__projeto.ocorrencias))
        self.assertIn(ocorrencia_bug_login, self.__projeto.ocorrencias)
        self.assertIn(ocorrencia_tarefa_emails, self.__projeto.ocorrencias)
        self.assertIn(ocorrencia_refatoracao_excecoes, self.__projeto.ocorrencias)
        self.assertIn(ocorrencia_data_incorreta, self.__projeto.ocorrencias)
        
    def test_nao_adicionar_ocorrencia_nula_no_projeto(self):
        with self.assertRaises(ValueError):
            self.__projeto.adicionar_ocorrencia(None)

    def test_nao_adicionar_ocorrencia_duplicada_no_projeto(self):
        jose = Funcionario("José")
        self.__projeto.adicionar_funcionario(jose)

        ocorrencia_bug_login = Ocorrencia(chave="BUG_001", resumo="Erro ao realizar login", responsavel=jose, prioridade=Prioridade.MEDIA, tipo=TipoOcorrencia.BUG)
       
        self.__projeto.adicionar_ocorrencia(ocorrencia_bug_login)

        with self.assertRaises(ValueError):
            self.__projeto.adicionar_ocorrencia(ocorrencia_bug_login)

    def test_nao_adicionar_ocorrencia_funcionario_responsavel_nao_pertence_projeto(self):
        jose = Funcionario("José")
        ocorrencia_bug_login = Ocorrencia(chave="BUG_001", resumo="Erro ao realizar login", responsavel=jose, prioridade=Prioridade.MEDIA, tipo=TipoOcorrencia.BUG)

        with self.assertRaises(ValueError):
            self.__projeto.adicionar_ocorrencia(ocorrencia_bug_login)

    def test_nao_adicionar_ocorrencia_quando_funcionario_atingiu_limite(self):
        jose = Funcionario("José")
        self.__projeto.adicionar_funcionario(jose)
        jose.adicionar_projeto(self.__projeto)

        criar_n_ocorrencias(jose, self.__projeto, 10)
        ocorrencia_bug_login = Ocorrencia(chave="BUG_001", resumo="Erro ao realizar login", responsavel=jose, prioridade=Prioridade.MEDIA, tipo=TipoOcorrencia.BUG)

        with self.assertRaises(ValueError):
            self.__projeto.adicionar_ocorrencia(ocorrencia_bug_login)
            
    def test_alterar_responsavel_ocorrencia(self):
        jose = Funcionario("José")
        maria = Funcionario("Maria")
        self.__projeto.adicionar_funcionario(jose)
        self.__projeto.adicionar_funcionario(maria)

        ocorrencia_bug_login = Ocorrencia(chave="BUG_001", resumo="Erro ao realizar login", responsavel=jose, prioridade=Prioridade.MEDIA, tipo=TipoOcorrencia.BUG)
        self.__projeto.adicionar_ocorrencia(ocorrencia_bug_login)

        self.__projeto.alterar_responsavel_ocorrencia(ocorrencia_bug_login, maria)

        self.assertEqual(maria, ocorrencia_bug_login.responsavel)


    def test_nao_alterar_responsavel_ocorrencia_nula(self):
        maria = Funcionario("Maria")
        self.__projeto.adicionar_funcionario(maria)

        with self.assertRaises(ValueError):
            self.__projeto.alterar_responsavel_ocorrencia(None, maria)


    def test_nao_alterar_responsavel_ocorrencia_que_nao_pertence_ao_projeto(self):
        jose = Funcionario("José")
        maria = Funcionario("Maria")
        self.__projeto.adicionar_funcionario(jose)
        self.__projeto.adicionar_funcionario(maria)

        ocorrencia_bug_login = Ocorrencia(chave="BUG_001", resumo="Erro ao realizar login", responsavel=jose, prioridade=Prioridade.MEDIA, tipo=TipoOcorrencia.BUG)

        with self.assertRaises(ValueError):
            self.__projeto.alterar_responsavel_ocorrencia(ocorrencia_bug_login, maria)

    def test_nao_alterar_responsavel_para_nulo(self):
        jose = Funcionario("José")
        self.__projeto.adicionar_funcionario(jose)

        ocorrencia_bug_login = Ocorrencia(chave="BUG_001", resumo="Erro ao realizar login", responsavel=jose, prioridade=Prioridade.MEDIA, tipo=TipoOcorrencia.BUG)
        self.__projeto.adicionar_ocorrencia(ocorrencia_bug_login)

        with self.assertRaises(ValueError):
            self.__projeto.alterar_responsavel_ocorrencia(ocorrencia_bug_login, None)

    def test_nao_alterar_responsavel_para_funcionario_que_nao_pertence_ao_projeto(self):
        jose = Funcionario("José")
        maria = Funcionario("Maria")
        self.__projeto.adicionar_funcionario(jose)

        ocorrencia_bug_login = Ocorrencia(chave="BUG_001", resumo="Erro ao realizar login", responsavel=jose, prioridade=Prioridade.MEDIA, tipo=TipoOcorrencia.BUG)
        self.__projeto.adicionar_ocorrencia(ocorrencia_bug_login)

        with self.assertRaises(ValueError):
            self.__projeto.alterar_responsavel_ocorrencia(ocorrencia_bug_login, maria)


    def test_nao_alterar_responsavel_quando_novo_responsavel_atingiu_limite(self):
        jose = Funcionario("José")
        maria = Funcionario("Maria")
        self.__projeto.adicionar_funcionario(jose)
        self.__projeto.adicionar_funcionario(maria)
        maria.adicionar_projeto(self.__projeto)

        criar_n_ocorrencias(maria, self.__projeto, 10)

        ocorrencia_jose = Ocorrencia(chave="BUG_999", resumo="Erro do José", responsavel=jose, prioridade=Prioridade.ALTA, tipo=TipoOcorrencia.BUG)
        self.__projeto.adicionar_ocorrencia(ocorrencia_jose)

        with self.assertRaises(ValueError):
            self.__projeto.alterar_responsavel_ocorrencia(ocorrencia_jose, maria)