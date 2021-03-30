# pylint: disable=unused-variable

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'vermelho': '\033[31m',
         'verde': '\033[32m'}

import random

def maisquatro():
    '''
    -> irá gerar uma carta "+4"
    :return: irá retornar um dict com o número da carta e a cor
    '''
    return {'numero': '+4', 'cor': 'preto'}


def maisdois():
    '''
    -> irá gerar uma carta "+2"
    :return: irá retornar um dict com o número da carta e a cor
    '''
    cornumero = random.randint(0, 40)
    cordacarta = 'vermelho'
    if cornumero < 10:
        cordacarta = 'azul'
    elif cornumero >= 10 and cornumero < 20:
        cordacarta = 'amarelo'
    elif cornumero >= 20 and cornumero < 30:
        cordacarta = 'vermelho'
    elif cornumero >= 30:
        cordacarta = 'verde'
    return {'numero': '+2', 'cor': cordacarta}


def mudarcor():
    '''
    -> irá gerar uma carta "Mudar Cor"
    :return: irá retornar um dict com o número da carta e a cor
    '''
    return {'numero': 'Mudar Cor', 'cor': 'preto'}


def bloqueio():
    '''
    -> Irá gerar uma carta "Bloqueio"
    :return: irá retornar um dict com o número da carta e a cor
    '''
    cornumero = random.randint(0, 40)
    cordacarta = 'vermelho'
    if cornumero < 10:
        cordacarta = 'azul'
    elif cornumero >= 10 and cornumero < 20:
        cordacarta = 'amarelo'
    elif cornumero >= 20 and cornumero < 30:
        cordacarta = 'vermelho'
    elif cornumero >= 30:
        cordacarta = 'verde'
    return {'numero': 'Bloqueio', 'cor': cordacarta}


def inverte():
    '''
    -> Irá gerar uma carta "Inverte"
    :return: irá retornar um dict com o número da carta e a cor
    '''
    cornumero = random.randint(0, 40)
    cordacarta = 'vermelho'
    if cornumero < 10:
        cordacarta = 'azul'
    elif cornumero >= 10 and cornumero < 20:
        cordacarta = 'amarelo'
    elif cornumero >= 20 and cornumero < 30:
        cordacarta = 'vermelho'
    elif cornumero >= 30:
        cordacarta = 'verde'
    return {'numero': 'Inverte', 'cor': cordacarta}


def cartanormal():
    '''
    -> Irá gerar uma carta normal, isto é, que não seja +4, +2, inverte e bloqueio
    :return: irá retornar um dict com o número da carta e a cor
    '''
    numerodacarta = random.randint(0, 9)
    cornumero = random.randint(0, 40)
    cordacarta = 'vermelho'
    if cornumero < 10:
        cordacarta = 'azul'
    elif cornumero >= 10 and cornumero < 20:
        cordacarta = 'amarelo'
    elif cornumero >= 20 and cornumero < 30:
        cordacarta = 'vermelho'
    elif cornumero >= 30:
        cordacarta = 'verde'
    return {'numero': numerodacarta, 'cor': cordacarta}


def sortearcarta(numRandom):
    '''
    -> Irá sortear uma carta de qualquer tipo
    :param numRandom: receberá um valor aleatório entre 0 á 100 (usando a biblioteca "random" e a função "randint()"
    :return: irá retornar o dict com o número da carta e a cor gerada
    '''
    if numRandom >= 90: # 10% de chance de +4
        return maisquatro()
    elif numRandom >= 75 and numRandom < 90: # 15% de chance de +2
        return maisdois()
    elif numRandom >= 64 and numRandom < 75: # 12% de Mudar cor
        return mudarcor()
    elif numRandom >= 50 and numRandom < 56: # 6% de Bloquear
        return bloqueio()
    elif numRandom >= 56 and numRandom < 64: # 6% de Inverte
        return inverte()
    else:
        return cartanormal()


