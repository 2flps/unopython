from time import sleep

def lerlinha(linha, arquivoNome='config.ini', inicioLinhaIndex=0):
    arquivo = open(arquivoNome, 'r')
    comentarios = 15
    count = 0
    while True:
        if count != comentarios + linha:
            arquivo.readline()
            count += 1
        else:
            linha = arquivo.readline()[inicioLinhaIndex:]
            break
    return linha


def escrever():
    try:
        arquivo = open('config.ini', 'x')
        arquivo.write("""#--Game configuration--
#Feel free to change the game configuration
#If for some reason you want to reset the game's configuration, just delete this file then a new one will be generated

#Type and behiavor of each parameter:
#If you don't know what you are doing, just let the default values on
#debug (boolean) -> If it's set true, it will print debug messages for better analysis of the code's structure | Default = False
#qntjogadores (integer) -> Sets the amount of players in the match. Needs to be more than 1 | Default = 4
#cartasiniciais (integer) -> Sets the amount of cards each player will have at the beginning of the game. Needs to be more than 3 | Default = 7
#aihabilitada (boolean) -> If it is set off, the AI will be turned off and the game will simply skip AI turns | Default = True
#uno_intervalo (float) -> If you play a card and left your deck with only one card, you will need to type "Uno" in a 'x' time. 'x' is determined by the value of this parameter. Needs to be more than 0 | Default = 1
#debug_aijogacartas (boolean) -> If it is False, the AI will simply skip their turn. However, if debug is set true, then it will print a message saying which choice was made by the AI | Default = True
#debug_condicoes (boolean) -> If it is set true, for each "card playing condition" the AI will face, a message will be printed saying if the condition 


debug = False
debug_aijogacartas = True
qntjogadores = 4
cartasiniciais = 7
aihabilitada = True
uno_intervalo = 1
debug_condicoes = False""")
    except:
        pass


def debug():
    try:
        linha = lerlinha(linha=0, inicioLinhaIndex=8)
        if 'True' in linha:
            return True
        elif 'False' in linha:
            return False
        else:
            return TypeError("O valor booleano está sendo analisado de forma errada. O valor está digitado corretamente?")
    except:
        raise FileNotFoundError("Arquivo não encontrado/Arquivo com defeito. Você têm certeza que está rodando o programa corretamente?")


def debug_aijogacartas():
    try:
        linha = lerlinha(linha=1, inicioLinhaIndex=21)
        if 'True' in linha:
            return True
        elif 'False' in linha:
            return False
        else:
            return TypeError("O valor booleano está sendo analisado de forma errada. O valor está digitado corretamente?")
    except:
        raise FileNotFoundError("Arquivo não encontrado/Arquivo com defeito. Você têm certeza que está rodando o programa corretamente?")


def qntjogadores():
    try:
        linha = lerlinha(linha=2, inicioLinhaIndex=15)
        return int(linha)
    except:
        raise FileNotFoundError("Arquivo não encontrado/Arquivo com defeito. Você têm certeza que está rodando o programa corretamente?")


def cartasiniciais():
    try:
        linha = lerlinha(linha=3, inicioLinhaIndex=17)
        return int(linha)
    except:
        raise FileNotFoundError("Arquivo não encontrado/Arquivo com defeito. Você têm certeza que está rodando o programa corretamente?")


def ai():
    try:
        linha = lerlinha(linha=4, inicioLinhaIndex=15)
        if 'True' in linha:
            return True
        elif 'False' in linha:
            return False
        else:
            return TypeError("O valor booleano está sendo analisado de forma errada. O valor está digitado corretamente?")
    except:
        raise FileNotFoundError("Arquivo não encontrado/Arquivo com defeito. Você têm certeza que está rodando o programa corretamente?")


def uno_intervalo():
    try:
        linha = lerlinha(linha=5, inicioLinhaIndex=16)
        return float(linha)
    except:
        raise FileNotFoundError("Arquivo não encontrado/Arquivo com defeito. Você têm certeza que está rodando o programa corretamente?")


def debug_printar(msg, debug_mode):
    if debug_mode == True:
        print(msg)
    else:
        pass


def debug_condicoes():
    try:
        linha = lerlinha(linha=6, inicioLinhaIndex=15)
        if 'True' in linha:
            return True
        elif 'False' in linha:
            return False
        else:
            return TypeError("O valor booleano está sendo analisado de forma errada. O valor está digitado corretamente?")
    except:
        raise FileNotFoundError("Arquivo não encontrado/Arquivo com defeito. Você têm certeza que está rodando o programa corretamente?")


def printar_condicoes(msg, debug_condicoes, delay=True, delay_tempo=1.0):
    if debug_condicoes == True:
        if delay == True:
            print(msg)
            sleep(delay_tempo)
        else:
            print(msg)
    else:
        pass


'''
escrever()
print(debug(), 'debug')
print(debug_aijogacartas(), 'debug_aijogacartas')
print(qntjogadores(), 'qntjogadores')
print(ai(), 'ai')
print(cartasiniciais(), 'cartasiniciais')
print(uno_intervalo(), 'uno_intervalo')
print(debug_condicoes(), 'debug_condicoes')
'''