# pylint: disable=unused-variable

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'vermelho': '\033[31m',
         'verde': '\033[32m'}

import random
from threading import Timer
from file_configs import debug_printar

class Mesa:
    def __init__(self, lista_jogadores):
        self.lista_jogadores = lista_jogadores


    def carta_inicial(self):
        """
        -> Irá gerar a carta inicial
        :return: retornará uma carta normal
        """
        return carta_normal()


    def sequencias(self, jogadoresHumanos = 1):
        """
        -> Irá gerar uma lista contendo dicionários com as informações de sequencia (quem é o player 0, 1, 2, etc...)
        :param jogadoresHumanos: int -> quantos jogadores humanos, ou seja, que não são IA estão jogando
        :return: retornará uma lista contendo dicionários com as informações de sequencia
        """
        if jogadoresHumanos > len(self.lista_jogadores):
            jogadoresHumanos = len(self.lista_jogadores)
        lista = list()
        dictSequencias = dict()
        for nJogadorReal in range(0, jogadoresHumanos):
            dictSequencias = {f'{nJogadorReal}': True}
            lista.append(dictSequencias.copy())
        for nJogador in range(jogadoresHumanos, len(self.lista_jogadores)):
            dictSequencias = {f'{nJogador}': False}
            lista.append(dictSequencias.copy())
        return lista


    def inverter_sequencias(self, sequenciaDaMesa):
        """
        -> Irá inverter a sequência de jogadores
        :param sequencias: Uma variavél contendo a sequência do jogo. A variavél pode ser declarada dentro da classe
        :return: no return
        """
        return sequenciaDaMesa[::-1]


    def quantidade_de_players(self):
        """
        -> Irá retornar o valor com a quantidade de jogadores que estão jogando
        :return: int -> retornará o valor com a quantidade de players que estão jogando
        """
        return len(self.lista_jogadores)


    def player_inicial(self, quantidade_de_players):
        """
        -> Irá sortear o jogador inicial
        :return: int -> retornará o número do player inicial
        """
        return random.randint(0, quantidade_de_players - 1)


    def inverter(self):
        """
        -> Irá gerar um valor booleano dizendo que o baralho está invertido
        :return: bool -> True
        """
        return True


    def desinverter(self):
        """
        -> Irá gerar um valor booleano dizendo que o baralho está desinvertido
        :return: bool -> False
        """
        return False


    def proximo_player(self, invertido, player_da_vez, quantidade_de_players, pular_player):
        """
        -> Irá definir qual será o próximo jogador á jogar
        :param invertido: váriavel booleana dizendo se o jogo está invertido ou não
        :param player_da_vez: jogador que está jogando
        :param quantidade_de_players: quantidade de players que estão jogando
        :param pular_player: quantidade de jogadores que serão pulados (1, 2, 3, etc.)
        :return: irá retornar qual um integer dizendo qual será o próximo jogador
        """
        quantidade_de_pulos = pular_player
        proximo_jogador = 0
        if invertido == False:
            if player_da_vez + pular_player >= quantidade_de_players:
                return (player_da_vez + pular_player) - quantidade_de_players
            else:
                return player_da_vez + pular_player
        else:
            if player_da_vez - pular_player < 0:
                while True:
                    if player_da_vez - 1 < 0:
                        proximo_jogador = quantidade_de_players - 1
                        quantidade_de_pulos -= 1
                    else:
                        proximo_jogador = player_da_vez - 1
                        quantidade_de_pulos -= 1
                    if quantidade_de_pulos <= 0:
                        break
                    else:
                        pass
                return proximo_jogador
            else:
                return player_da_vez - pular_player


    def acao(self, cores):
        """
        -> Irá printar um menu de jogar
        :param cores: dicionário contendo as cores
        :return: irá retornar um int na qual condiz com a escolhda do jogador
        """
        pergunta = str(input("""Escolha uma ação:
{}1.{} Jogar uma carta
{}2.{} Comprar carta(s)
{}3.{} Ver o seu baralho e a quantidade de cartas de outros jogadores
{}4.{} Encerrar o jogo

Escolha sua opção: """.format(cores['amarelo'], cores['limpa'], cores['amarelo'], cores['limpa'], cores['amarelo'], cores['limpa'], cores['vermelho'], cores['limpa']))).strip()
        while pergunta not in '1234':
            pergunta = str(input('Valor inválido. Por favor, digite novamente: ')).strip()
        perguntaint = int(pergunta)
        return perguntaint
    
    
    def printar_carta_mesa(self, carta_mesa):
        """
        Irá printar a carta na mesa de forma formatada
        :param carta_mesa: váriavel contendo a carta na mesa
        :return: irá retornar uma string dizendo formatada
        """
        if carta_mesa['cor'] == 'vermelho':
            return '{}{} | Vermelho{}'.format(cores['vermelho'], carta_mesa['numero'], cores['limpa'])
        elif carta_mesa['cor'] == 'amarelo':
            return '{}{} | Amarelo{}'.format(cores['amarelo'], carta_mesa['numero'], cores['limpa'])
        elif carta_mesa['cor'] == 'verde':
            return '{}{} | Verde{}'.format(cores['verde'], carta_mesa['numero'], cores['limpa'])
        elif carta_mesa['cor'] == 'azul':
            return '{}{} | Azul{}'.format(cores['azul'], carta_mesa['numero'], cores['limpa'])
        else:
            return '{} | Especial'.format(carta_mesa['numero'])


    def cartas_jogavel(self, carta_mesa, jogador_da_vez, somatoria_de_compra, somatoria_carta, cor_escolhida, cor_escolhidacor, debug=False):
        """
        -> Irá gerar um valor booleano dizendo se há ou não cartas jogáveis no baralho do player
        :param carta_mesa: váriavel contendo a carta na mesa
        :param jogador_da_vez: váriavel integer dizendo o jogador da vez
        :param somatoria_de_compra: somatória de compras de cartas
        :param somatoria_carta: váriavel contendo o tipo de carta que está fazendo a somatória
        :param cor_escolhida: váriavel booleana na qual diz se há uma cor escolhida para ser jogada
        :param cor_escolhidacor: váriavel dizendo a cor específicada
        :return: irá retornar um valor booleano dizendo se há ou não cartas jogáveis
        """
        jogavel = False
        if cor_escolhida == True:
            debug_printar('Cor escolhida == True', debug) # Debug
            if somatoria_de_compra > 0:
                debug_printar('Somatória de compra > 0', debug) # Debug
                for carta in self.lista_jogadores[jogador_da_vez]:
                    if carta['numero'] == '+4':
                        debug_printar('Carta analisada {} == +4'.format(carta), debug) # Debug
                        jogavel = True
                    else:
                        debug_printar('Carta analisada {} != +4'.format(carta), debug) # Debug
                        pass
            else:
                debug_printar('Somatória de compra =< 0', debug) # Debug
                for carta in self.lista_jogadores[jogador_da_vez]:
                    if carta['cor'] == cor_escolhidacor or carta['numero'] == '+4' or carta['numero'] == 'Mudar Cor':
                        debug_printar('Carta analisada {} == Cor escolhida ({}) ou +4 ou Mudar Cor. (Jogável = True)'.format(carta, cor_escolhidacor), debug) # Debug
                        jogavel = True
                    else:
                        debug_printar('Carta analisada {} != Cor escolhida ({}) e +4 e Mudar Cor. (Jogável = False)'.format(carta, cor_escolhidacor), debug) # Debug
                        pass
        else:
            debug_printar('Cor escolhida == False', debug) # Debug
            if somatoria_de_compra > 0:
                debug_printar('Somatória de compra > 0', debug) # Debug
                for carta in self.lista_jogadores[jogador_da_vez]:
                    if carta['numero'] == somatoria_carta:
                        debug_printar('Carta analisada {} == Somatória carta ({}). (Jogável = True)'.format(carta, somatoria_carta), debug) # Debug
                        jogavel = True
                    else:
                        debug_printar('Carta analisada {} != Somatória carta ({}). (Jogável = False)'.format(carta, somatoria_carta), debug) # Debug
                        pass
            else:
                debug_printar('Somatória de compra <= 0', debug) # Debug
                for carta in self.lista_jogadores[jogador_da_vez]:
                    if carta['numero'] == carta_mesa['numero'] or carta['cor'] == carta_mesa['cor'] or carta['numero'] == '+4' or carta['numero'] == 'Mudar Cor':
                        debug_printar('Carta analisada {} == +4 ou Mudar Cor ou Carta na mesa número ({}) ou Carta na Mesa cor ({}). (Jogável = True)'.format(carta, carta_mesa['numero'], carta_mesa['cor']), debug) # Debug
                        jogavel = True
                    else:
                        debug_printar('Carta analisada {} != +4 e Mudar Cor e Carta na mesa número ({}) e Carta na Mesa cor ({}). (Jogável = False)'.format(carta, carta_mesa['numero'], carta_mesa['cor']), debug) # Debug
                        pass
        return jogavel


    def carta_jogavel(self, carta_mesa, carta_jogada, somatoria_de_compra, somatoria_carta, jogador_da_vez, cor_escolhida, cor_escolhidacor, debug=False):
        """
        -> Irá retornar um valor booleano dizendo se a carta escolhida pelo player é jogável
        :param carta_mesa: váriavel contendo a carta na mesa
        :param carta_jogada: carta jogável pelo player
        :param somatoria_de_compra: váriavel integer contendo a quantidade de somatórias de cartas para comprar
        :param somatoria_carta: váriavel dizendo o tipo da carta para somatória de compra
        :param jogador_da_vez: váriavel integer dizendo o jogador da vez
        :param cor_escolhida: váriavel booleana dizendo se há cor escolhida para ser jogada
        :param cor_escolhidacor: váriavel dizendo a cor escolhida para ser jogada
        :return: irá retornar um valor booleano
        """
        if self.lista_jogadores[jogador_da_vez][carta_jogada]['numero'] == '+4':
            if somatoria_de_compra > 0 and somatoria_carta != '+4':
                debug_printar('Carta = +4 | Somatória de compra > 0 e Somatória carta != +4 | Retorno False', debug) # Debug
                return False
            else:
                debug_printar('Carta = +4 | Somatória de compra == 0 e Somatória carta == +4 | Retorno True', debug) # Debug
                return True
        elif self.lista_jogadores[jogador_da_vez][carta_jogada]['numero'] == 'Mudar Cor':
            if somatoria_de_compra > 0:
                debug_printar('Carta = Mudar Cor | Somatória de compra > 0 | Retorno False', debug) # Debug
                return False
            else:
                debug_printar('Carta = Mudar Cor | Somatória de compra == 0 | Retorno True', debug) # Debug
                return True
        elif self.lista_jogadores[jogador_da_vez][carta_jogada]['numero'] == '+2':
            if somatoria_de_compra > 0 and somatoria_carta == '+2':
                debug_printar('Carta = +2 | Somatória de compra > 0 e Somatória Carta == +2 | Retorno True', debug) # Debug
                return True
            elif somatoria_de_compra == 0 and carta_mesa['cor'] == self.lista_jogadores[jogador_da_vez][carta_jogada]['cor']:
                debug_printar('Carta = +2 | Somatória de compra == 0 e Cor da carta na mesa == Cor da carta jogada | Retorno True', debug) # Debug
                return True
            else:
                debug_printar('Carta = +2 | Não atende a nenhum requisito anterior | Retorno False', debug) # Debug
                return False
        else:
            if somatoria_de_compra > 0:
                debug_printar('Carta != +4, Mudar Cor e +2 | Somatória de compra > 0 | Retorno False', debug) # Debug
                return False
            if cor_escolhida == True:
                if self.lista_jogadores[jogador_da_vez][carta_jogada]['cor'] == cor_escolhidacor:
                    debug_printar('Carta != +4, Mudar Cor e +2 | Cor escolhida == True e Carta jogada == Cor escolhida cor | Retorno True', debug) # Debug
                    return True
                else:
                    debug_printar('Carta != +4, Mudar Cor e +2 | Cor escolhida == True e Carta jogada != Cor escolhida cor | Retorno True', debug) # Debug
                    return False
            else:
                if self.lista_jogadores[jogador_da_vez][carta_jogada]['cor'] == carta_mesa['cor'] or self.lista_jogadores[jogador_da_vez][carta_jogada]['numero'] == carta_mesa['numero']:
                    debug_printar('Carta != +4, Mudar Cor e +2 | Cor escolhida == True e Carta jogada != Cor escolhida cor | Retorno True', debug) # Debug
                    return True
                else:
                    debug_printar('Carta != +4, Mudar Cor e +2 | Cor escolhida == True e Carta jogada != Cor escolhida cor | Retorno True', debug) # Debug
                    return False


    def jogar_carta_menu(self, jogador_da_vez, cores, lock_jogar):
        """
        -> Irá fazer um input na qual o jogador irá ter que digitar a carta que deseja jogar
        :param jogador_da_vez: váriavel integer dizendo o jogador da vez
        :param cores: dicionário com cores
        :return: irá retornar o integer do índice da carta
        """
        if lock_jogar == False:
            while True:
                try:
                    carta = int(input('Por favor, digite a carta que deseja jogar: '.format(cores['vermelho'], cores['limpa'])))
                    if carta > -1 and carta < len(self.lista_jogadores[jogador_da_vez]):
                        break
                except:
                    pass
            return carta
        else:
            pass


    def cartas_invalidas_loop(self, cores):
        """
        -> Caso ocorra um erro de cartas iválidas, este loop será acionado
        :param cores: dicionário contendo as cores
        :return: retornará um integer dando uma opção válida para ser jogada
        """
        print()
        print('Você não possui nenhuma carta jogável. Escolha outra opção:')
        print('{}1.{} Jogar uma carta\n{}2.{} Comprar carta(s)\n{}3.{} Ver o seu baralho e a quantidade de cartas de outros jogadores\n{}4.{} Encerrar o jogo'.format(cores['amarelo'], cores['limpa'], cores['amarelo'], cores['limpa'], cores['amarelo'], cores['limpa'], cores['vermelho'], cores['limpa']))
        while True:
            try:
                escolha_loop = int(input('Digite sua opção: '))
                if escolha_loop != 1 and escolha_loop != 2 and escolha_loop != 3 and escolha_loop != 4:
                    escolha_loop = int(input('{}Opção inválida.{} Digite sua opção novamente: '.format(cores['vermelho'], cores['limpa'])))
                else:
                    break
            except:
                pass
        while escolha_loop == 1:
            print('Você não possui cartas válidas.', end= '')
            while True:
                try:
                    escolha_loop = int(input('Digite sua opção: '))
                    if escolha_loop != 1 and escolha_loop != 2 and escolha_loop != 3 and escolha_loop != 4:
                        escolha_loop = int(input('{}Opção inválida.{} Digite sua opção novamente: '.format(cores['vermelho'], cores['limpa'])))
                    else:
                        break
                except:
                    pass
        if escolha_loop == 2:
            return 2
        elif escolha_loop == 3:
            return 3
        elif escolha_loop == 4:
            return 4


    def printar_nome_cor(self, cor_escolhidacor, cores):
        """
        -> Irá printar o nome da cor escolhida de forma formatada
        :param cor_escolhidacor: váriavel contendo a cor escolhida
        :param cores: dicionário de cores
        :return: irá retornar uma string formatada com o nome da cor
        """
        if cor_escolhidacor == 'azul':
            return '{}Azul{}'.format(cores['azul'], cores['limpa'])
        elif cor_escolhidacor == 'verde':
            return '{}Verde{}'.format(cores['verde'], cores['limpa'])
        elif cor_escolhidacor == 'amarelo':
            return '{}Amarelo{}'.format(cores['amarelo'], cores['limpa'])
        elif cor_escolhidacor == 'vermelho':
            return '{}Vermelho{}'.format(cores['vermelho'], cores['limpa'])
        else:
            return cor_escolhidacor


    def uno_menu(self, intervalo, cores):
        """
        -> Irá printar um prompt pedindo para o jogador digitar uno dentro do tempo especificado. Caso não consiga, comprar cartas.
        :param intervalo: (float) intervalo especificado em "config.ini"
        :param cores: dicionário contendo as cores
        :return: valor booleano dizendo se o jogador terá que comprar cartas ou não
        """
        comprar = True
        t = Timer(intervalo, print, ['\nTempo acabou. Você não digitou "Uno" :( | Aperte {}"Enter"{} para continuar.'.format(cores['azul'], cores['limpa'])])
        t.start()
        pergunta = str(input('{}UNO NA SUA VEZ! DIGITE UNO{}: '.format(cores['vermelho'], cores['limpa']))).lower().strip()
        t.cancel()
        if pergunta == 'uno':
            print('Boa! você se livrou de comprar cartas')
            t.cancel()
            comprar = False
        else:
            t.cancel()
        return comprar


