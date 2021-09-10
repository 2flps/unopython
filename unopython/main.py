# pylint: disable=unused-import

from uno import *
from time import sleep
import file_configs

# Configs from 'file_configs.py'
file_configs.escrever() # If the file does not exist, it will generate one
debug = file_configs.debug() # Will decides if debug mode is on/off
debug_ai_joga_cartas = file_configs.debug_ai_joga_cartas() # If it is set false, then the bots will simply skip their turns based on the choice making of card playing
jogadores_iniciais_qnt = file_configs.qnt_jogadores() # Will set the amount of players in the match
cartas_iniciais_qnt = file_configs.cartas_iniciais() # Will set the amount of cards each player will receive in the beginning
ai_habilitada = file_configs.ai() # If the Ai is off, it will simply skip it's turn
uno_intervalo = file_configs.uno_intervalo() # This will set the interval the player will have to type "Uno" in the prompt
debug_condicoes = file_configs.debug_condicoes() # If it is set true, then for each "card playing condition" the Ai face, a message will be printed

baralho = gerar_baralhos(jogadores_iniciais_qnt, cartas_iniciais_qnt) # This variable will store the deck of all players inside a dictionare
mesa = Mesa(baralho) # Calls the class 'mesa'
cartas = Cartas(baralho) # Calls the class 'cartas'
quantidade_de_jogadores = mesa.quantidade_de_players() # This variable will store the amount of players in the match
jogadores = mesa.sequencias(1) # This will set the order of playing
primeiro_jogador = mesa.player_inicial(quantidade_de_jogadores) # Calls the function 'player_inicial' to generate the first player for the first turn
jogador_da_vez = primeiro_jogador # This variable stores the number (integer) of the current turn player. When the game starts, the current player will always be the result of 'player_inicial' function
invertido = False # This variable stores a boolean which will tell if the game is clockwise or anticlockwise
carta_na_mesa = mesa.carta_inicial() # This variable stores a dictionare containing the current turn card. This is an example of a card -> {'cor': 'especial', 'numero': '+4'} 
somatoria_de_compra = 0 # If there is an ongoing "buy-type" card (+4 or +2), then this variable will store the purchase sum that the unlucky one will have to buy
somatoria_carta = '0' # This variable will store the "buy-type" card (+4 or +2). This '0' data is just a placeholder :)
cor_escolhida = False # If some player choosed a color with a "change-color-type" card ('Change color' or +4) then the variable will set "True" until someone buy a card
cor_escolhida_cor = '' # This variable stores the choosed color for the variable above
vencedor = False # If there's a winner, this variable will set True
vencedor_num = 0 # This variable stores the index of the winner
class_debug = Debug(baralho, cores) # Calls the class 'debug'
class_ai = Ai(baralho, cores) # Calls the class 'Ai'

# Intro <- This section will only prints the introduction. Nothing else
print('---UNO---')
print(f'Há {quantidade_de_jogadores} jogadores na mesa.')
print('')
print('Sorteando as cartas...')
if jogadores[primeiro_jogador]['{}'.format(primeiro_jogador)] == True:
    print('O primeiro jogador é você!\n')
else:
    print(f'O primeiro jogador é o Jogador {primeiro_jogador}!\n')


# This variable below stores the choice the player will take during the game
acao = 1

