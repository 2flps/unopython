# pylint: disable=unused-import

from uno import *
from time import sleep
import file_configs

# Configs from 'file_configs.py'
file_configs.escrever() # If the file does not exist, it will generate one
debug = file_configs.debug() # Will decides if debug mode is on/off
debug_aijogacartas = file_configs.debug_aijogacartas() # If it is set false, then the bots will simply skip their turns based on the choice making of card playing
jogadoresiniciaisqnt = file_configs.qntjogadores() # Will set the amount of players in the match
cartasiniciaisqnt = file_configs.cartasiniciais() # Will set the amount of cards each player will receive in the beginning
aihabilitada = file_configs.ai() # If the AI is off, it will simply skip it's turn
uno_intervalo = file_configs.uno_intervalo() # This will set the interval the player will have to type "Uno" in the prompt
debug_condicoes = file_configs.debug_condicoes() # If it is set true, then for each "card playing condition" the AI face, a message will be printed

baralho = gerarbaralhos(jogadoresiniciaisqnt, cartasiniciaisqnt) # This variable will store the deck of all players inside a dictionare
mesa = Mesa(baralho) # Calls the class 'mesa'
cartas = Cartas(baralho) # Calls the class 'cartas'
quantidadejogadores = mesa.quantidadedeplayers() # This variable will store the amount of players in the match
jogadores = mesa.sequencias(1) # This will set the order of playing
primeirojogador = mesa.playerinicial(quantidadejogadores) # Calls the function 'playerinicial' to generate the first player for the first turn
jogadordavez = primeirojogador # This variable stores the number (integer) of the current turn player. When the game starts, the current player will always be the result of 'playerinicial' function
invertido = False # This variable stores a boolean which will tell if the game is clockwise or anticlockwise
cartanamesa = mesa.cartainicial() # This variable stores a dictionare containing the current turn card. This is an example of a card -> {'cor': 'especial', 'numero': '+4'} 
somatoriadecompra = 0 # If there is an ongoing "buy-type" card (+4 or +2), then this variable will store the purchase sum that the unlucky one will have to buy
somatoriacarta = '0' # This variable will store the "buy-type" card (+4 or +2). This '0' data is just a placeholder :)
corescolhida = False # If some player choosed a color with a "change-color-type" card ('Change color' or +4) then the variable will set "True" until someone buy a card
corescolhida_cor = '' # This variable stores the choosed color for the variable above
vencedor = False # If there's a winner, this variable will set True
vencedorn = 0 # This variable stores the index of the winner
class_debug = Debug(baralho, cores) # Calls the class 'debug'
class_ai = AI(baralho, cores) # Calls the class 'AI'

# Intro <- This section will only prints the introduction. Nothing else
print('---UNO---')
print(f'Há {quantidadejogadores} jogadores na mesa.')
print('')
print('Sorteando as cartas...')
if jogadores[primeirojogador]['{}'.format(primeirojogador)] == True:
    print('O primeiro jogador é você!\n')
else:
    print(f'O primeiro jogador é o Jogador {primeirojogador}!\n')


# This variable below stores the choice the player will take during the game
acao = 1