class Cartas:
    def __init__(self, lista_jogadores):
        self.lista_jogadores = lista_jogadores


    def possui_carta_numero(self, request_player, carta_numero):
        """
        -> Irá gerar um valor booleano dizendo se o jogador possuí uma carta de 'x' número
        :param request_player: baralho que será analisado
        :param carta_numero: número da carta que se deseja encontrar
        :return: True/False
        """
        possui_carta = False
        for c in range(0, len(self.lista_jogadores[request_player])):
            if self.lista_jogadores[request_player][c]['numero'] == carta_numero:
                possui_carta = True
            else:
                pass
        return possui_carta


    def menu_cores(self, cores):
        """
        -> Irá criar um input na qual o usuário terá que escolher a cor que desejá jogar
        :param cores: dicionário contendo as cores
        :return: irá retornar um integer na qual condiz com a cor escolhida
        """
        print('Escolha uma cor: \n{}1. Vermelho{}\n{}2. Amarelo{}\n{}3. Azul{}\n{}4. Verde{}'.format(cores['vermelho'], cores['limpa'], cores['amarelo'], cores['limpa'], cores['azul'], cores['limpa'], cores['verde'], cores['limpa']))
        cor = str(input('Digite o número da cor: '))
        while cor not in '1234':
            cor = str(input('Valor inválido. Por favor, digite o número da cor: '))
        corint = int(cor)
        return corint


    def efeito_mudar_cor(self, cores):
        """
        -> Irá associar as cores em integer com as cores em string
        :param cores: dicionário de cores
        :return: irá retornar uma string dizendo a cor escolhida no menu_cores
        """
        cornum = self.menu_cores(cores)
        if cornum == 1:
            return 'vermelho'
        elif cornum == 2:
            return 'amarelo'
        elif cornum == 3:
            return 'azul'
        else:
            return 'verde'