def baralhoinicial(numPlayers, listJogadores, cartasIniciais):
    '''
    -> Irá sortear o baralho inicial para cada jogador
    :param numPlayers: int -> o número de players que haverá na partida (contando com os bots e os players)
    :param listJogadores: list() -> lista vazia na qual será armazenada listas contendo as cartas dos jogadores
    :param cartasIniciais: int -> o número de cartas que serão sorteadas
    :return: no return
    '''
    for jogador in range(0, numPlayers):
        baralhoPlayer = list()
        for c in range(0, cartasIniciais):
            numerorandom = random.randint(0, 100)
            carta = sortearcarta(numerorandom)
            baralhoPlayer.append(carta.copy())
        listJogadores.append(baralhoPlayer[:])


def vercartas(listJogadores, requestPlayer = 0):
    '''
    -> Irá mostrar as cartas do player requisitado (valor default = 0)
    :param listJogadores: list() -> Lista na qual foi armazenada as informações das cartas dos jogadores
    :param requestPlayer: int -> Player na qual requisitou a informação
    :return: no return
    '''
    print('-'*20)
    for c in range(0, len(listJogadores[requestPlayer])):
        if listJogadores[requestPlayer][c]['cor'] == 'amarelo':
            print('{}{}. {:<9} | Amarelo{}'.format(cores['amarelo'], c, listJogadores[requestPlayer][c]['numero'], cores['limpa']))
        elif listJogadores[requestPlayer][c]['cor'] == 'vermelho':
            print('{}{}. {:<9} | Vermelho{}'.format(cores['vermelho'], c, listJogadores[requestPlayer][c]['numero'], cores['limpa']))
        elif listJogadores[requestPlayer][c]['cor'] == 'verde':
            print('{}{}. {:<9} | Verde{}'.format(cores['verde'], c, listJogadores[requestPlayer][c]['numero'], cores['limpa']))
        elif listJogadores[requestPlayer][c]['cor'] == 'azul':
            print('{}{}. {:<9} | Azul {}'.format(cores['azul'], c, listJogadores[requestPlayer][c]['numero'], cores['limpa']))
        if listJogadores[requestPlayer][c]['cor'] == 'preto':
            print('{}. {:<9} | Especial'.format(c, listJogadores[requestPlayer][c]['numero']))


def gerarbaralhos(numerojogadores=4, cartasiniciais=7):
    '''
    -> Irá gerar os baralhos iniciais
    :return: retornará uma lista contendo o baralho de cada player
    '''
    if numerojogadores < 2:
        numerojogadores = 4
    if cartasiniciais <= 2:
        cartasiniciais = 7
    lista = list()
    baralhoinicial(numerojogadores, lista, cartasiniciais)
    return lista


def removercarta(listJogadores, requestJogador, indexCarta):
    '''
    -> Irá remover uma carta específica do baralho de certo jogador
    :param listJogadores: lista contendo as listas com o baralho de cada jogador
    :param requestJogador: jogador que requisitou o método
    :param indexCarta: o número da carta que irá ser removida
    :return: no return
    '''
    del listJogadores[requestJogador][indexCarta]


def comprarcarta(listJogadores, requestPlayer, nCartas):
    """
    -> Irá comprar um número específico de cartas e adicioná-las ao baralho do player requisitado
    :param listJogadores: lista contendo os baralhos dos jogadores
    :param requestPlayer: player que requisitou a ação
    :param nCartas: número de cartas que se deseja comprar
    :return: no return
    """
    if nCartas < 1:
        nCartas = 1
    for c in range(0, nCartas):
        numrandom = random.randint(0, 100)
        carta = sortearcarta(numrandom)
        listJogadores[requestPlayer].append(carta)


