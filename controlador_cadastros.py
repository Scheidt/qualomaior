from cadastro import Cadastro
from tela_cadastros import TelaCadastros
from random import randint


class Controlador_Cadastros():
    def __init__(self) -> None:
        self.__cadastros = [Cadastro("Facebook", "rede social", "Estados Unidos", 1440000001), 
                            Cadastro("Youtube", "website de vídeos", "Estados Unidos", 1440000000),
                            Cadastro("Amazon", "website de compras", "Estados Unidos", 1200000000),
                            Cadastro("Messi", "jogador de futebol", "Argentina", 43493385),
                            Cadastro("Pele", "jogador de futebol", "Brasil", 24468352),
                            Cadastro("luigi", "ruivo", "Brasil", 1750000)]
        self.__tela = TelaCadastros()

    def menu(self):
        switch = {1: self.listar_cadastros,
                  2: self.listar_cadastros_com_pesquisas,
                  3: self.incluir_opcao,
                  4: self.excluir_produto,
                  5: self.jogar}
        while True:
            escolha = self.__tela.listar_opcoes()
            if escolha is None:
                break
            if escolha == 5:
                if switch[escolha]():  # Se a pessoa acertar, ela retorna um True ao main, o que adiciona um ponto
                    return True
            switch[escolha]()

    def listar_cadastros(self):
        if len(self.__cadastros) == 0:
            self.__tela.mostra_mensagem("Nenhuma opção foi registrada ainda, por favor, registre uma opção antes de utilizar este comando.")
        else:
            buffer = []
            for cadastro in self.__cadastros:
                buffer.append({'nome': cadastro.nome, 'descricao': cadastro.descricao, 'pais': cadastro.pais})
            self.__tela.mostra_cadastros(buffer)

    def listar_cadastros_com_pesquisas(self):
        if len(self.__cadastros) == 0:
            self.__tela.mostra_mensagem("Nenhuma opção foi registrada ainda, por favor, registre uma opção antes de utilizar este comando. \n")
        else:
            buffer = []
            for cadastro in self.__cadastros:
                buffer.append({'nome': cadastro.nome, 'descricao': cadastro.descricao, 'pais': cadastro.pais, 'pesquisas': cadastro.pesquisas})
            self.__tela.mostra_cadastros(buffer, pesquisasTbm = True)

    def incluir_opcao(self):
        dados = self.__tela.pega_dados_cadastro()
        if dados is None: # Quando a entrada é cancelada na tela
            return None
        else:
            cadastro = self.pega_opcao_por_nome(nome = dados['nome'])
            try:
                if cadastro is None:  #cód de saída
                    return None
                elif not cadastro:
                    self.__cadastros.append(Cadastro(dados['nome'],
                                                dados['descricao'],
                                                dados['pais'],
                                                dados['pesquisas']))
                else:
                    self.__tela.mostra_mensagem("Já foi inscrito uma opção com este nome! Cadastro não feito.")
            except:
                self.__tela.mostra_mensagem("Não é possível alcançar esse código, eu acho")
                pass
        
    def excluir_produto(self):
        opcao = self.pega_opcao_por_nome()
        while True:
            if opcao is None:
                break
            try:
                self.__cadastros.remove(opcao)
            except:
                self.__tela.mostra_mensagem("Não foi encontrado cadastro com esse nome.")
            else:
                self.__tela.mostra_mensagem("Cadastro removido com sucesso")
                break

    def pega_opcao_por_nome(self, nome = None): # None para cód de retorno, False se n achar e Objeto se achar
        if nome is None:
            nome = self.__tela.pega_nome()
        if nome == '0':
            return None
        for opcao in self.__cadastros:
            if opcao.nome == nome:
                return opcao
        else:
            return False

    def jogar(self):
        if not len(self.__cadastros) > 2:
            self.__tela.mostra_mensagem(f"Utilizar esta função requer que ao menos dois cadastros sejam feito."\
                                         f"Por favor, registre mais {2-len(self.__cadastros)} opções")
        else:
            buffer = []
            rand1 = randint(0, len(self.__cadastros))
            rand2 = randint(0, len(self.__cadastros))
            while rand1 == rand2:
                rand2 = randint(0, len(self.__cadastros))
            cadastro1 = self.__cadastros[rand1]
            cadastro2 = self.__cadastros[rand2]
            buffer.append({'nome': cadastro1.nome, 'descricao': cadastro1.descricao, 'pais': cadastro1.pais, 'pesquisas': cadastro1.pesquisas})
            buffer.append({'nome': cadastro2.nome, 'descricao': cadastro2.descricao, 'pais': cadastro2.pais, 'pesquisas': cadastro2.pesquisas})
            resultado = self.__tela.jogar(buffer)
            if resultado is None:
                return
            elif resultado:  # Se a pessoa acertar qual é maior
                return True
            elif not resultado:
                return False