class Debug:
    def __init__(self, lista_jogadores, cores):
        self.lista_jogadores = lista_jogadores
        self.cores = cores


    def ai_printarcartas(self, jogador_da_vez, carta_mesa, somatoria_de_compra, somatoria_carta, cor_escolhida, cor_escolhidacor, debug=False):
        """
        -> Irá printar as cartas dos jogadores. Tambem haverá debug caso esteja especificado.
        :param jogador_da_vez: váriavel contendo o jogador da vez
        :param carta_mesa: váriavel contendo a carta na mesa
        :param somatoria_de_compra: váriavel contendo a somatória de compra
        :param somatoria_carta: váriavel contendo a carta da somatória
        :param cor_escolhida: váriavel contendo um boolean dizendo se há uma cor escolhida
        :param cor_escolhidacor: váriavel contendo a cor escolhida
        :param debug: irá ativar ou desativar o debug
        :return: sem retorno
        """
        classe_mesa = Mesa(self.lista_jogadores)
        if debug == True:
            print(f'==========\nJogador da vez: {jogador_da_vez}\num_cartas jogáveis: {classe_mesa.cartas_jogavel(carta_mesa, jogador_da_vez, somatoria_de_compra, somatoria_carta, cor_escolhida, cor_escolhidacor, False)}\num_cartas do Jogador:')
            for carta in self.lista_jogadores[jogador_da_vez]:
                if carta['cor'] == 'vermelho':
                    print('{}{} | Vermelho{}'.format(cores['vermelho'], carta['numero'], cores['limpa']))
                elif carta['cor'] == 'amarelo':
                    print('{}{} | Amarelo{}'.format(cores['amarelo'], carta['numero'], cores['limpa']))
                elif carta['cor'] == 'verde':
                    print('{}{} | Verde{}'.format(cores['verde'], carta['numero'], cores['limpa']))
                elif carta['cor'] == 'azul':
                    print('{}{} | Azul{}'.format(cores['azul'], carta['numero'], cores['limpa']))
                else:
                    print('{} | Especial'.format(carta['numero']))