def qntcartasjogadores(listJogadores, jogadorDaVez):
    '''
    -> Irá printar na tela quantas cartas o jogador que requisitou a ação tem
    :param listJogadores: lista contendo os baralhos dos jogadores
    :param jogadorDaVez: jogador que requisitou a ação
    :return: no return
    '''
    lista = listJogadores
    for c in range(0, len(lista)):
        if c == jogadorDaVez:
            print('Você ({}jogador {}{}) possui {}{}{} carta(s).'.format(cores['amarelo'], c, cores['limpa'], cores['vermelho'], len(lista[c]), cores['limpa']), end = ' ')
        else:
            print('O jogador {}{}{} possui {}{}{} carta(s).'.format(cores['amarelo'], c, cores['limpa'], cores['vermelho'], len(lista[c]), cores['limpa']), end = ' ')
    print()


def pegarcartaindex(listJogadores, jogadorDaVez, indexCarta):
    '''
    -> Irá pegar o dicionário da carta através do índice da mesma na lista
    :param listJogadores: lista contendo os baralhos dos jogadores
    :param jogadorDaVez: jogador da vez
    :param indexCarta: índice da carta que o usuário deseja
    :return: irá retornar o dicionário da carta
    '''
    return listJogadores[jogadorDaVez][indexCarta]


