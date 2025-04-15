from random import randint, shuffle
from termcolor import colored
from colorama import Fore, Back, Style


class Dado:
    def __init__(self, cor, lados, lado_sorteado):
        self.cor = cor
        self.lados = lados
        self.lado_sorteado = lado_sorteado


class Jogador:
    def __init__(self, nomes, cerebros, tiros):
        self.nome = nomes
        self.cerebros = cerebros
        self.tiros = tiros


# Função para as siglas das faces do dado
def sigla_das_faces(argument):
    switcher = {
        "C": "Cérebro",
        "P": "Passo",
        "T": "Tiro",
    }
    return switcher.get(argument, "Teste")


# Função para ajogar os dados
def joga_dado(lista_dados):
    dado = lista_dados.pop()
    num_sorteado = randint(0, 5)
    dado.lado_sorteado = dado.lados[num_sorteado]
    if dado.cor == 'Verde':
        print("Dado sorteado: " + Fore.GREEN + 'VERDE - ' + sigla_das_faces(dado.lado_sorteado) + Fore.RESET)
    elif dado.cor == 'Amarelo':
        print("Dado sorteado: " + Fore.YELLOW + 'AMARELO - ' + sigla_das_faces(dado.lado_sorteado) + Fore.RESET)
    else:
        print("Dado sorteado: " + Fore.RED + 'VERMELHO - ' + sigla_das_faces(dado.lado_sorteado) + Fore.RESET)
    return dado


# Função verificar a sigla da face do dado
def verifica_tipo_lado(lista_dados_jogados, jogador_atual):
    for dado in lista_dados_jogados:
        if dado.lado_sorteado == "C":
            jogador_atual.cerebros = jogador_atual.cerebros + 1
        elif dado.lado_sorteado == "T":
            jogador_atual.tiros = jogador_atual.tiros + 1


aluna = "Brenda Marcela de Menezes Bertolo"
curso = "Análise e desenvolvimento de Sistema"

print(aluna)
print(curso)

# Apresentação do jogo
print('\n' + colored('                                  WELCOME TO                                  ',
                     'red', attrs=['reverse', 'blink']) + '\n')
print(Fore.RED + '███████╗ ██████╗ ███╗   ███╗██████╗ ██╗███████╗    ██████╗ ██╗ ██████╗███████╗')
print("╚══███╔╝██╔═══██╗████╗ ████║██╔══██╗██║██╔════╝    ██╔══██╗██║██╔════╝██╔════╝")
print("  ███╔╝ ██║   ██║██╔████╔██║██████╔╝██║█████╗      ██║  ██║██║██║     █████╗  ")
print(" ███╔╝  ██║   ██║██║╚██╔╝██║██╔══██╗██║██╔══╝      ██║  ██║██║██║     ██╔══╝  ")
print("███████╗╚██████╔╝██║ ╚═╝ ██║██████╔╝██║███████╗    ██████╔╝██║╚██████╗███████╗")
print("╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚═╝╚══════╝    ╚═════╝ ╚═╝ ╚═════╝╚══════╝")
print(Fore.RESET + '')

# Dados de entrada dos jogadores. Quantidade e Nomes.
num_jogadores = 0

# Enquanto digitar menos que 2, o jogo não continua
while num_jogadores < 2:
    num_jogadores = int(input("INFORME O NUMERO DE JOGADORES: "))

    if num_jogadores < 2:
        print('\n' + colored('                ERRO: VOCÊ PRECISA DE NO MÍNIMO 2 JOGADORES                  ', 'red',
                             attrs=['reverse', 'blink']) + '\n')

lista_usuarios = []

# Executa o comando abaixo de acordo com a quantidade de usuários mencionados
for i in range(num_jogadores):
    nome = input('Informe o nome do jogador ' + str(i + 1) + ': ')
    lista_usuarios.append(Jogador(nome, 0, 0))

# Setando as faces dos Dados.
lados_dado_verde = ["C", "P", "C", "T", "P", "C"]
lados_dado_amarelo = ["T", "P", "C", "T", "P", "C"]
lados_dado_vermelho = ["T", "P", "T", "C", "P", "T"]

dado_verde = Dado("Verde", lados_dado_verde, "")
dado_amarelo = Dado("Amarelo", lados_dado_amarelo, "")
dado_vermelho = Dado("Vermelho", lados_dado_vermelho, "")

lista_dados = [
    dado_verde, dado_verde, dado_verde, dado_verde, dado_verde, dado_verde,
    dado_amarelo, dado_amarelo, dado_amarelo, dado_amarelo,
    dado_vermelho, dado_vermelho, dado_vermelho
]

alguem_ganhou = False

lista_dados_jogados = []

# Inicio do jogo.
print('\n' + colored('                                START GAME...                                 ',
                     'red', attrs=['reverse', 'blink']))

# Enquanto a variavel alguem_ganhou for False, irá continuar o jogo
while not alguem_ganhou:
    for jogador_atual in lista_usuarios:
        print('\n' + Fore.BLACK + Back.LIGHTWHITE_EX + Style.BRIGHT + 'TURNO DO JOGADOR: '
              + jogador_atual.nome + Style.RESET_ALL)

        shuffle(lista_dados)
        num_sorteado = randint(0, 5)

        d1 = joga_dado(lista_dados)
        d2 = joga_dado(lista_dados)
        d3 = joga_dado(lista_dados)

        shuffle(lista_dados)

        lista_dados_jogados.clear()
        lista_dados_jogados.append(d1)
        lista_dados_jogados.append(d2)
        lista_dados_jogados.append(d3)

        verifica_tipo_lado(lista_dados_jogados, jogador_atual)

        lista_dados.append(d1)
        lista_dados.append(d2)
        lista_dados.append(d3)

        shuffle(lista_dados)

        print('\n' + Fore.BLACK + Back.LIGHTWHITE_EX + Style.BRIGHT + 'SCORE ATUAL de ' + jogador_atual.nome + ':' +
              Style.RESET_ALL)
        print("CÉREBROS:", jogador_atual.cerebros)
        print("TIROS: " + str(jogador_atual.tiros) + '\n')

        for jogador in lista_usuarios:
            # Verificar se a quantidade de cérebros atingiu 13
            if jogador.cerebros >= 13:
                print('O jogador ', jogador.nome, ' Ganhou\n')
                print(colored('O jogador ' + jogador.nome + ' Ganhou', 'green', attrs=['reverse', 'blink']))
                alguem_ganhou = True

        for jogador in lista_usuarios:
            # Verificar se a quantidade de tiros atingiu 3. Se sim, retira o usuário do jogo
            if jogador.tiros >= 3:
                print(colored('O jogador ' + jogador.nome + ' Perdeu', 'red', attrs=['reverse', 'blink']))
                lista_usuarios.remove(jogador)

        if len(lista_usuarios) == 1:
            print(colored('O jogador ' + lista_usuarios[0].nome + ' Ganhou', 'green', attrs=['reverse', 'blink']))
            alguem_ganhou = True
            break

print('\n' + colored('                                GAME OVER!!!                                  ', 'red', attrs=[
    'reverse', 'blink']) + '\n')