class Ai:
    def __init__(self, lista_jogadores, cores):
        self.lista_jogadores = lista_jogadores
        self.cores = cores


    def possui_cartas(self, lista_jogadores, jogador_escolhido, carta_numero, cor_especifica=''):
        """
        -> Irá informar se o jogador desejado para a análise possui cartas do número/cor desejada
        :param lista_jogadores: váriavel contendo a lista com os baralhos
        :param jogador_escolhido: jogador escolhido para a análise
        :param carta_numero: número específico para ser analisado
        :param cor_especifica: cor específica para ser analisada
        :return: irá retornar um boolean dizendo se o jogador possui cartas
        """
        possui_cartas_desejadas = False
        if cor_especifica != 'amarelo' and cor_especifica != 'vermelho' and cor_especifica != 'azul' and cor_especifica != 'verde' and cor_especifica != 'especial' and cor_especifica != '':
            raise TypeError("Cor específica selecionada é do tipo errado. Por favor, digite um cor específica certa.")
        else:
            if cor_especifica == '':
                for carta in lista_jogadores[jogador_escolhido]:
                    if carta['numero'] == carta_numero:
                        possui_cartas_desejadas = True
                    else:
                        pass
            else:
                for carta in lista_jogadores[jogador_escolhido]:
                    if carta['numero'] == carta_numero and carta['cor'] == cor_especifica:
                        possui_cartas_desejadas = True
                    else:
                        pass
        return possui_cartas_desejadas


    def tamanho_baralho(self, lista_jogadores, jogador_escolhido, tamanho_index=False):
        """
        -> irá informar o tamanho do baralho de um player
        :param lista_jogadores: váriavel contendo os baralhos
        :param jogador_escolhido: jogador escolhido para ser analisado
        :param tamanho_index: caso true, irá retornar um valor de índice, isto é, usando o método len() - 1
        :return: irá retornar o tamanho do baralho do player desejado
        """
        if tamanho_index == True:
            return len(lista_jogadores[jogador_escolhido]) - 1 # Will return the index length of the chosen player's deck. That's it: the len function minus one
        else:
            return len(lista_jogadores[jogador_escolhido]) # Will return the length of the chosen player using the 'len()' method


    def unica_carta_jogavel(self, lista_jogadores, jogador_escolhido, carta_escolhida_numero, carta_mesa, somatoria_de_compra, somatoria_carta, cor_escolhida, cor_escolhidacor):
        """
        -> Irá informar se o player analisado possui apenas uma unica carta jogável do tipo específico
        :param lista_jogadores: váriavel contendo os baralhos dos jogadores
        :param jogador_escolhido: jogador escolhido para ser analisado
        :param carta_escolhida_numero: número específico para ser analisado
        :param carta_mesa: carta na mesa
        :param somatoria_de_compra: váriavel contendo a somatória de compra
        :param somatoria_carta: váriavel contendo a carta da somatória
        :param cor_escolhida: váriavel booleana dizendo se há cor escolhida específica
        :param cor_escolhidacor: váriavel contendo a cor escolhida
        :return: irá retornar um booleano dizendo se há apenas uma carta jogável
        """
        unica_carta_jogavel = True
        classe_mesa = Mesa(lista_jogadores)        
        for c in range(0, self.tamanho_baralho(lista_jogadores, jogador_escolhido, False)):
            if lista_jogadores[jogador_escolhido][c]['numero'] != carta_escolhida_numero and classe_mesa.carta_jogavel(carta_mesa, c, somatoria_de_compra, somatoria_carta, jogador_escolhido, cor_escolhida, cor_escolhidacor, False) == True:
                unica_carta_jogavel = False
            else:
                pass
        return unica_carta_jogavel


    def selecionar_carta_random_index(self, lista_jogadores, jogador_escolhido, carta_numero):
        """
        -> Irá selecionar carta random baseada no número específico
        :param lista_jogadores: váriavel contendo os baralhos dos jogadores
        :param jogador_escolhido: jogador escolhido para ser analisado
        :param carta_numero: carta específica para ser analisada
        :return: irá retornar o índice da carta específica a ser analisada dentro do baralho
        """
        primeiro_indice = -1
        for c in range(0, self.tamanho_baralho(lista_jogadores, jogador_escolhido, False)):
            if primeiro_indice != -1:
                pass
            else:
                if lista_jogadores[jogador_escolhido][c]['numero'] == carta_numero:
                    primeiro_indice = c
        if primeiro_indice == -1:
            raise ValueError('A carta desejada para ser selecionada não está no baralho. Você digitou a carta certa?')
        else:
            return primeiro_indice


    def selecionar_carta_normal_random(self, lista_jogadores, jogador_escolhido, carta_mesa, somatoria_carta, somatoria_de_compra, cor_escolhida, cor_escolhidacor, ignorar_bloqueio_e_inverte):
        """
        -> Irá selecionar uma carta normal aleatória do baralho do jogador especificado
        :param lista_jogadores: váriavel contendo os baralhos
        :param jogador_escolhido: jogador especifico a ser analisado
        :param carta_mesa: váriavel contendo a carta na mesa
        :param somatoria_carta: váriavel contendo o tipo da carta de somatória
        :param somatoria_de_compra: váriavel contendo a compra da somatória
        :param cor_escolhida: váriavel booleana dizendo se há uma cor escolhida
        :param cor_escolhidacor: váriavel dizendo a cor escolhida
        :param ignorar_bloqueio_e_inverte: se selecionado True, irá pular cartas "bloqueio" e "inverte"
        :return: irá retornar o índice da carta específicada
        """
        classe_mesa = Mesa(lista_jogadores)
        primeiro_indice = -1
        for c in range(0, self.tamanho_baralho(lista_jogadores, jogador_escolhido, False)):
            if primeiro_indice != -1:
                pass
            else:
                if ignorar_bloqueio_e_inverte == True:
                    if lista_jogadores[jogador_escolhido][c]['numero'] != '+4' and lista_jogadores[jogador_escolhido][c]['numero'] != '+2' and lista_jogadores[jogador_escolhido][c]['numero'] != 'Mudar Cor' and lista_jogadores[jogador_escolhido][c]['numero'] != 'Inverte' and lista_jogadores[jogador_escolhido][c]['numero'] != 'Bloqueio':
                        if classe_mesa.carta_jogavel(carta_mesa, c, somatoria_de_compra, somatoria_carta, jogador_escolhido, cor_escolhida, cor_escolhidacor, False) == True:
                            primeiro_indice = c
                    else:
                        pass
                else:
                    if lista_jogadores[jogador_escolhido][c]['numero'] != '+4' and lista_jogadores[jogador_escolhido][c]['numero'] != '+2' and lista_jogadores[jogador_escolhido][c]['numero'] != 'Mudar Cor':
                        if classe_mesa.carta_jogavel(carta_mesa, c, somatoria_de_compra, somatoria_carta, jogador_escolhido, cor_escolhida, cor_escolhidacor, False) == True:
                            primeiro_indice = c
                    else:
                        pass
        if primeiro_indice == -1:
            raise ValueError('A carta desejada para ser selecionada não está no baralho. Você digitou a carta certa?')
        else:
            return primeiro_indice


    def possui_cartas_normais(self, lista_jogadores, jogador_escolhido, carta_mesa, somatoria_de_compra, somatoria_carta, cor_escolhida, cor_escolhidacor):
        """
        -> Irá analisar o baralho do jogador especifico para dizer se há cartas normais em seu baralho
        :param lista_jogadores: váriavel contendo os baralhos
        :param jogador_escolhido: jogador para ser analisado
        :param carta_mesa: váriavel contendo a carta na mesa
        :param somatoria_de_compra: váriavel contendo a somatória de compra
        :param somatoria_carta: váriavel contendo a carta da somatória
        :param cor_escolhida: váriavel booleana dizendo se há uma cor escolhida
        :param cor_escolhidacor: váriavel dizendo a cor escolhida
        :return: irá retornar um valor booleano dizendo se o jogador possui cartas normais
        """
        classe_mesa = Mesa(lista_jogadores)
        possuicartasnormais = False
        for c in range(0, self.tamanho_baralho(lista_jogadores, jogador_escolhido, False)):
            if lista_jogadores[jogador_escolhido][c]['numero'] != '+4' and lista_jogadores[jogador_escolhido][c]['numero'] != '+2' and lista_jogadores[jogador_escolhido][c]['numero'] != 'Bloqueio' and lista_jogadores[jogador_escolhido][c]['numero'] != 'Inverte' and lista_jogadores[jogador_escolhido][c]['numero'] != 'Mudar Cor':
                if classe_mesa.carta_jogavel(carta_mesa, c, somatoria_de_compra, somatoria_carta, jogador_escolhido, cor_escolhida, cor_escolhidacor, False) == True:
                    possuicartasnormais = True
            else:
                pass
        return possuicartasnormais


    def cor_majoritaria(self, lista_jogadores, jogador_escolhido, considerar_cores_especiais=False):
        """
        -> Irá analisar e ver qual é a cor majoritária do baralho do player especificado
        :param lista_jogadores: váriavel contendo os baralhos
        :param jogador_escolhido: jogador para ser analisado
        :param considerar_cores_especiais: irá considerar as cores especiais
        :return: irá retornar um valor string dizendo qual é a cor majoritária
        """
        cor_majoritaria = {'amarelo': 0, 'vermelho': 0, 'azul': 0, 'verde': 0, 'especiais': 0}
        for carta in lista_jogadores[jogador_escolhido]:
            if carta['cor'] == 'amarelo':
                cor_majoritaria['amarelo'] += 1
            if carta['cor'] == 'vermelho':
                cor_majoritaria['vermelho'] += 1
            if carta['cor'] == 'azul':
                cor_majoritaria['azul'] += 1
            if carta['cor'] == 'verde':
                cor_majoritaria['verde'] += 1
            if carta['cor'] == 'preto':
                cor_majoritaria['especiais'] += 1
        if considerar_cores_especiais == False:
            del cor_majoritaria['especiais']
        else:
            pass
        cor_majoritaria_sorted = sorted(cor_majoritaria.items(), key = lambda kv: kv[1], reverse=True)
        valormaisaltocor = cor_majoritaria_sorted[0][0]
        return valormaisaltocor


    def possui_carta_jogavel(self, lista_jogadores, jogador_escolhido, carta, carta_mesa, somatoria_de_compra, somatoria_carta, cor_escolhida, cor_escolhidacor):
        """
        -> Irá analisar e dizer se o jogador especificado possui alguma a carta especificada jogável
        :param lista_jogadores: váriavel contendo os baralhos
        :param jogador_escolhido: jogador para ser analisado
        :param carta: carta para ser analisada
        :param carta_mesa: váriavel contendo a carta na mesa
        :param somatoria_de_compra: váriavel contendo a somatória de compra
        :param somatoria_carta: váriavel contendo a carta da somatória
        :param cor_escolhida: váriavel booleana dizendo se há uma cor escolhida
        :param cor_escolhidacor: váriavel dizendo a cor escolhida
        :return: irá retonar um valor booleano dizendo se possui carta especificada jogável
        """
        classe_mesa = Mesa(lista_jogadores)
        carta_jogavel = False
        for c in range(0, self.tamanho_baralho(lista_jogadores, jogador_escolhido, False)):
            if lista_jogadores[jogador_escolhido][c]['numero'] == carta and classe_mesa.carta_jogavel(carta_mesa, c, somatoria_de_compra, somatoria_carta, jogador_escolhido, cor_escolhida, cor_escolhidacor, False) == True:
                carta_jogavel = True
            else:
                pass
        return carta_jogavel