class Mesa:
    def __init__(self, listaJogadores):
        self.listaJogadores = listaJogadores
       

    def cartainicial(self):
        '''
        -> Irá gerar a carta inicial
        :return: retornará uma carta normal
        '''
        return cartanormal()
    

    def sequencias(self, jogadoresHumanos = 1):
        '''
        -> Irá gerar uma lista contendo dicionários com as informações de sequencia (quem é o player 0, 1, 2, etc...)
        :param jogadoresHumanos: int -> quantos jogadores humanos, ou seja, que não são IA estão jogando
        :return: retornará uma lista contendo dicionários com as informações de sequencia
        '''
        if jogadoresHumanos > len(self.listaJogadores):
            jogadoresHumanos = len(self.listaJogadores)
        lista = list()
        dictSequencias = dict()
        for nJogadorReal in range(0, jogadoresHumanos):
            dictSequencias = {f'{nJogadorReal}': True}
            lista.append(dictSequencias.copy())
        for nJogador in range(jogadoresHumanos, len(self.listaJogadores)):
            dictSequencias = {f'{nJogador}': False}
            lista.append(dictSequencias.copy())
        return lista
    

    def invertersequencias(self, sequenciaDaMesa):
        '''
        -> Irá inverter a sequência de jogadores
        :param sequencias: Uma variavél contendo a sequência do jogo. A variavél pode ser declarada dentro da classe
        :return: no return
        '''
        return sequenciaDaMesa[::-1]
    

    def quantidadedeplayers(self):
        '''
        -> Irá retornar o valor com a quantidade de jogadores que estão jogando
        :return: int -> retornará o valor com a quantidade de players que estão jogando
        '''
        return len(self.listaJogadores)
    

    def playerinicial(self, quantidadedeplayers):
        '''
        -> Irá sortear o jogador inicial
        :return: int -> retornará o número do player inicial
        '''
        return random.randint(0, quantidadedeplayers - 1)
    

    def inverter(self):
        '''
        -> Irá gerar um valor booleano dizendo que o baralho está invertido
        :return: bool -> True
        '''
        return True
    

    def desinverter(self):
        '''
        -> Irá gerar um valor booleano dizendo que o baralho está desinvertido
        :return: bool -> False
        '''
        return False


    def proximoplayer(self, invertido, playerdavez, quantidadedeplayers, pularplayer):
        '''
        -> Irá definir qual será o próximo jogador á jogar
        :param invertido: váriavel booleana dizendo se o jogo está invertido ou não
        :param playerdavez: jogador que está jogando
        :param quantidadedeplayers: quantidade de players que estão jogando
        :param pularplayer: quantidade de jogadores que serão pulados (1, 2, 3, etc.)
        :return: irá retornar qual um integer dizendo qual será o próximo jogador
        '''
        quantidade_de_pulos = pularplayer
        proximojogador = 0
        if invertido == False:
            if playerdavez + pularplayer >= quantidadedeplayers:
                return (playerdavez + pularplayer) - quantidadedeplayers
            else:
                return playerdavez + pularplayer
        else:
            if playerdavez - pularplayer < 0:
                while True:
                    if playerdavez - 1 < 0:
                        proximojogador = quantidadedeplayers - 1
                        quantidade_de_pulos -= 1
                    else:
                        proximojogador = playerdavez - 1
                        quantidade_de_pulos -= 1
                    if quantidade_de_pulos <= 0:
                        break
                    else:
                        pass
                return proximojogador
            else:
                return playerdavez - pularplayer


    def acao(self, cores):
        '''
        -> Irá printar um menu de jogar
        :param cores: dicionário contendo as cores
        :return: irá retornar um int na qual condiz com a escolhda do jogador
        '''
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
    
    
    def printarcartamesa(self, cartamesa):
        '''
        Irá printar a carta na mesa de forma formatada
        :param cartamesa: váriavel contendo a carta na mesa
        :return: irá retornar uma string dizendo formatada
        '''
        if cartamesa['cor'] == 'vermelho':
            return '{}{} | Vermelho{}'.format(cores['vermelho'], cartamesa['numero'], cores['limpa'])
        elif cartamesa['cor'] == 'amarelo':
            return '{}{} | Amarelo{}'.format(cores['amarelo'], cartamesa['numero'], cores['limpa'])
        elif cartamesa['cor'] == 'verde':
            return '{}{} | Verde{}'.format(cores['verde'], cartamesa['numero'], cores['limpa'])
        elif cartamesa['cor'] == 'azul':
            return '{}{} | Azul{}'.format(cores['azul'], cartamesa['numero'], cores['limpa'])
        else:
            return '{} | Especial'.format(cartamesa['numero'])
    

    def cartasjogavel(self, cartamesa, jogadorDaVez, somatoriadecompra, somatoriacarta, corescolhida, corescolhidaCor):
        '''
        -> Irá gerar um valor booleano dizendo se há ou não cartas jogáveis no baralho do player
        :param cartamesa: váriavel contendo a carta na mesa
        :param jogadorDaVez: váriavel integer dizendo o jogador da vez
        :param somatoriadecompra: somatória de compras de cartas
        :param somatoriacarta: váriavel contendo o tipo de carta que está fazendo a somatória
        :param corescolhida: váriavel booleana na qual diz se há uma cor escolhida para ser jogada
        :param corescolhidaCor: váriavel dizendo a cor específicada
        :return: irá retornar um valor booleano dizendo se há ou não cartas jogáveis
        '''
        if corescolhida == True:
            cartasjogaveis = False
            for c in range(0, len(self.listaJogadores[jogadorDaVez])):
                if self.listaJogadores[jogadorDaVez][c]['cor'] == corescolhidaCor or self.listaJogadores[jogadorDaVez][c]['numero'] == 'Mudar Cor' or self.listaJogadores[jogadorDaVez][c]['numero'] == '+4':
                    cartasjogaveis = True
                else:
                    pass
            return cartasjogaveis
        else:
            cartasjogaveis2 = False
            for c in range(0, len(self.listaJogadores[jogadorDaVez])):
                if self.listaJogadores[jogadorDaVez][c]['cor'] == cartamesa['cor'] or self.listaJogadores[jogadorDaVez][c]['numero'] == cartamesa['numero'] or self.listaJogadores[jogadorDaVez][c]['cor'] == 'preto':
                    cartasjogaveis2 = True
                else:
                    pass
            return cartasjogaveis2
        if somatoriadecompra > 0:
            cartasjogaveis3 = False
            for c in range(0, len(self.listaJogadores[jogadorDaVez])):
                if self.listaJogadores[jogadorDaVez][c]['numero'] == somatoriacarta:
                    cartasjogaveis3 = True
                else:
                    pass
            return cartasjogaveis3


    def cartajogavel(self, cartamesa, cartajogada, somatoriadecompra, somatoriacarta, jogadordavez, corescolhida, corescolhidaCor):
        '''
        -> Irá retornar um valor booleano dizendo se a carta escolhida pelo player é jogável
        :param cartamesa: váriavel contendo a carta na mesa
        :param cartajogada: carta jogável pelo player
        :param somatoriadecompra: váriavel integer contendo a quantidade de somatórias de cartas para comprar
        :param somatoriacarta: váriavel dizendo o tipo da carta para somatória de compra
        :param jogadordavez: váriavel integer dizendo o jogador da vez
        :param corescolhida: váriavel booleana dizendo se há cor escolhida para ser jogada
        :param corescolhidaCor: váriavel dizendo a cor escolhida para ser jogada
        :return: irá retornar um valor booleano
        '''
        if self.listaJogadores[jogadordavez][cartajogada]['numero'] == '+4':
            if somatoriadecompra > 0 and somatoriacarta != '+4':
                return False
            else:
                return True
        elif self.listaJogadores[jogadordavez][cartajogada]['numero'] == 'Mudar Cor' and somatoriadecompra == 0:
            return True
        elif self.listaJogadores[jogadordavez][cartajogada]['numero'] == 'Mudar Cor' and somatoriadecompra > 0:
            return False
        elif self.listaJogadores[jogadordavez][cartajogada]['numero'] == cartamesa['numero'] or self.listaJogadores[jogadordavez][cartajogada]['cor'] == cartamesa['cor']:
            if somatoriadecompra > 0:
                if self.listaJogadores[jogadordavez][cartajogada]['numero'] == cartamesa['numero']:
                    return True
                else:
                    return False
            else:
                if corescolhida == True:
                    if self.listaJogadores[jogadordavez][cartajogada]['cor'] == corescolhidaCor:
                        return True
                    else:
                        return False
                else:
                    return True
        elif self.listaJogadores[jogadordavez][cartajogada]['numero'] != cartamesa['numero'] or self.listaJogadores[jogadordavez][cartajogada]['cor'] != cartamesa['cor']:
            return False
        else:
            return 'ERRO: Condição não presente no código.'


    def jogarcartamenu(self, jogadordavez, cores):
        '''
        -> Irá fazer um input na qual o jogador irá ter que digitar a carta que deseja jogar
        :param jogadordavez: váriavel integer dizendo o jogador da vez
        :param cores: dicionário com cores
        :return: irá retornar o integer do índice da carta
        '''
        while True:
            try:
                carta = int(input('Por favor, digite a carta que deseja jogar: '.format(cores['vermelho'], cores['limpa'])))
                if carta > -1 and carta < len(self.listaJogadores[jogadordavez]):
                    break
            except:
                pass
        return carta


    def cartasinvalidas_loop(self, invertido, jogadordavez, quantidadejogadores, somatoriadecompra, cartanamesa, mesa_printarcartamesa):
        '''
        -> Caso ocorra um erro de cartas iválidas, este loop será acionado
        :param invertido: váriavel booleana dizendo se o jogo está invertido
        :param jogadordavez: váriavel integer dizendo o jogador da vez
        :param quantidadejogadores: váriavel contendo o número de jogadores
        :param somatoriadecompra: váriavel dizendo a somatória de cartas para serem compradas
        :param cartanamesa: váriavel contendo o dicionário com a carta na mesa
        :param mesa_printarcartamesa: função dizendo para printar a carta na mesa
        :return: retornará um integer dando uma opção válida para ser jogada
        '''
        print()
        print('Você não possui nenhuma carta jogável. Escolha outra opção:')
        print('''1. Jogar uma carta
2. Comprar carta(s)
3. Ver o seu baralho e a quantidade de cartas de outros jogadores
4. Encerrar o jogo''')
        escolhaloop = str(input('Digite sua opção: '))[0]
        while escolhaloop.isnumeric() == False:
            escolhaloop = str(input('Digite uma opção válida: '))[0]
        escolhaloopint = int(escolhaloop)
        while escolhaloopint < 1 and escolhaloopint > 4:
            escolhaloop = str(input('Digite uma opção válida: '))
            while escolhaloop.isnumeric() == False:
                escolhaloop = str(input('Digite uma opção válida: '))
            escolhaloopint = int(escolhaloop)
        if escolhaloopint == 1:
            print('Você não possui cartas válidas.')
        elif escolhaloopint == 2:
            if somatoriadecompra == 0:
                comprarcarta(self.listaJogadores, jogadordavez, 1)
                print('Você comprou 1 carta.')
            if somatoriadecompra > 0:
                comprarcarta(self.listaJogadores, jogadordavez, somatoriadecompra)
                print(f'Você comprou {somatoriadecompra} cartas.')
                somatoriadecompra = 0
            jogadordavez = self.proximoplayer(invertido, jogadordavez, quantidadejogadores, 1)
            return 2
        elif escolhaloopint == 3:
            vercartas(self.listaJogadores)
            qntcartasjogadores(self.listaJogadores, jogadordavez)
            print()
            print('A carta na mesa é: {}'.format(mesa_printarcartamesa), end = ' | ')
            return 3
        elif escolhaloopint == 4:
            return 4
    

    def printarnomedacor(self, corescolhidaCor, cores):
        '''
        -> Irá printar o nome da cor escolhida de forma formatada
        :param corescolhidaCor: váriavel contendo a cor escolhida
        :param cores: dicionário de cores
        :return: irá retornar uma string formatada com o nome da cor
        '''
        if corescolhidaCor == 'azul':
            return '{}Azul{}'.format(cores['azul'], cores['limpa'])
        elif corescolhidaCor == 'verde':
            return '{}Verde{}'.format(cores['verde'], cores['limpa'])
        elif corescolhidaCor == 'amarelo':
            return '{}Amarelo{}'.format(cores['amarelo'], cores['limpa'])
        elif corescolhidaCor == 'vermelho':
            return '{}Vermelho{}'.format(cores['vermelho'], cores['limpa'])
        else:
            return corescolhidaCor