while acao > 0 and acao < 4: # As long as the player choice stood more than 0 and less than 4, the game/console will not shutdown itself
    if debug == True: # If debug is set True, then it will print each player deck each turn
        for c in range(0, 4):
            print(baralho[c])
    if checar_ganhador(baralho, quantidade_de_jogadores) == True: # This will check if there is a winner in the current game
        vencedor = True
        vencedor_num = ganhador(baralho, quantidade_de_jogadores)
    if vencedor == True: # If there is a winner, then this loop will break and a winner message will be displayed
        break
    else: # If there is no winner, then the game will simply run
        if jogadores[jogador_da_vez][f'{jogador_da_vez}'] == True: # This section covers the player controlled part
            escolha_loop = 0 # This variable stores an integer. It's usage is explained below
            lock_jogar = False # If there is none available card to be played, this variable will be set True
            printar_cartas_mesa = mesa.printar_carta_mesa(carta_na_mesa) # Calls the 'printar_carta_mesa' function, which prints the current player cards in a colorful way (it's not good for me, due to my colorblindness)
            print('===============================================\nÉ a sua vez de jogar. Estas são as suas cartas:')
            ver_cartas(baralho) # Calls the 'ver_cartas' function, which prints the amount of cards of each player
            qnt_cartas_jogadores(baralho, jogador_da_vez) # It seeems that this function has the pretty same workability that the 'printar_carta_mesa' has. Idk why :|
            print() # This just simply prints a blank message, because I'm too lazy to use \n
            print('A carta na mesa é: {}'.format(mesa.printar_carta_mesa(carta_na_mesa)), end = ' | ') # This prints the card on the desk in a colorful way
            if somatoria_de_compra > 0: # This section covers the Purchase Sum that will be printed.
                if somatoria_carta == '+4':
                    print('Há {} carta(s) de +4, totalizando uma somatória de compra de {} cartas.'.format(somatoria_de_compra // 4, somatoria_de_compra)) # If the purchase sum card is +4, it will print a +4 message
                else:
                    print('Há {} carta(s) de +2, totalizando uma somatória de compra de {} cartas.'.format(somatoria_de_compra // 2, somatoria_de_compra)) # If the purchase sum card is +2, it will print a +2 message
            else:
                pass
            if cor_escolhida == False:
                print()
            else:
                print('Cor escolhida: {}'.format(mesa.printar_nome_cor(cor_escolhida_cor, cores))) # If there's a chosen color, then this will print the chosen one
            print()
            acao = mesa.acao(cores) # This function will print the user menu.
            if acao == 1: # If the user action is 1, then will execute this block
                while mesa.cartas_jogavel(carta_na_mesa, jogador_da_vez, somatoria_de_compra, somatoria_carta, cor_escolhida, cor_escolhida_cor, debug) == False: # If there's no available card to play, then it will starts a loop
                    escolha_loop = mesa.cartas_invalidas_loop(cores)
                    if escolha_loop == 2:
                        if somatoria_de_compra == 0: # If the purchase sum is 0, then it will purchase just one card
                            comprar_carta(baralho, jogador_da_vez, 1)
                            print('Você comprou 1 carta.')
                        if somatoria_de_compra > 0: # If the purchase sum is more than 0, then it will purchase the whole purchase sum
                            comprar_carta(baralho, jogador_da_vez, somatoria_de_compra)
                            print(f'Você comprou {somatoria_de_compra} cartas.')
                            somatoria_de_compra = 0
                        jogador_da_vez = mesa.proximo_player(invertido, jogador_da_vez, quantidade_de_jogadores, 1)
                        lock_jogar = True
                        break
                    if escolha_loop == 3:
                        if acao == 3: # If the chosen action is 3, then it prints the amount of cards each player have
                            print('--Ver Cartas--')
                            print()
                            print('A carta na mesa é: {}'.format(mesa.printar_carta_mesa(carta_na_mesa)), end = ' | ')
                            if somatoria_de_compra > 0:
                                if somatoria_carta == '+4':
                                    print('Há {} carta(s) de +4, totalizando uma somatória de compra de {} cartas.'.format(somatoria_de_compra // 4, somatoria_de_compra))
                                else:
                                    print('Há {} carta(s) de +2, totalizando uma somatória de compra de {} cartas.'.format(somatoria_de_compra // 2, somatoria_de_compra))
                            else:
                                pass
                            if cor_escolhida == False:
                                print()
                            else:
                                print('Cor escolhida: {}'.format(mesa.printar_nome_cor(cor_escolhida_cor, cores)))
                            print()
                            break
                    if escolha_loop == 4:
                        break
                if escolha_loop == 3 or escolha_loop == 4: # This will break the loop if the user choose option 3 or 4. Otherwise the loop will just continues
                    break
                elif escolha_loop == 2:
                    jogador_da_vez = mesa.proximo_player(invertido, jogador_da_vez, quantidade_de_jogadores, 1)
                else:
                    pass
                if lock_jogar == False: # If there's an available card to be played then this block will be executed, otherwise it will just ignore
                    carta_jogar = mesa.jogar_carta_menu(jogador_da_vez, cores, lock_jogar) # This functions call the "Play card" menu, where the user will choose a card based on it's index to play
                    while mesa.carta_jogavel(carta_na_mesa, carta_jogar, somatoria_de_compra, somatoria_carta, jogador_da_vez, cor_escolhida, cor_escolhida_cor, debug) == False: # If the chosen card is not playable, then it will starts this loop
                        print('Esta carta é inválida')
                        carta_jogar = mesa.jogar_carta_menu(jogador_da_vez, cores, lock_jogar)
                    if cor_escolhida == True: # If there's a chosen color and a player plays a card, then the "chosen color" variable will set False
                        cor_escolhida = False
                    if debug == True: # Debug things
                        print("""Carta escolhida things:\nCarta jogável: {}\nCarta na mesa: {}\nCarta jogada: {}\nSomatória de compra: {}\nSomatória carta: {}\nJogador da vez: {}\nCor escolhida: {}\nCor escolhida_cor: {}""".format(mesa.carta_jogavel(carta_na_mesa, carta_jogar, somatoria_de_compra, somatoria_carta, jogador_da_vez, cor_escolhida, cor_escolhida_cor), carta_na_mesa, carta_jogar, somatoria_de_compra, somatoria_carta, jogador_da_vez, cor_escolhida, cor_escolhida_cor))
                    carta_na_mesa = pegar_carta_index(baralho, jogador_da_vez, carta_jogar) # This will set the current turn card to be the one the player selected using the 'pegar_carta_index' function
                    remover_carta(baralho, jogador_da_vez, carta_jogar) # This will remove the card the player selected
                    #This section below will cover the Chosen color part and the Purchase sum part
                    if carta_na_mesa['numero'] == 'Mudar Cor' or carta_na_mesa['numero'] == '+4':
                        cor_escolhida = True
                        cor_escolhida_cor = cartas.efeito_mudar_cor(cores)
                    if carta_na_mesa['numero'] == '+4':
                        somatoria_de_compra += 4
                        somatoria_carta = '+4'
                    if carta_na_mesa['numero'] == '+2':
                        somatoria_de_compra += 2
                        somatoria_carta = '+2'
                    if carta_na_mesa['numero'] == 'Inverte':
                        if invertido == False:
                            invertido = mesa.inverter()
                        else:
                            invertido = mesa.desinverter()
                    if len(baralho[jogador_da_vez]) == 1: # This will run the "Uno" part, when there's only one card left in the deck
                        menu_uno = mesa.uno_menu(uno_intervalo, cores)
                        if menu_uno == False:
                            pass
                        else:
                            comprar_carta(baralho, jogador_da_vez, 2)
                            print('{}Você comprou 2 cartas pois digitou "Uno" errado ou simplesmente não digitou.')
                    if len(baralho[jogador_da_vez]) == 0:
                        vencedor = True
                        vencedor_num = jogador_da_vez
                    else:
                        pass
                    if carta_na_mesa['numero'] == 'Bloqueio':
                        jogador_da_vez = mesa.proximo_player(invertido, jogador_da_vez, quantidade_de_jogadores, 2) # If some player use the Block card, then it will skip 2 person. Otherwise it will just skip 1.
                    else:
                        jogador_da_vez = mesa.proximo_player(invertido, jogador_da_vez, quantidade_de_jogadores, 1)
            if acao == 2: # If the chosen action is 2, then the player will purchase one or more cards
                if somatoria_de_compra == 0: # If the purchase sum is 0, then it will purchase just one card
                    comprar_carta(baralho, jogador_da_vez, 1)
                    print('Você comprou 1 carta.')
                if somatoria_de_compra > 0: # If the purchase sum is more than 0, then it will purchase the whole purchase sum
                    comprar_carta(baralho, jogador_da_vez, somatoria_de_compra)
                    print(f'Você comprou {somatoria_de_compra} cartas.')
                    somatoria_de_compra = 0
                jogador_da_vez = mesa.proximo_player(invertido, jogador_da_vez, quantidade_de_jogadores, 1)
            if acao == 3: # If the chosen action is 3, then it prints the amount of cards each player have
                print('--Ver Cartas--')
                print()
                print('A carta na mesa é: {}'.format(mesa.printar_carta_mesa(carta_na_mesa)), end = ' | ')
                if somatoria_de_compra > 0:
                    if somatoria_carta == '+4':
                        print('Há {} carta(s) de +4, totalizando uma somatória de compra de {} cartas.'.format(somatoria_de_compra // 4, somatoria_de_compra))
                    else:
                        print('Há {} carta(s) de +2, totalizando uma somatória de compra de {} cartas.'.format(somatoria_de_compra // 2, somatoria_de_compra))
                else:
                    pass
                if cor_escolhida == False:
                    print()
                else:
                    print('Cor escolhida: {}'.format(mesa.printar_nome_cor(cor_escolhida_cor, cores)))
                print()
        if jogadores[jogador_da_vez][f'{jogador_da_vez}'] == False: # This section coverts the Ai controlled part
            if ai_habilitada == False: # If the Ai is turned off, then it simply skips the Ai turn
                print('Ai Desabilitada. Vez do Bot #{}. Pulando vez'.format(jogador_da_vez))
                jogador_da_vez = mesa.proximo_player(invertido, jogador_da_vez, quantidade_de_jogadores, 1)            
            else: # This section covers the "Ai card playing decision" part
                file_configs.printar_condicoes('Condição 1. Somatória de Compra == 0 ({}) e Única carta jogável == +4 {}'.format(somatoria_de_compra, class_ai.unica_carta_jogavel(baralho, jogador_da_vez, '+4', carta_na_mesa, somatoria_de_compra, somatoria_carta, cor_escolhida, cor_escolhida_cor)), debug_condicoes)
                if mesa.cartas_jogavel(carta_na_mesa, jogador_da_vez, somatoria_de_compra, somatoria_carta, cor_escolhida, cor_escolhida_cor, False) == True: # First condition. If the purchase amount is equal to 0 and the only playable card is +4, then the Ai will simply buy one card
                    if somatoria_de_compra == 0 and class_ai.unica_carta_jogavel(baralho, jogador_da_vez, '+4', carta_na_mesa, somatoria_de_compra, somatoria_carta, cor_escolhida, cor_escolhida_cor) == True:
                        if debug_ai_joga_cartas == True:
                            comprar_carta(baralho, jogador_da_vez, 1)
                            print(f'Jogador #{jogador_da_vez} comprou uma carta.')
                        debug_printar('Somatória de compra == 0 e única carta jogável é +4. Ação = Comprar uma carta', debug)
                        jogador_da_vez = mesa.proximo_player(invertido, jogador_da_vez, quantidade_de_jogadores, 1)
                    else:
                        file_configs.printar_condicoes('Condição 2. Somatória de Compra > 0 ({}) e possui carta == carta somatória {}'.format(somatoria_de_compra, cartas.possui_carta_numero(jogador_da_vez, somatoria_carta)), debug_condicoes)
                        if somatoria_de_compra > 0 and cartas.possui_carta_numero(jogador_da_vez, somatoria_carta) == True: # Second condition. If the purchase amount is > 0 and Ai has an playable card, then it will play
                            debug_printar('Somatória de compra > 0 e Jogador possuí carta == Somatória carta', debug)
                            if debug_ai_joga_cartas == True:
                                indexcartadasomatoria = class_ai.selecionar_carta_random_index(baralho, jogador_da_vez, somatoria_carta)
                                if baralho[jogador_da_vez][indexcartadasomatoria]['numero'] == '+4':
                                    somatoria_de_compra += 4
                                    somatoria_carta = '+4'
                                    cor_escolhida = True
                                    cor_escolhida_cor = class_ai.cor_majoritaria(baralho, jogador_da_vez, False)
                                elif baralho[jogador_da_vez][indexcartadasomatoria]['numero'] == '+2':
                                    somatoria_de_compra += 2
                                    somatoria_carta = '+2'
                                    if cor_escolhida == True:
                                        cor_escolhida = False
                                    else:
                                        pass
                                else:
                                    raise ValueError('O número do índice da carta escolhida difere de +2 e +4. O código está certo?')
                                carta_na_mesa = pegar_carta_index(baralho, jogador_da_vez, indexcartadasomatoria)
                                remover_carta(baralho, jogador_da_vez, indexcartadasomatoria)
                                print(f'Jogador #{jogador_da_vez} jogou a carta: {mesa.printar_carta_mesa(carta_na_mesa)}')
                            jogador_da_vez = mesa.proximo_player(invertido, jogador_da_vez, quantidade_de_jogadores, 1)
                        else:
                            file_configs.printar_condicoes('Condição 3. Tamanho do baralho do próximo player < 3 ({}).'.format(class_ai.tamanho_baralho(baralho, mesa.proximo_player(invertido, jogador_da_vez, quantidade_de_jogadores, 1), False)), debug_condicoes)
                            if class_ai.tamanho_baralho(baralho, mesa.proximo_player(invertido, jogador_da_vez, quantidade_de_jogadores, 1), False) < 3: # Third condition. If the next player has less than 3 cards on its deck, then it will choose one subcondition.
                                if cartas.possui_carta_numero(jogador_da_vez, '+4') == True and class_ai.possui_carta_jogavel(baralho, jogador_da_vez, '+4', carta_na_mesa, somatoria_de_compra, somatoria_carta, cor_escolhida, cor_escolhida_cor) == True: # First subcondition. If Ai has +4 and is playable, then it will play it
                                    debug_printar('Tamanho do baralho do próximo player < 3 cartas. Bot possui carta +4.', debug)
                                    if debug_ai_joga_cartas == True:
                                        index_carta_selecionada = class_ai.selecionar_carta_random_index(baralho, jogador_da_vez, '+4')
                                        carta_na_mesa = pegar_carta_index(baralho, jogador_da_vez, index_carta_selecionada)
                                        remover_carta(baralho, jogador_da_vez, index_carta_selecionada)
                                        somatoria_de_compra += 4
                                        somatoria_carta = '+4'
                                        cor_escolhida = True
                                        cor_escolhida_cor = class_ai.cor_majoritaria(baralho, jogador_da_vez, False)
                                        print(f'Jogador #{jogador_da_vez} jogou a carta: {mesa.printar_carta_mesa(carta_na_mesa)}')
                                    jogador_da_vez = mesa.proximo_player(invertido, jogador_da_vez, quantidade_de_jogadores, 1)
                                elif cartas.possui_carta_numero(jogador_da_vez, '+2') == True and class_ai.possui_carta_jogavel(baralho, jogador_da_vez, '+2', carta_na_mesa, somatoria_de_compra, somatoria_carta, cor_escolhida, cor_escolhida_cor) == True: # Second subcondition. If Ai has +2 and is playable, then it will play it
                                    debug_printar('Tamanho do baralho do próximo player < 3 cartas. Bot possui carta +2.', debug)
                                    if debug_ai_joga_cartas == True:
                                        index_carta_selecionada = class_ai.selecionar_carta_random_index(baralho, jogador_da_vez, '+2')
                                        carta_na_mesa = pegar_carta_index(baralho, jogador_da_vez, index_carta_selecionada)
                                        remover_carta(baralho, jogador_da_vez, index_carta_selecionada)
                                        somatoria_de_compra += 2
                                        somatoria_carta = '+2'
                                        if cor_escolhida == True:
                                            cor_escolhida = False
                                        else:
                                            pass
                                        print(f'Jogador #{jogador_da_vez} jogou a carta: {mesa.printar_carta_mesa(carta_na_mesa)}')
                                    jogador_da_vez = mesa.proximo_player(invertido, jogador_da_vez, quantidade_de_jogadores, 1)
                                elif cartas.possui_carta_numero(jogador_da_vez, 'Bloqueio') == True and class_ai.possui_carta_jogavel(baralho, jogador_da_vez, 'Bloqueio', carta_na_mesa, somatoria_de_compra, somatoria_carta, cor_escolhida, cor_escolhida_cor) == True: # Third subcondition. If Ai has skip and is playable, then it will play it
                                    debug_printar('Tamanho do baralho do próximo player < 3 cartas. Bot possui carta Bloqueio.', debug)
                                    if debug_ai_joga_cartas == True:
                                        index_carta_selecionada = class_ai.selecionar_carta_random_index(baralho, jogador_da_vez, 'Bloqueio')
                                        carta_na_mesa = pegar_carta_index(baralho, jogador_da_vez, index_carta_selecionada)
                                        remover_carta(baralho, jogador_da_vez, index_carta_selecionada)
                                        if cor_escolhida == True:
                                            cor_escolhida = False
                                        else:
                                            pass
                                        print(f'Jogador #{jogador_da_vez} jogou a carta: {mesa.printar_carta_mesa(carta_na_mesa)}')
                                    jogador_da_vez = mesa.proximo_player(invertido, jogador_da_vez, quantidade_de_jogadores, 2)
                                elif cartas.possui_carta_numero(jogador_da_vez, 'Inverte') == True and class_ai.possui_carta_jogavel(baralho, jogador_da_vez, 'Inverte', carta_na_mesa, somatoria_de_compra, somatoria_carta, cor_escolhida, cor_escolhida_cor) == True: # Fourth subcondition. If Ai has reverse and is playable, then it will play it
                                    debug_printar('Tamanho do baralho do próximo player < 3 cartas. Bot possui carta Inverte.', debug)
                                    if debug_ai_joga_cartas == True:
                                        index_carta_selecionada = class_ai.selecionar_carta_random_index(baralho, jogador_da_vez, 'Inverte')
                                        carta_na_mesa = pegar_carta_index(baralho, jogador_da_vez, index_carta_selecionada)
                                        remover_carta(baralho, jogador_da_vez, index_carta_selecionada)
                                        if invertido == False:
                                            invertido = True
                                        else:
                                            invertido = False
                                        if cor_escolhida == True:
                                            cor_escolhida = False
                                        else:
                                            pass
                                        print(f'Jogador #{jogador_da_vez} jogou a carta: {mesa.printar_carta_mesa(carta_na_mesa)}')
                                    jogador_da_vez = mesa.proximo_player(invertido, jogador_da_vez, quantidade_de_jogadores, 1)
                                else: # Fifth condition. If Ai has any normal card, then it will play it
                                    debug_printar('Tamanho do baralho do próximo player < 3 cartas. Jogando qualquer carta normal aleatória.', debug)
                                    if debug_ai_joga_cartas == True:
                                        index_carta_selecionada = class_ai.selecionar_carta_normal_random(baralho, jogador_da_vez, carta_na_mesa, somatoria_carta, somatoria_de_compra, cor_escolhida, cor_escolhida_cor)
                                        carta_na_mesa = pegar_carta_index(baralho, jogador_da_vez, index_carta_selecionada)
                                        remover_carta(baralho, jogador_da_vez, index_carta_selecionada)
                                        if cor_escolhida == True:
                                            cor_escolhida = False
                                        else:
                                            pass
                                        print(f'Jogador #{jogador_da_vez} jogou a carta: {mesa.printar_carta_mesa(carta_na_mesa)}')
                                    jogador_da_vez = mesa.proximo_player(invertido, jogador_da_vez, quantidade_de_jogadores, 1)
                            else:
                                file_configs.printar_condicoes('Condição 4. Possui Bloqueio ({}) e é jogável ({})'.format(cartas.possui_carta_numero(jogador_da_vez, 'Bloqueio'), class_ai.possui_carta_jogavel(baralho, jogador_da_vez, 'Bloqueio', carta_na_mesa, somatoria_de_compra, somatoria_carta, cor_escolhida, cor_escolhida_cor)), debug_condicoes)
                                if cartas.possui_carta_numero(jogador_da_vez, 'Bloqueio') == True and class_ai.possui_carta_jogavel(baralho, jogador_da_vez, 'Bloqueio', carta_na_mesa, somatoria_de_compra, somatoria_carta, cor_escolhida, cor_escolhida_cor) == True: # Fourth condition. If Ai has skip and is playable, then it will play it
                                    debug_printar('Jogar Bloqueio.', debug)
                                    if debug_ai_joga_cartas == True:
                                        index_carta_selecionada = class_ai.selecionar_carta_random_index(baralho, jogador_da_vez, 'Bloqueio')
                                        carta_na_mesa = pegar_carta_index(baralho, jogador_da_vez, index_carta_selecionada)
                                        remover_carta(baralho, jogador_da_vez, index_carta_selecionada)
                                        if cor_escolhida == True:
                                            cor_escolhida = False
                                        else:
                                            pass
                                        print(f'Jogador #{jogador_da_vez} jogou a carta: {mesa.printar_carta_mesa(carta_na_mesa)}')
                                    jogador_da_vez = mesa.proximo_player(invertido, jogador_da_vez, quantidade_de_jogadores, 2)
                                else:
                                    file_configs.printar_condicoes('Condição 5. Possui Inverte ({}) e é jogável ({})'.format(cartas.possui_carta_numero(jogador_da_vez, 'Inverte'), class_ai.possui_carta_jogavel(baralho, jogador_da_vez, 'Inverte', carta_na_mesa, somatoria_de_compra, somatoria_carta, cor_escolhida, cor_escolhida_cor)), debug_condicoes)
                                    if cartas.possui_carta_numero(jogador_da_vez, 'Inverte') == True and class_ai.possui_carta_jogavel(baralho, jogador_da_vez, 'Inverte', carta_na_mesa, somatoria_de_compra, somatoria_carta, cor_escolhida, cor_escolhida_cor) == True: # Fifth condition. If Ai has reverse and is playable, then it will play it
                                        debug_printar('Jogar Inverte.', debug)
                                        if debug_ai_joga_cartas == True:
                                            index_carta_selecionada = class_ai.selecionar_carta_random_index(baralho, jogador_da_vez, 'Inverte')
                                            carta_na_mesa = pegar_carta_index(baralho, jogador_da_vez, index_carta_selecionada)
                                            remover_carta(baralho, jogador_da_vez, index_carta_selecionada)
                                            if invertido == True:
                                                invertido = False
                                            else:
                                                invertido = True
                                            if cor_escolhida == True:
                                                cor_escolhida = False
                                            else:
                                                pass
                                            print(f'Jogador #{jogador_da_vez} jogou a carta: {mesa.printar_carta_mesa(carta_na_mesa)}')
                                        jogador_da_vez = mesa.proximo_player(invertido, jogador_da_vez, quantidade_de_jogadores, 1)
                                    else:
                                        file_configs.printar_condicoes('Condição 6. Possui cartas normais ({})'.format(class_ai.possui_cartas_normais(baralho, jogador_da_vez, carta_na_mesa, somatoria_de_compra, somatoria_carta, cor_escolhida, cor_escolhida_cor)), debug_condicoes)
                                        if class_ai.possui_cartas_normais(baralho, jogador_da_vez, carta_na_mesa, somatoria_de_compra, somatoria_carta, cor_escolhida, cor_escolhida_cor) == True: # Sixth condition. If Ai has any normal card and is playable, then it will play it
                                            debug_printar('Jogar Carta Normal.', debug)
                                            if debug_ai_joga_cartas == True:
                                                index_carta_selecionada = class_ai.selecionar_carta_normal_random(baralho, jogador_da_vez, carta_na_mesa, somatoria_carta, somatoria_de_compra, cor_escolhida, cor_escolhida_cor, True)
                                                carta_na_mesa = pegar_carta_index(baralho, jogador_da_vez, index_carta_selecionada)
                                                remover_carta(baralho, jogador_da_vez, index_carta_selecionada)
                                                if cor_escolhida == True:
                                                    cor_escolhida = False
                                                else:
                                                    pass
                                                print(f'Jogador #{jogador_da_vez} jogou a carta: {mesa.printar_carta_mesa(carta_na_mesa)}')
                                            if carta_na_mesa['numero'] == 'Bloqueio':
                                                jogador_da_vez = mesa.proximo_player(invertido, jogador_da_vez, quantidade_de_jogadores, 2)
                                            else:
                                                jogador_da_vez = mesa.proximo_player(invertido, jogador_da_vez, quantidade_de_jogadores, 1)
                                        else:
                                            file_configs.printar_condicoes('Condição 7. Se possuir Mudar Cor ({}) jogar e escolher cor que mais possui ({}).'.format(cartas.possui_carta_numero(jogador_da_vez, 'Mudar Cor'), class_ai.cor_majoritaria(baralho, jogador_da_vez, False)), debug_condicoes)
                                            if cartas.possui_carta_numero(jogador_da_vez, 'Mudar Cor') == True: # Seventh condition. If Ai has Wild and it is playable, then it will play it
                                                debug_printar('Jogar Mudar Cor baseado na cor que o bot mais possui.', debug)
                                                if debug_ai_joga_cartas == True:
                                                    index_carta_selecionada = class_ai.selecionar_carta_random_index(baralho, jogador_da_vez, 'Mudar Cor')
                                                    carta_na_mesa = pegar_carta_index(baralho, jogador_da_vez, index_carta_selecionada)
                                                    remover_carta(baralho, jogador_da_vez, index_carta_selecionada)
                                                    cor_escolhida = True
                                                    cor_escolhida_cor = class_ai.cor_majoritaria(baralho, jogador_da_vez, False)
                                                    print(f'Jogador #{jogador_da_vez} jogou a carta: {mesa.printar_carta_mesa(carta_na_mesa)}')
                                                jogador_da_vez = mesa.proximo_player(invertido, jogador_da_vez, quantidade_de_jogadores, 1)
                                            else:
                                                file_configs.printar_condicoes('Condição 8. Possui +2 ({})'.format(class_ai.possui_carta_jogavel(baralho, jogador_da_vez, '+2', carta_na_mesa, somatoria_de_compra, somatoria_carta, cor_escolhida, cor_escolhida_cor)), debug_condicoes)
                                                if class_ai.possui_carta_jogavel(baralho, jogador_da_vez, '+2', carta_na_mesa, somatoria_de_compra, somatoria_carta, cor_escolhida, cor_escolhida_cor) == True: # Eighth condition. If Ai has Draw 2 and it is playable, then it will play it
                                                    debug_printar('Jogar +2', debug)
                                                    if debug_ai_joga_cartas == True:
                                                        index_carta_selecionada = class_ai.selecionar_carta_random_index(baralho, jogador_da_vez, '+2')
                                                        carta_na_mesa = pegar_carta_index(baralho, jogador_da_vez, index_carta_selecionada)
                                                        remover_carta(baralho, jogador_da_vez, index_carta_selecionada)
                                                        if cor_escolhida == True:
                                                            cor_escolhida = False
                                                        else:
                                                            pass
                                                        somatoria_carta = '+2'
                                                        somatoria_de_compra += 2
                                                        print(f'Jogador #{jogador_da_vez} jogou a carta: {mesa.printar_carta_mesa(carta_na_mesa)}')
                                                    jogador_da_vez = mesa.proximo_player(invertido, jogador_da_vez, quantidade_de_jogadores, 1)
                                                else:
                                                    raise TypeError('Condição não existente. Por favor, contate o desenvolver do jogo')
                else:
                    if somatoria_de_compra == 0: # If the purchase sum is 0, then it will purchase just one card
                        comprar_carta(baralho, jogador_da_vez, 1)
                        print(f'Jogador #{jogador_da_vez} comprou 1 carta.')
                    if somatoria_de_compra > 0: # If the purchase sum is more than 0, then it will purchase the whole purchase sum
                        comprar_carta(baralho, jogador_da_vez, somatoria_de_compra)
                        print(f'Jogador #{jogador_da_vez} comprou {somatoria_de_compra} cartas.')
                        somatoria_de_compra = 0
                    jogador_da_vez = mesa.proximo_player(invertido, jogador_da_vez, quantidade_de_jogadores, 1)


print()
if vencedor == True: # If there's a winner, the game will show this message, otherwise will show nothing
    print(f'O jogador n. {vencedor_num} venceu!')
else:
    pass
print('Programa encerrado.') # This will tell the user the program was finalized