def maisquatro():
    """
    -> irá gerar uma carta "+4"
    :return: irá retornar um dict com o número da carta e a cor
    """
    return {'numero': '+4', 'cor': 'preto'}


def maisdois():
    """
    -> irá gerar uma carta "+2"
    :return: irá retornar um dict com o número da carta e a cor
    """
    cor_numero = random.randint(0, 40)
    cor_da_carta = 'vermelho'
    if cor_numero < 10:
        cor_da_carta = 'azul'
    elif cor_numero >= 10 and cor_numero < 20:
        cor_da_carta = 'amarelo'
    elif cor_numero >= 20 and cor_numero < 30:
        cor_da_carta = 'vermelho'
    elif cor_numero >= 30:
        cor_da_carta = 'verde'
    return {'numero': '+2', 'cor': cor_da_carta}


def mudarcor():
    """
    -> irá gerar uma carta "Mudar Cor"
    :return: irá retornar um dict com o número da carta e a cor
    """
    return {'numero': 'Mudar Cor', 'cor': 'preto'}


def bloqueio():
    """
    -> Irá gerar uma carta "Bloqueio"
    :return: irá retornar um dict com o número da carta e a cor
    """
    cor_numero = random.randint(0, 40)
    cor_da_carta = 'vermelho'
    if cor_numero < 10:
        cor_da_carta = 'azul'
    elif cor_numero >= 10 and cor_numero < 20:
        cor_da_carta = 'amarelo'
    elif cor_numero >= 20 and cor_numero < 30:
        cor_da_carta = 'vermelho'
    elif cor_numero >= 30:
        cor_da_carta = 'verde'
    return {'numero': 'Bloqueio', 'cor': cor_da_carta}


