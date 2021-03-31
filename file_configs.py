def lerlinha(linha, arquivoNome='config.cfg', inicioLinhaIndex=0):
    arquivo = open(arquivoNome, 'r')
    count = 0
    while True:
        if count != linha:
            arquivo.readline()
            count += 1
        else:
            linha = arquivo.readline()[inicioLinhaIndex:]
            break
    return linha


def escrever():
    try:
        arquivo = open('config.cfg', 'x')
        arquivo.write("""debug = False
qntjogadores = 4
cartasiniciais = 7
aihabilitada = True""")
    except:
        pass


def debug():
    try:
        arquivo = open('config.cfg', 'r')
        debugstr = arquivo.readline()[8:]
        if 'True' in debugstr:
            return True
        elif 'False' in debugstr:
            return False
    except:
        raise FileNotFoundError("Arquivo não encontrado/Arquivo com defeito. Você têm certeza que está rodando o programa corretamente?")


def qntjogadores():
    try:
        linha = lerlinha(linha=1, inicioLinhaIndex=15)
        return int(linha)
    except:
        raise FileNotFoundError("Arquivo não encontrado/Arquivo com defeito. Você têm certeza que está rodando o programa corretamente?")

def cartasiniciais():
    try:
        linha = lerlinha(linha=2, inicioLinhaIndex=17)
        return int(linha)
    except:
        raise FileNotFoundError("Arquivo não encontrado/Arquivo com defeito. Você têm certeza que está rodando o programa corretamente?")


def ai():
    try:
        linha = lerlinha(linha=3, inicioLinhaIndex=15)
        if 'True' in linha:
            return True
        elif 'False' in linha:
            return False
        else:
            return TypeError("O valor booleano está sendo analisado de forma errada. O valor está digitado corretamente?")
    except:
        raise FileNotFoundError("Arquivo não encontrado/Arquivo com defeito. Você têm certeza que está rodando o programa corretamente?")