while acao > 0 and acao < 4: # As long as the player choice stood more than 0 and less than 4, the game/console will not shutdown itself
    if debug == True: # If debug is set True, then it will print each player deck each turn
        for c in range(0, 4):
            print(baralho[c])
    if checar_ganhador(baralho, quantidadejogadores) == True: # This will check if there is a winner in the current game
        vencedor = True
        vencedorn = ganhador(baralho, quantidadejogadores)
    if vencedor == True: # If there is a winner, then this loop will break and a winner message will be displayed
        break
    else: # If there is no winner, then the game will simply run
        if jogadores[jogadordavez][f'{jogadordavez}'] == True: # This section covers the player controlled part
            escolhaloop = 0 # This variable stores an integer. It's usage is explained below
            lock_jogar = False # If there is none available card to be played, this variable will be set True
            printarcartasmesa = mesa.printarcartamesa(cartanamesa) # Calls the 'printarcartamesa' function, which prints the current player cards in a colorful way (it's not good for me, due to my colorblindness)
            print('===============================================\nÉ a sua vez de jogar. Estas são as suas cartas:')
            vercartas(baralho) # Calls the 'vercartas' function, which prints the amount of cards of each player
            qntcartasjogadores(baralho, jogadordavez) # It seeems that this function has the pretty same workability that the 'printarcartamesa' has. Idk why :|
            print() # This just simply prints a blank message, because I'm too lazy to use \n
            print('A carta na mesa é: {}'.format(mesa.printarcartamesa(cartanamesa)), end = ' | ') # This prints the card on the desk in a colorful way
            if somatoriadecompra > 0: # This section covers the Purchase Sum that will be printed.
                if somatoriacarta == '+4':
                    print('Há {} carta(s) de +4, totalizando uma somatória de compra de {} cartas.'.format(somatoriadecompra // 4, somatoriadecompra)) # If the purchase sum card is +4, it will print a +4 message
                else:
                    print('Há {} carta(s) de +2, totalizando uma somatória de compra de {} cartas.'.format(somatoriadecompra // 2, somatoriadecompra)) # If the purchase sum card is +2, it will print a +2 message
            else:
                pass
            if corescolhida == False:
                print()
            else:
                print('Cor escolhida: {}'.format(mesa.printarnomedacor(corescolhida_cor, cores))) # If there's a chosen color, then this will print the chosen one
            print()
            acao = mesa.acao(cores) # This function will print the user menu.
            if acao == 1: # If the user action is 1, then will execute this block
                while mesa.cartasjogavel(cartanamesa, jogadordavez, somatoriadecompra, somatoriacarta, corescolhida, corescolhida_cor, debug) == False: # If there's no available card to play, then it will starts a loop
                    escolhaloop = mesa.cartasinvalidas_loop(cores)
                    if escolhaloop == 2:
                        if somatoriadecompra == 0: # If the purchase sum is 0, then it will purchase just one card
                            comprarcarta(baralho, jogadordavez, 1)
                            print('Você comprou 1 carta.')
                        if somatoriadecompra > 0: # If the purchase sum is more than 0, then it will purchase the whole purchase sum
                            comprarcarta(baralho, jogadordavez, somatoriadecompra)
                            print(f'Você comprou {somatoriadecompra} cartas.')
                            somatoriadecompra = 0
                        jogadordavez = mesa.proximoplayer(invertido, jogadordavez, quantidadejogadores, 1)
                        lock_jogar = True
                        break
                    if escolhaloop == 3:
                        if acao == 3: # If the chosen action is 3, then it prints the amount of cards each player have
                            print('--Ver Cartas--')
                            print()
                            print('A carta na mesa é: {}'.format(mesa.printarcartamesa(cartanamesa)), end = ' | ')
                            if somatoriadecompra > 0:
                                if somatoriacarta == '+4':
                                    print('Há {} carta(s) de +4, totalizando uma somatória de compra de {} cartas.'.format(somatoriadecompra // 4, somatoriadecompra))
                                else:
                                    print('Há {} carta(s) de +2, totalizando uma somatória de compra de {} cartas.'.format(somatoriadecompra // 2, somatoriadecompra))
                            else:
                                pass
                            if corescolhida == False:
                                print()
                            else:
                                print('Cor escolhida: {}'.format(mesa.printarnomedacor(corescolhida_cor, cores)))
                            print()
                            break
                    if escolhaloop == 4:
                        break
                if escolhaloop == 3 or escolhaloop == 4: # This will break the loop if the user choose option 3 or 4. Otherwise the loop will just continues
                    break
                elif escolhaloop == 2:
                    jogadordavez = mesa.proximoplayer(invertido, jogadordavez, quantidadejogadores, 1)
                else:
                    pass
                if lock_jogar == False: # If there's an available card to be played then this block will be executed, otherwise it will just ignore
                    cartajogar = mesa.jogarcartamenu(jogadordavez, cores, lock_jogar) # This functions call the "Play card" menu, where the user will choose a card based on it's index to play
                    while mesa.cartajogavel(cartanamesa, cartajogar, somatoriadecompra, somatoriacarta, jogadordavez, corescolhida, corescolhida_cor, debug) == False: # If the chosen card is not playable, then it will starts this loop
                        print('Esta carta é inválida')
                        cartajogar = mesa.jogarcartamenu(jogadordavez, cores, lock_jogar)
                    if corescolhida == True: # If there's a chosen color and a player plays a card, then the "chosen color" variable will set False
                        corescolhida = False
                    if debug == True: # Debug things
                        print('''Carta escolhida things:\nCarta jogável: {}\nCarta na mesa: {}\nCarta jogada: {}\nSomatória de compra: {}\nSomatória carta: {}\nJogador da vez: {}\nCor escolhida: {}\nCor escolhida_cor: {}'''.format(mesa.cartajogavel(cartanamesa, cartajogar, somatoriadecompra, somatoriacarta, jogadordavez, corescolhida, corescolhida_cor), cartanamesa, cartajogar, somatoriadecompra, somatoriacarta, jogadordavez, corescolhida, corescolhida_cor))
                    cartanamesa = pegarcartaindex(baralho, jogadordavez, cartajogar) # This will set the current turn card to be the one the player selected using the 'pegarcartaindex' function
                    removercarta(baralho, jogadordavez, cartajogar) # This will remove the card the player selected
                    #This section below will cover the Chosen color part and the Purchase sum part
                    if cartanamesa['numero'] == 'Mudar Cor' or cartanamesa['numero'] == '+4':
                        corescolhida = True
                        corescolhida_cor = cartas.efeito_mudarcor(cores)
                    if cartanamesa['numero'] == '+4':
                        somatoriadecompra += 4
                        somatoriacarta = '+4'
                    if cartanamesa['numero'] == '+2':
                        somatoriadecompra += 2
                        somatoriacarta = '+2'
                    if cartanamesa['numero'] == 'Inverte':
                        if invertido == False:
                            invertido = mesa.inverter()
                        else:
                            invertido = mesa.desinverter()
                    if len(baralho[jogadordavez]) == 1: # This will run the "Uno" part, when there's only one card left in the deck
                        menu_uno = mesa.unomenu(uno_intervalo, cores)
                        if menu_uno == False:
                            pass
                        else:
                            comprarcarta(baralho, jogadordavez, 2)
                            print('{}Você comprou 2 cartas pois digitou "Uno" errado ou simplesmente não digitou.')
                    if len(baralho[jogadordavez]) == 0:
                        vencedor = True
                        vencedorn = jogadordavez
                    else:
                        pass
                    if cartanamesa['numero'] == 'Bloqueio':
                        jogadordavez = mesa.proximoplayer(invertido, jogadordavez, quantidadejogadores, 2) # If some player use the Block card, then it will skip 2 person. Otherwise it will just skip 1.
                    else:
                        jogadordavez = mesa.proximoplayer(invertido, jogadordavez, quantidadejogadores, 1)
            if acao == 2: # If the chosen action is 2, then the player will purchase one or more cards
                if somatoriadecompra == 0: # If the purchase sum is 0, then it will purchase just one card
                    comprarcarta(baralho, jogadordavez, 1)
                    print('Você comprou 1 carta.')
                if somatoriadecompra > 0: # If the purchase sum is more than 0, then it will purchase the whole purchase sum
                    comprarcarta(baralho, jogadordavez, somatoriadecompra)
                    print(f'Você comprou {somatoriadecompra} cartas.')
                    somatoriadecompra = 0
                jogadordavez = mesa.proximoplayer(invertido, jogadordavez, quantidadejogadores, 1)
            if acao == 3: # If the chosen action is 3, then it prints the amount of cards each player have
                print('--Ver Cartas--')
                print()
                print('A carta na mesa é: {}'.format(mesa.printarcartamesa(cartanamesa)), end = ' | ')
                if somatoriadecompra > 0:
                    if somatoriacarta == '+4':
                        print('Há {} carta(s) de +4, totalizando uma somatória de compra de {} cartas.'.format(somatoriadecompra // 4, somatoriadecompra))
                    else:
                        print('Há {} carta(s) de +2, totalizando uma somatória de compra de {} cartas.'.format(somatoriadecompra // 2, somatoriadecompra))
                else:
                    pass
                if corescolhida == False:
                    print()
                else:
                    print('Cor escolhida: {}'.format(mesa.printarnomedacor(corescolhida_cor, cores)))
                print()
        if jogadores[jogadordavez][f'{jogadordavez}'] == False: # This section coverts the AI controlled part
            if aihabilitada == False: # If the AI is turned off, then it simply skips the AI turn
                print('AI Desabilitada. Vez do Bot #{}. Pulando vez'.format(jogadordavez))
                jogadordavez = mesa.proximoplayer(invertido, jogadordavez, quantidadejogadores, 1)            
            else: # This section covers the "AI card playing decision" part
                file_configs.printar_condicoes('Condição 1. Somatória de Compra == 0 ({}) e Única carta jogável == +4 {}'.format(somatoriadecompra, class_ai.unica_carta_jogavel(baralho, jogadordavez, '+4', cartanamesa, somatoriadecompra, somatoriacarta, corescolhida, corescolhida_cor)), debug_condicoes)
                if mesa.cartasjogavel(cartanamesa, jogadordavez, somatoriadecompra, somatoriacarta, corescolhida, corescolhida_cor, False) == True: # First condition. If the purchase amount is equal to 0 and the only playable card is +4, then the AI will simply buy one card
                    if somatoriadecompra == 0 and class_ai.unica_carta_jogavel(baralho, jogadordavez, '+4', cartanamesa, somatoriadecompra, somatoriacarta, corescolhida, corescolhida_cor) == True:
                        if debug_aijogacartas == True:
                            comprarcarta(baralho, jogadordavez, 1)
                            print(f'Jogador #{jogadordavez} comprou uma carta.')
                        debug_printar('Somatória de compra == 0 e única carta jogável é +4. Ação = Comprar uma carta', debug)
                        jogadordavez = mesa.proximoplayer(invertido, jogadordavez, quantidadejogadores, 1)
                    else:
                        file_configs.printar_condicoes('Condição 2. Somatória de Compra > 0 ({}) e possui carta == carta somatória {}'.format(somatoriadecompra, cartas.possuicartanumero(jogadordavez, somatoriacarta)), debug_condicoes)
                        if somatoriadecompra > 0 and cartas.possuicartanumero(jogadordavez, somatoriacarta) == True: # Second condition. If the purchase amount is > 0 and AI has an playable card, then it will play
                            debug_printar('Somatória de compra > 0 e Jogador possuí carta == Somatória carta', debug)
                            if debug_aijogacartas == True:
                                indexcartadasomatoria = class_ai.selecionar_carta_random_index(baralho, jogadordavez, somatoriacarta)
                                if baralho[jogadordavez][indexcartadasomatoria]['numero'] == '+4':
                                    somatoriadecompra += 4
                                    somatoriacarta = '+4'
                                    corescolhida = True
                                    corescolhida_cor = class_ai.cor_majoritaria(baralho, jogadordavez, False)
                                elif baralho[jogadordavez][indexcartadasomatoria]['numero'] == '+2':
                                    somatoriadecompra += 2
                                    somatoriacarta = '+2'
                                    if corescolhida == True:
                                        corescolhida = False
                                    else:
                                        pass
                                else:
                                    raise ValueError('O número do índice da carta escolhida difere de +2 e +4. O código está certo?')
                                cartanamesa = pegarcartaindex(baralho, jogadordavez, indexcartadasomatoria)
                                removercarta(baralho, jogadordavez, indexcartadasomatoria)
                                print(f'Jogador #{jogadordavez} jogou a carta: {mesa.printarcartamesa(cartanamesa)}')
                            jogadordavez = mesa.proximoplayer(invertido, jogadordavez, quantidadejogadores, 1)
                        else:
                            file_configs.printar_condicoes('Condição 3. Tamanho do baralho do próximo player < 3 ({}).'.format(class_ai.tamanho_baralho(baralho, mesa.proximoplayer(invertido, jogadordavez, quantidadejogadores, 1), False)), debug_condicoes)
                            if class_ai.tamanho_baralho(baralho, mesa.proximoplayer(invertido, jogadordavez, quantidadejogadores, 1), False) < 3: # Third condition. If the next player has less than 3 cards on its deck, then it will choose one subcondition.
                                if cartas.possuicartanumero(jogadordavez, '+4') == True and class_ai.possuicartajogavel(baralho, jogadordavez, '+4', cartanamesa, somatoriadecompra, somatoriacarta, corescolhida, corescolhida_cor) == True: # First subcondition. If AI has +4 and is playable, then it will play it
                                    debug_printar('Tamanho do baralho do próximo player < 3 cartas. Bot possui carta +4.', debug)
                                    if debug_aijogacartas == True:
                                        indexcartaselecionada = class_ai.selecionar_carta_random_index(baralho, jogadordavez, '+4')
                                        cartanamesa = pegarcartaindex(baralho, jogadordavez, indexcartaselecionada)
                                        removercarta(baralho, jogadordavez, indexcartaselecionada)
                                        somatoriadecompra += 4
                                        somatoriacarta = '+4'
                                        corescolhida = True
                                        corescolhida_cor = class_ai.cor_majoritaria(baralho, jogadordavez, False)
                                        print(f'Jogador #{jogadordavez} jogou a carta: {mesa.printarcartamesa(cartanamesa)}')
                                    jogadordavez = mesa.proximoplayer(invertido, jogadordavez, quantidadejogadores, 1)
                                elif cartas.possuicartanumero(jogadordavez, '+2') == True and class_ai.possuicartajogavel(baralho, jogadordavez, '+2', cartanamesa, somatoriadecompra, somatoriacarta, corescolhida, corescolhida_cor) == True: # Second subcondition. If AI has +2 and is playable, then it will play it
                                    debug_printar('Tamanho do baralho do próximo player < 3 cartas. Bot possui carta +2.', debug)
                                    if debug_aijogacartas == True:
                                        indexcartaselecionada = class_ai.selecionar_carta_random_index(baralho, jogadordavez, '+2')
                                        cartanamesa = pegarcartaindex(baralho, jogadordavez, indexcartaselecionada)
                                        removercarta(baralho, jogadordavez, indexcartaselecionada)
                                        somatoriadecompra += 2
                                        somatoriacarta = '+2'
                                        if corescolhida == True:
                                            corescolhida = False
                                        else:
                                            pass
                                        print(f'Jogador #{jogadordavez} jogou a carta: {mesa.printarcartamesa(cartanamesa)}')
                                    jogadordavez = mesa.proximoplayer(invertido, jogadordavez, quantidadejogadores, 1)
                                elif cartas.possuicartanumero(jogadordavez, 'Bloqueio') == True and class_ai.possuicartajogavel(baralho, jogadordavez, 'Bloqueio', cartanamesa, somatoriadecompra, somatoriacarta, corescolhida, corescolhida_cor) == True: # Third subcondition. If AI has skip and is playable, then it will play it
                                    debug_printar('Tamanho do baralho do próximo player < 3 cartas. Bot possui carta Bloqueio.', debug)
                                    if debug_aijogacartas == True:
                                        indexcartaselecionada = class_ai.selecionar_carta_random_index(baralho, jogadordavez, 'Bloqueio')
                                        cartanamesa = pegarcartaindex(baralho, jogadordavez, indexcartaselecionada)
                                        removercarta(baralho, jogadordavez, indexcartaselecionada)
                                        if corescolhida == True:
                                            corescolhida = False
                                        else:
                                            pass
                                        print(f'Jogador #{jogadordavez} jogou a carta: {mesa.printarcartamesa(cartanamesa)}')
                                    jogadordavez = mesa.proximoplayer(invertido, jogadordavez, quantidadejogadores, 2)
                                elif cartas.possuicartanumero(jogadordavez, 'Inverte') == True and class_ai.possuicartajogavel(baralho, jogadordavez, 'Inverte', cartanamesa, somatoriadecompra, somatoriacarta, corescolhida, corescolhida_cor) == True: # Fourth subcondition. If AI has reverse and is playable, then it will play it
                                    debug_printar('Tamanho do baralho do próximo player < 3 cartas. Bot possui carta Inverte.', debug)
                                    if debug_aijogacartas == True:
                                        indexcartaselecionada = class_ai.selecionar_carta_random_index(baralho, jogadordavez, 'Inverte')
                                        cartanamesa = pegarcartaindex(baralho, jogadordavez, indexcartaselecionada)
                                        removercarta(baralho, jogadordavez, indexcartaselecionada)
                                        if invertido == False:
                                            invertido = True
                                        else:
                                            invertido = False
                                        if corescolhida == True:
                                            corescolhida = False
                                        else:
                                            pass
                                        print(f'Jogador #{jogadordavez} jogou a carta: {mesa.printarcartamesa(cartanamesa)}')
                                    jogadordavez = mesa.proximoplayer(invertido, jogadordavez, quantidadejogadores, 1)
                                else: # Fifth condition. If AI has any normal card, then it will play it
                                    debug_printar('Tamanho do baralho do próximo player < 3 cartas. Jogando qualquer carta normal aleatória.', debug)
                                    if debug_aijogacartas == True:
                                        indexcartaselecionada = class_ai.selecionar_carta_normal_random(baralho, jogadordavez, cartanamesa, somatoriacarta, somatoriadecompra, corescolhida, corescolhida_cor)
                                        cartanamesa = pegarcartaindex(baralho, jogadordavez, indexcartaselecionada)
                                        removercarta(baralho, jogadordavez, indexcartaselecionada)
                                        if corescolhida == True:
                                            corescolhida = False
                                        else:
                                            pass
                                        print(f'Jogador #{jogadordavez} jogou a carta: {mesa.printarcartamesa(cartanamesa)}')
                                    jogadordavez = mesa.proximoplayer(invertido, jogadordavez, quantidadejogadores, 1)
                            else:
                                file_configs.printar_condicoes('Condição 4. Possui Bloqueio ({}) e é jogável ({})'.format(cartas.possuicartanumero(jogadordavez, 'Bloqueio'), class_ai.possuicartajogavel(baralho, jogadordavez, 'Bloqueio', cartanamesa, somatoriadecompra, somatoriacarta, corescolhida, corescolhida_cor)), debug_condicoes)
                                if cartas.possuicartanumero(jogadordavez, 'Bloqueio') == True and class_ai.possuicartajogavel(baralho, jogadordavez, 'Bloqueio', cartanamesa, somatoriadecompra, somatoriacarta, corescolhida, corescolhida_cor) == True: # Fourth condition. If AI has skip and is playable, then it will play it
                                    debug_printar('Jogar Bloqueio.', debug)
                                    if debug_aijogacartas == True:
                                        indexcartaselecionada = class_ai.selecionar_carta_random_index(baralho, jogadordavez, 'Bloqueio')
                                        cartanamesa = pegarcartaindex(baralho, jogadordavez, indexcartaselecionada)
                                        removercarta(baralho, jogadordavez, indexcartaselecionada)
                                        if corescolhida == True:
                                            corescolhida = False
                                        else:
                                            pass
                                        print(f'Jogador #{jogadordavez} jogou a carta: {mesa.printarcartamesa(cartanamesa)}')
                                    jogadordavez = mesa.proximoplayer(invertido, jogadordavez, quantidadejogadores, 2)
                                else:
                                    file_configs.printar_condicoes('Condição 5. Possui Inverte ({}) e é jogável ({})'.format(cartas.possuicartanumero(jogadordavez, 'Inverte'), class_ai.possuicartajogavel(baralho, jogadordavez, 'Inverte', cartanamesa, somatoriadecompra, somatoriacarta, corescolhida, corescolhida_cor)), debug_condicoes)
                                    if cartas.possuicartanumero(jogadordavez, 'Inverte') == True and class_ai.possuicartajogavel(baralho, jogadordavez, 'Inverte', cartanamesa, somatoriadecompra, somatoriacarta, corescolhida, corescolhida_cor) == True: # Fifth condition. If AI has reverse and is playable, then it will play it
                                        debug_printar('Jogar Inverte.', debug)
                                        if debug_aijogacartas == True:
                                            indexcartaselecionada = class_ai.selecionar_carta_random_index(baralho, jogadordavez, 'Inverte')
                                            cartanamesa = pegarcartaindex(baralho, jogadordavez, indexcartaselecionada)
                                            removercarta(baralho, jogadordavez, indexcartaselecionada)
                                            if invertido == True:
                                                invertido = False
                                            else:
                                                invertido = True
                                            if corescolhida == True:
                                                corescolhida = False
                                            else:
                                                pass
                                            print(f'Jogador #{jogadordavez} jogou a carta: {mesa.printarcartamesa(cartanamesa)}')
                                        jogadordavez = mesa.proximoplayer(invertido, jogadordavez, quantidadejogadores, 1)
                                    else:
                                        file_configs.printar_condicoes('Condição 6. Possui cartas normais ({})'.format(class_ai.possui_cartas_normais(baralho, jogadordavez, cartanamesa, somatoriadecompra, somatoriacarta, corescolhida, corescolhida_cor)), debug_condicoes)
                                        if class_ai.possui_cartas_normais(baralho, jogadordavez, cartanamesa, somatoriadecompra, somatoriacarta, corescolhida, corescolhida_cor) == True: # Sixth condition. If AI has any normal card and is playable, then it will play it
                                            debug_printar('Jogar Carta Normal.', debug)
                                            if debug_aijogacartas == True:
                                                indexcartaselecionada = class_ai.selecionar_carta_normal_random(baralho, jogadordavez, cartanamesa, somatoriacarta, somatoriadecompra, corescolhida, corescolhida_cor, True)
                                                cartanamesa = pegarcartaindex(baralho, jogadordavez, indexcartaselecionada)
                                                removercarta(baralho, jogadordavez, indexcartaselecionada)
                                                if corescolhida == True:
                                                    corescolhida = False
                                                else:
                                                    pass
                                                print(f'Jogador #{jogadordavez} jogou a carta: {mesa.printarcartamesa(cartanamesa)}')
                                            if cartanamesa['numero'] == 'Bloqueio':
                                                jogadordavez = mesa.proximoplayer(invertido, jogadordavez, quantidadejogadores, 2)
                                            else:
                                                jogadordavez = mesa.proximoplayer(invertido, jogadordavez, quantidadejogadores, 1)
                                        else:
                                            file_configs.printar_condicoes('Condição 7. Se possuir Mudar Cor ({}) jogar e escolher cor que mais possui ({}).'.format(cartas.possuicartanumero(jogadordavez, 'Mudar Cor'), class_ai.cor_majoritaria(baralho, jogadordavez, False)), debug_condicoes)
                                            if cartas.possuicartanumero(jogadordavez, 'Mudar Cor') == True: # Seventh condition. If AI has Wild and it is playable, then it will play it
                                                debug_printar('Jogar Mudar Cor baseado na cor que o bot mais possui.', debug)
                                                if debug_aijogacartas == True:
                                                    indexcartaselecionada = class_ai.selecionar_carta_random_index(baralho, jogadordavez, 'Mudar Cor')
                                                    cartanamesa = pegarcartaindex(baralho, jogadordavez, indexcartaselecionada)
                                                    removercarta(baralho, jogadordavez, indexcartaselecionada)
                                                    corescolhida = True
                                                    corescolhida_cor = class_ai.cor_majoritaria(baralho, jogadordavez, False)
                                                    print(f'Jogador #{jogadordavez} jogou a carta: {mesa.printarcartamesa(cartanamesa)}')
                                                jogadordavez = mesa.proximoplayer(invertido, jogadordavez, quantidadejogadores, 1)
                                            else:
                                                file_configs.printar_condicoes('Condição 8. Possui +2 ({})'.format(class_ai.possuicartajogavel(baralho, jogadordavez, '+2', cartanamesa, somatoriadecompra, somatoriacarta, corescolhida, corescolhida_cor)), debug_condicoes)
                                                if class_ai.possuicartajogavel(baralho, jogadordavez, '+2', cartanamesa, somatoriadecompra, somatoriacarta, corescolhida, corescolhida_cor) == True: # Eighth condition. If AI has Draw 2 and it is playable, then it will play it
                                                    debug_printar('Jogar +2', debug)
                                                    if debug_aijogacartas == True:
                                                        indexcartaselecionada = class_ai.selecionar_carta_random_index(baralho, jogadordavez, '+2')
                                                        cartanamesa = pegarcartaindex(baralho, jogadordavez, indexcartaselecionada)
                                                        removercarta(baralho, jogadordavez, indexcartaselecionada)
                                                        if corescolhida == True:
                                                            corescolhida = False
                                                        else:
                                                            pass
                                                        somatoriacarta = '+2'
                                                        somatoriadecompra += 2
                                                        print(f'Jogador #{jogadordavez} jogou a carta: {mesa.printarcartamesa(cartanamesa)}')
                                                    jogadordavez = mesa.proximoplayer(invertido, jogadordavez, quantidadejogadores, 1)
                                                else:
                                                    raise TypeError('Condição não existente. Por favor, contate o desenvolver do jogo')
                else:
                    if somatoriadecompra == 0: # If the purchase sum is 0, then it will purchase just one card
                        comprarcarta(baralho, jogadordavez, 1)
                        print(f'Jogador #{jogadordavez} comprou 1 carta.')
                    if somatoriadecompra > 0: # If the purchase sum is more than 0, then it will purchase the whole purchase sum
                        comprarcarta(baralho, jogadordavez, somatoriadecompra)
                        print(f'Jogador #{jogadordavez} comprou {somatoriadecompra} cartas.')
                        somatoriadecompra = 0
                    jogadordavez = mesa.proximoplayer(invertido, jogadordavez, quantidadejogadores, 1)


print()
if vencedor == True: # If there's a winner, the game will show this message, otherwise will show nothing
    print(f'O jogador n. {vencedorn} venceu!')
else:
    pass
print('Programa encerrado.') # This will tell the user the program was finalized