def inverte():
    """
    -> Irá gerar uma carta "Inverte"
    :return: irá retornar um dict com o número da carta e a cor
    """
    cor_numero = random.randint(0, 40)
    cor_da_carta = 'vermelho'
    if cor_numero < 10:
        cor_da_carta = 'azul'
    elif cor_numero >= 10 and cor_numero < 20:
        cor_da_carta = 'amarelo'
    elif cor_numero >= 20 and cor_numero < 30:
        cor_da_carta = 'vermelho'
    elif cor_numero >= 30:
        cor_da_carta = 'verde'
    return {'numero': 'Inverte', 'cor': cor_da_carta}


def carta_normal():
    """
    -> Irá gerar uma carta normal, isto é, que não seja +4, +2, inverte e bloqueio
    :return: irá retornar um dict com o número da carta e a cor
    """
    numero_da_carta = random.randint(0, 9)
    cor_numero = random.randint(0, 40)
    cor_da_carta = 'vermelho'
    if cor_numero < 10:
        cor_da_carta = 'azul'
    elif cor_numero >= 10 and cor_numero < 20:
        cor_da_carta = 'amarelo'
    elif cor_numero >= 20 and cor_numero < 30:
        cor_da_carta = 'vermelho'
    elif cor_numero >= 30:
        cor_da_carta = 'verde'
    return {'numero': numero_da_carta, 'cor': cor_da_carta}


