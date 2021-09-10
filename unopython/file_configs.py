from time import sleep

def ler_linha(linha, arquivo_nome='config.ini', inicio_linha_index=0):
    """
    -> Irá ler uma linha desejada
    :param linha: (int) linha na qual o usuário deseja ler
    :param arquivo_nome: (str) nome do arquivo na qual o usuário deseja ler
    :param inicio_linha_index: (int) índice na qual o usuário deseja que a leitura comece
    :return: irá retornar uma string com a linha lida pela função
    """
    arquivo = open(arquivo_nome, 'r')
    comentarios = 15
    count = 0
    while True:
        if count != comentarios + linha:
            arquivo.readline()
            count += 1
        else:
            linha = arquivo.readline()[inicio_linha_index:]
            break
    return linha


def escrever():
    """
    -> Irá gerar um arquivo .ini de configurações na pasta raíz do jogo. Caso o arquivo já exista, nada acontecerá
    :return: sem retorno
    """
    try:
        arquivo = open('config.ini', 'x')
        arquivo.write("""#--Game configuration--
#Feel free to change the game configuration
#If for some reason you want to reset the game's configuration, just delete this file then a new one will be generated

#Type and behiavor of each parameter:
#If you don't know what you are doing, just let the default values on
#debug (boolean) -> If it's set true, it will print debug messages for better analysis of the code's structure | Default = False
#qnt_jogadores (integer) -> Sets the amount of players in the match. Needs to be more than 1 | Default = 4
#cartas_iniciais (integer) -> Sets the amount of cards each player will have at the beginning of the game. Needs to be more than 3 | Default = 7
#ai_habilitada (boolean) -> If it is set off, the Ai will be turned off and the game will simply skip Ai turns | Default = True
#uno_intervalo (float) -> If you play a card and left your deck with only one card, you will need to type "Uno" in a 'x' time. 'x' is determined by the value of this parameter. Needs to be more than 0 | Default = 1
#debug_ai_joga_cartas (boolean) -> If it is False, the Ai will simply skip their turn. However, if debug is set true, then it will print a message saying which choice was made by the Ai | Default = True
#debug_condicoes (boolean) -> If it is set true, for each "card playing condition" the Ai face, a message will be printed saying if the condition 


debug = False
debug_ai_joga_cartas = True
qnt_jogadores = 4
cartas_iniciais = 7
ai_habilitada = True
uno_intervalo = 1.5
debug_condicoes = False""")
    except:
        pass


def debug():
    """
    -> Irá ler o arquivo de configurações e analisar o parâmetro de "debug"
    :return: retornará um booleano dizendo se o parâmetro é True ou False
    """
    try:
        linha = ler_linha(linha=0, inicio_linha_index=8)
        if 'True' in linha:
            return True
        elif 'False' in linha:
            return False
        else:
            return TypeError("O valor booleano está sendo analisado de forma errada. O valor está digitado corretamente?")
    except:
        raise FileNotFoundError("Arquivo não encontrado/Arquivo com defeito. Você têm certeza que está rodando o programa corretamente?")


def debug_ai_joga_cartas():
    """
    -> Irá ler o arquivo de configurações e analisar o parâmetro de "debug_ai_joga_cartas"
    :return: retornará um booleano dizendo se o parâmetro é True ou False
    """
    try:
        linha = ler_linha(linha=1, inicio_linha_index=21)
        if 'True' in linha:
            return True
        elif 'False' in linha:
            return False
        else:
            return TypeError("O valor booleano está sendo analisado de forma errada. O valor está digitado corretamente?")
    except:
        raise FileNotFoundError("Arquivo não encontrado/Arquivo com defeito. Você têm certeza que está rodando o programa corretamente?")


def qnt_jogadores():
    """
    -> Irá ler o arquivo de configurações e analisar o parâmetro "qnt_jogadores"
    :return: retornará o valor do parâmetro
    """
    try:
        linha = ler_linha(linha=2, inicio_linha_index=15)
        return int(linha)
    except:
        raise FileNotFoundError("Arquivo não encontrado/Arquivo com defeito. Você têm certeza que está rodando o programa corretamente?")


def cartas_iniciais():
    """
    -> Irá ler o arquivo de configurações e analisar o parâmetro "cartas_iniciais"
    :return: retornará o valor do parâmetro
    """
    try:
        linha = ler_linha(linha=3, inicio_linha_index=17)
        return int(linha)
    except:
        raise FileNotFoundError("Arquivo não encontrado/Arquivo com defeito. Você têm certeza que está rodando o programa corretamente?")


def ai():
    """
    -> Irá ler o arquivo de configurações e analisar o parâmetro "Ai"
    :return: retornará o valor do parâmetro
    """
    try:
        linha = ler_linha(linha=4, inicio_linha_index=15)
        if 'True' in linha:
            return True
        elif 'False' in linha:
            return False
        else:
            return TypeError("O valor booleano está sendo analisado de forma errada. O valor está digitado corretamente?")
    except:
        raise FileNotFoundError("Arquivo não encontrado/Arquivo com defeito. Você têm certeza que está rodando o programa corretamente?")


def uno_intervalo():
    """
    -> Irá ler o arquivo de configurações e analisar o parâmetro "uno_intervalo"
    :return: retornará o valor do parâmetro
    """
    try:
        linha = ler_linha(linha=5, inicio_linha_index=16)
        return float(linha)
    except:
        raise FileNotFoundError("Arquivo não encontrado/Arquivo com defeito. Você têm certeza que está rodando o programa corretamente?")


def debug_printar(msg, debug_mode):
    """
    -> Irá ler o arquivo de configurações e analisar o parâmetro "debug_printar"
    :return: retornará o valor do parâmetro
    """
    if debug_mode == True:
        print(msg)
    else:
        pass


def debug_condicoes():
    """
    -> Irá ler o arquivo de configurações e analisar o parâmetro "debug_condicoes"
    :return: retornará o valor do parâmetro
    """
    try:
        linha = ler_linha(linha=6, inicio_linha_index=15)
        if 'True' in linha:
            return True
        elif 'False' in linha:
            return False
        else:
            return TypeError("O valor booleano está sendo analisado de forma errada. O valor está digitado corretamente?")
    except:
        raise FileNotFoundError("Arquivo não encontrado/Arquivo com defeito. Você têm certeza que está rodando o programa corretamente?")


def printar_condicoes(msg, debug_condicoes, delay=True, delay_tempo=1.0):
    """
    -> Irá ler o arquivo de configurações e analisar o parâmetro "printar_condicoes"
    :return: retornará o valor do parâmetro
    """
    if debug_condicoes == True:
        if delay == True:
            print(msg)
            sleep(delay_tempo)
        else:
            print(msg)
    else:
        pass
