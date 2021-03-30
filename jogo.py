# pylint: disable=unused-import

from uno import *
from time import sleep
import file_configs

# Configs from 'file_configs.py'
file_configs.escrever() # If the file does not exist, it will generate one
debug = file_configs.debug()
jogadoresiniciaisqnt = file_configs.qntjogadores()
cartasiniciaisqnt = file_configs.cartasiniciais()
aihabilitada = file_configs.ai()

baralho = gerarbaralhos(jogadoresiniciaisqnt, cartasiniciaisqnt)
mesa = Mesa(baralho)
cartas = Cartas(baralho)
quantidadejogadores = mesa.quantidadedeplayers()
jogadores = mesa.sequencias(1)
primeirojogador = mesa.playerinicial(quantidadejogadores)
jogadordavez = primeirojogador
invertido = False
cartanamesa = mesa.cartainicial() #{'cor': 'especial', 'numero': '+4'}
somatoriadecompra = 0
somatoriacarta = '0'
corescolhida = False
corescolhida_cor = ''
pene = ''

# Intro
print('---UNO---')
print(f'Há {quantidadejogadores} jogadores na mesa.')
print('')
print('Sorteando as cartas...')
#sleep(1.5)
if jogadores[primeirojogador]['{}'.format(primeirojogador)] == True:
    print('O primeiro jogador é você!')
else:
    print(f'O primeiro jogador é o Jogador {primeirojogador}!')


#Jogo
acao = 1
quebrar = False

while acao > 0 and acao < 4:
    if jogadores[jogadordavez][f'{jogadordavez}'] == True: # Player
        escolhaloop = 0
        printarcartasmesa = mesa.printarcartamesa(cartanamesa)
        print('É a sua vez de jogar. Estas são as suas cartas:')
        vercartas(baralho)
        qntcartasjogadores(baralho, jogadordavez)
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
        acao = mesa.acao(cores)
        if acao == 1:
            print(mesa.cartasjogavel(cartanamesa, jogadordavez, somatoriadecompra, somatoriacarta, corescolhida, corescolhida_cor))
            while mesa.cartasjogavel(cartanamesa, jogadordavez, somatoriadecompra, somatoriacarta, corescolhida, corescolhida_cor) == False:
                escolhaloop = mesa.cartasinvalidas_loop(invertido, jogadordavez, quantidadejogadores, somatoriadecompra, cartanamesa, printarcartasmesa)
            if escolhaloop == 3 or escolhaloop == 4:
                break
            else:
                pass
            cartajogar = mesa.jogarcartamenu(jogadordavez, cores)
            while mesa.cartajogavel(cartanamesa, cartajogar, somatoriadecompra, somatoriacarta, jogadordavez, corescolhida, corescolhida_cor) == False:
                print('Esta carta é inválida')
                cartajogar = mesa.jogarcartamenu(jogadordavez, cores)
            if corescolhida == True:
                corescolhida = False
            if debug == True:
                print('''Carta escolhida things:
Carta jogável: {}
Carta na mesa: {}
Carta jogada: {}
Somatória de compra: {}
Somatória carta: {}
Jogador da vez: {}
Cor escolhida: {}
Cor escolhida_cor: {}'''.format(mesa.cartajogavel(cartanamesa, cartajogar, somatoriadecompra, somatoriacarta, jogadordavez, corescolhida, corescolhida_cor), cartanamesa, cartajogar, somatoriadecompra, somatoriacarta, jogadordavez, corescolhida, corescolhida_cor))
            cartanamesa = pegarcartaindex(baralho, jogadordavez, cartajogar)
            removercarta(baralho, jogadordavez, cartajogar)
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
            if cartanamesa['numero'] == 'Bloqueio':
                jogadordavez = mesa.proximoplayer(invertido, jogadordavez, quantidadejogadores, 2)    
            else:
                jogadordavez = mesa.proximoplayer(invertido, jogadordavez, quantidadejogadores, 1)            
        if acao == 2:
            if somatoriadecompra == 0:
                comprarcarta(baralho, jogadordavez, 1)
                print('Você comprou 1 carta.')
            if somatoriadecompra > 0:
                comprarcarta(baralho, jogadordavez, somatoriadecompra)
                print(f'Você comprou {somatoriadecompra} cartas.')
                somatoriadecompra = 0
            jogadordavez = mesa.proximoplayer(invertido, jogadordavez, quantidadejogadores, 1)
        if acao == 3:
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
    if jogadores[jogadordavez][f'{jogadordavez}'] == False: # AI
        if aihabilitada == False:
            print('AI Desabilitada. Vez do Bot #{}. Pulando vez'.format(jogadordavez))
            jogadordavez = mesa.proximoplayer(invertido, jogadordavez, quantidadejogadores, 1)
        else:
            pass


print('Programa encerrado.')