def sortear_carta(num_random):
    """
    -> Irá sortear uma carta de qualquer tipo
    :param num_random: receberá um valor aleatório entre 0 á 100 (usando a biblioteca "random" e a função "randint()"
    :return: irá retornar o dict com o número da carta e a cor gerada
    """
    if num_random >= 90: # 10% de chance de +4
        return maisquatro()
    elif num_random >= 75 and num_random < 90: # 15% de chance de +2
        return maisdois()
    elif num_random >= 64 and num_random < 75: # 12% de Mudar cor
        return mudarcor()
    elif num_random >= 50 and num_random < 56: # 6% de Bloquear
        return bloqueio()
    elif num_random >= 56 and num_random < 64: # 6% de Inverte
        return inverte()
    else:
        return carta_normal()


def baralho_inicial(num_players, lista_jogadores, cartas_iniciais):
    """
    -> Irá sortear o baralho inicial para cada jogador
    :param num_players: int -> o número de players que haverá na partida (contando com os bots e os players)
    :param lista_jogadores: list() -> lista vazia na qual será armazenada listas contendo as cartas dos jogadores
    :param cartas_iniciais: int -> o número de cartas que serão sorteadas
    :return: no return
    """
    for jogador in range(0, num_players):
        baralhoPlayer = list()
        for c in range(0, cartas_iniciais):
            numerorandom = random.randint(0, 100)
            carta = sortear_carta(numerorandom)
            baralhoPlayer.append(carta.copy())
        lista_jogadores.append(baralhoPlayer[:])