class Cartas:
    def __init__(self, listaJogadores):
        self.listaJogadores = listaJogadores


    def possuicartanumero(self, requestPlayer, cartanumero):
        '''
        -> Irá gerar um valor booleano dizendo se o jogador possuí uma carta de 'x' número
        :param requestPlayer: baralho que será analisado
        :param cartanumero: número da carta que se deseja encontrar
        :return: True/False
        '''
        possuicarta = False
        for c in range(0, len(self.listaJogadores[requestPlayer])):
            if self.listaJogadores[requestPlayer][c]['numero'] == cartanumero:
                possuicarta = True
            else:
                pass
        return possuicarta
    

    def menu_cores(self, cores):
        '''
        -> Irá criar um input na qual o usuário terá que escolher a cor que desejá jogar
        :param cores: dicionário contendo as cores
        :return: irá retornar um integer na qual condiz com a cor escolhida
        '''
        print('Escolha uma cor: \n{}1. Vermelho{}\n{}2. Amarelo{}\n{}3. Azul{}\n{}4. Verde{}'.format(cores['vermelho'], cores['limpa'], cores['amarelo'], cores['limpa'], cores['azul'], cores['limpa'], cores['verde'], cores['limpa']))
        cor = str(input('Digite o número da cor: '))
        while cor not in '1234':
            cor = str(input('Valor inválido. Por favor, digite o número da cor: '))
        corint = int(cor)
        return corint
    

    def efeito_mudarcor(self, cores):
        '''
        -> Irá associar as cores em integer com as cores em string
        :param cores: dicionário de cores
        :return: irá retornar uma string dizendo a cor escolhida no menu_cores
        '''
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
    def __init__(self, debug_mode):
        self.debug_mode = debug_mode


    def printar(msg):
        if self.debug_mode == True:
            print(msg)
        else:
            pass