def ver_cartas(lista_jogadores, request_player = 0):
    """
    -> Irá mostrar as cartas do player requisitado (valor default = 0)
    :param lista_jogadores: list() -> Lista na qual foi armazenada as informações das cartas dos jogadores
    :param request_player: int -> Player na qual requisitou a informação
    :return: no return
    """
    print('-'*20)
    for c in range(0, len(lista_jogadores[request_player])):
        if lista_jogadores[request_player][c]['cor'] == 'amarelo':
            print('{}{}. {:<9} | Amarelo{}'.format(cores['amarelo'], c, lista_jogadores[request_player][c]['numero'], cores['limpa']))
        elif lista_jogadores[request_player][c]['cor'] == 'vermelho':
            print('{}{}. {:<9} | Vermelho{}'.format(cores['vermelho'], c, lista_jogadores[request_player][c]['numero'], cores['limpa']))
        elif lista_jogadores[request_player][c]['cor'] == 'verde':
            print('{}{}. {:<9} | Verde{}'.format(cores['verde'], c, lista_jogadores[request_player][c]['numero'], cores['limpa']))
        elif lista_jogadores[request_player][c]['cor'] == 'azul':
            print('{}{}. {:<9} | Azul {}'.format(cores['azul'], c, lista_jogadores[request_player][c]['numero'], cores['limpa']))
        if lista_jogadores[request_player][c]['cor'] == 'preto':
            print('{}. {:<9} | Especial'.format(c, lista_jogadores[request_player][c]['numero']))


def gerar_baralhos(numero_jogadores=4, cartas_iniciais=7):
    """
    -> Irá gerar os baralhos iniciais
    :return: retornará uma lista contendo o baralho de cada player
    """
    if numero_jogadores < 2:
        numero_jogadores = 4
    if cartas_iniciais <= 2:
        cartas_iniciais = 7
    lista = list()
    baralho_inicial(numero_jogadores, lista, cartas_iniciais)
    return lista


def remover_carta(lista_jogadores, request_jogador, index_carta):
    """
    -> Irá remover uma carta específica do baralho de certo jogador
    :param lista_jogadores: lista contendo as listas com o baralho de cada jogador
    :param request_jogador: jogador que requisitou o método
    :param index_carta: o número da carta que irá ser removida
    :return: no return
    """
    del lista_jogadores[request_jogador][index_carta]


def comprar_carta(lista_jogadores, request_player, num_cartas):
    """
    -> Irá comprar um número específico de cartas e adicioná-las ao baralho do player requisitado
    :param lista_jogadores: lista contendo os baralhos dos jogadores
    :param request_player: player que requisitou a ação
    :param num_cartas: número de cartas que se deseja comprar
    :return: no return
    """
    if num_cartas < 1:
        num_cartas = 1
    for c in range(0, num_cartas):
        num_random = random.randint(0, 100)
        carta = sortear_carta(num_random)
        lista_jogadores[request_player].append(carta)


def qnt_cartas_jogadores(lista_jogadores, jogador_da_vez):
    """
    -> Irá printar na tela quantas cartas o jogador que requisitou a ação tem
    :param lista_jogadores: lista contendo os baralhos dos jogadores
    :param jogador_da_vez: jogador que requisitou a ação
    :return: no return
    """
    lista = lista_jogadores
    for c in range(0, len(lista)):
        if c == jogador_da_vez:
            print('Você ({}jogador {}{}) possui {}{}{} carta(s).'.format(cores['amarelo'], c, cores['limpa'], cores['vermelho'], len(lista[c]), cores['limpa']), end = ' ')
        else:
            print('O jogador {}{}{} possui {}{}{} carta(s).'.format(cores['amarelo'], c, cores['limpa'], cores['vermelho'], len(lista[c]), cores['limpa']), end = ' ')
    print()


def pegar_carta_index(lista_jogadores, jogador_da_vez, index_carta):
    """
    -> Irá pegar o dicionário da carta através do índice da mesma na lista
    :param lista_jogadores: lista contendo os baralhos dos jogadores
    :param jogador_da_vez: jogador da vez
    :param index_carta: índice da carta que o usuário deseja
    :return: irá retornar o dicionário da carta
    """
    return lista_jogadores[jogador_da_vez][index_carta]


def checar_ganhador(lista_jogadores, quantidade_de_players):
    """
    -> Irá analisar o tamanho dos baralhos e informar se houve um ganhador
    :param lista_jogadores: lista contendo os baralhos dos jogadores
    :param quantidade_de_players: quantidade de jogadores na partida
    :return: irá retornar um valor booleano dizendo se há um ganhador
    """
    jogador_ganhou = False
    for c in range(0, quantidade_de_players):
        if len(lista_jogadores[c]) == 0:
            jogador_ganhou = True
        else:
            pass
    return jogador_ganhou


def ganhador(lista_jogadores, quantidade_de_players):
    """
    -> Irá analisar o tamanho dos baralhos e informar se quem foi o ganhador
    :param lista_jogadores: lista contendo os baralhos dos jogadores
    :param quantidade_de_players: quantidade de jogadores na partida
    :return: irá retornar um valor integer dizendo qual player foi o ganhador
    """
    ganhador = 0
    for c in range(0, quantidade_de_players):
        if len(lista_jogadores[c]) == 0:
            ganhador = c
        else:
            pass
    return ganhador
