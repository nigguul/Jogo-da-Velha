#########################################
#         FEITO POR nigguul             # 
#        discord → nigguul#1159         #
# e-mail:guilherme.l.lima1104@gmail.com #
#########################################


################################
#           Imports            # 
################################

import math
from time import sleep
from random import randint
player1 = 'player1playes.txt'
p1 = None
game = False

################################
#      Functions Program       # 
################################

def jogadores():
    global p1
    p1 = input(str('Player 1, digite seu apelido ->'))
    linha()
    sleep(1)


def linha():
    print('-=' * 30)

def head(txt):
    linha()
    print(txt.center(60))
    linha()

def menu(list):
    c = 1
    for item in list:
        print(f'{c} - {item}')
        c += 1


def menuGame():
    print('Seja bem vindo ao Jogo da Velha!')
    print('Boa sorte!')
    print("Este é o tabuleiro, e com isso ja está identificado as posições no tabuleiro")
    print()
    print(' 1 | 2 | 3')
    print('-----------')
    print(' 4 | 5 | 6')
    print('-----------')
    print(' 7 | 8 | 9')
    print()        

def recomecar():
    print()
    print(' 1 | 2 | 3')
    print('-----------')
    print(' 4 | 5 | 6')
    print('-----------')
    print(' 7 | 8 | 9')
    print()        

contarVitoriasBot = 0
contarVitoriasJogador = 0
def startGame():
    global contarVitoriasBot
    global contarVitoriasJogador
    escolhaDeJogada = str(input("Você prefere qual X ou O ? -> ").lower())
    jogadaAleatoriaDoBot = randint(1,9)
    winner = False
    posicao = ['','','','','','','','','']
    posicaoOcupada = [False,False,False,False,False,False,False,False,False]
    for rodada in range(0,9):
        if winner == True:
            break
        else:
            while True:
                if escolhaDeJogada == "x":
                    jogadaEscolhida = "X"
                    jogadaDoBot = "O"
                elif escolhaDeJogada == "O" or "0":
                    jogadaEscolhida = "O"
                    jogadaDoBot = "X"
                   
                jogada = int(str(input(f'Digite sua jogada {p1} -> ')))  

                if posicaoOcupada[jogada - 1]:
                    print('Posição Ocupada, Jogue novamente!')
                    continue
                else:
                    pass

                if jogada > 9 or jogada < 1:
                    print('Jogada invalida, jogue novamente')
                    continue

                if not posicaoOcupada[jogada - 1]:
                    posicaoOcupada[jogada - 1] = True
                    posicao[jogada -1] = jogadaEscolhida
                else:
                    continue

                print()
                print(f' {posicao[0]} | {posicao[1]} | {posicao[2]}'.center(10))
                print('-'*10)
                print(f' {posicao[3]} | {posicao[4]} | {posicao[5]}'.center(10))
                print('-'*10)
                print(f' {posicao[6]} | {posicao[7]} | {posicao[8]}'.center(10))
                print()                        

                if posicao[0] == jogadaEscolhida and posicao[1] == jogadaEscolhida and posicao[2] == jogadaEscolhida:
                    print(f'Parabens {p1}! Você ganhou :(')
                    linha()
                    jogador = 1
                    winner = True
                    break
                elif posicao[3] == jogadaEscolhida and posicao[4] == jogadaEscolhida and posicao[5] == jogadaEscolhida:
                    print(f'Parabens {p1}! Você ganhou :(')
                    linha()
                    jogador = 1
                    winner = True
                    break
                elif posicao[6] == jogadaEscolhida and posicao[7] == jogadaEscolhida and posicao[8] == jogadaEscolhida:
                    print(f'Parabens {p1}! Você ganhou :(')
                    linha()
                    jogador = 1
                    winner = True
                    break
                elif posicao[0] == jogadaEscolhida and posicao[3] == jogadaEscolhida and posicao[6] == jogadaEscolhida:
                    print(f'Parabens {p1}! Você ganhou :(')
                    linha()
                    jogador = 1
                    winner = True
                    break
                elif posicao[1] == jogadaEscolhida and posicao[4] == jogadaEscolhida and posicao[7] == jogadaEscolhida:
                    print(f'Parabens {p1}! Você ganhou :(')
                    linha()
                    jogador = 1
                    winner = True
                    break
                elif posicao[0] == jogadaEscolhida and posicao[4] == jogadaEscolhida and posicao[8] == jogadaEscolhida:
                    print(f'Parabens {p1}! Você ganhou :(')
                    linha()
                    jogador = 1
                    winner = True
                    break
                elif posicao[2] == jogadaEscolhida and posicao[4] == jogadaEscolhida and posicao[6] == jogadaEscolhida:
                    print(f'Parabens {p1}! Você ganhou :(')
                    linha()
                    jogador = 1
                    winner = True
                    break
                elif posicao[2] == jogadaEscolhida and posicao[5] == jogadaEscolhida and posicao[8] == jogadaEscolhida:
                    print(f'Parabens {p1}! Você ganhou :(')
                    linha()
                    jogador = 1
                    winner = True 
                    break    

                check = True

                for pos in posicaoOcupada:
                    if pos == False:
                        check = False
                        break

                if check:
                    print('Empatamos! ^^')
                    winner = True
                    break

                jogadaAleatoriaDoBot = randint(0,8)
                while posicaoOcupada[jogadaAleatoriaDoBot]:
                    jogadaAleatoriaDoBot = randint(0,8)

                if not posicaoOcupada[jogadaAleatoriaDoBot]:
                    posicaoOcupada[jogadaAleatoriaDoBot] = True
                    posicao[jogadaAleatoriaDoBot] = jogadaDoBot
            
                sleep(0.5)     
                print('Deixa eu pensar onde vou jogar...')
                sleep(0.5)
                print('...')
                sleep(1)
                print(f'Decidi! Tenho certeza que essa você nao esperava... hehe')
                sleep(0.5)

                print()
                print(f' {posicao[0]} | {posicao[1]} | {posicao[2]}'.center(10))
                print('-'*10)
                print(f' {posicao[3]} | {posicao[4]} | {posicao[5]}'.center(10))
                print('-'*10)
                print(f' {posicao[6]} | {posicao[7]} | {posicao[8]}'.center(10))
                print()  

                if posicao[0] == jogadaDoBot and posicao[1] == jogadaDoBot and posicao[2] == jogadaDoBot:
                    print('Hahaha eu ganhei!')
                    linha()
                    bot = 1
                    winner = True
                    break
                elif posicao[3] == jogadaDoBot and posicao[4] == jogadaDoBot and posicao[5] == jogadaDoBot:
                    print('Hahaha eu ganhei!')
                    linha()
                    bot = 1
                    winner = True
                    break
                elif posicao[6] == jogadaDoBot and posicao[7] == jogadaDoBot and posicao[8] == jogadaDoBot:
                    print('Hahaha eu ganhei!')
                    linha()
                    bot = 1
                    winner = True
                    break
                elif posicao[0] == jogadaDoBot and posicao[3] == jogadaDoBot and posicao[6] == jogadaDoBot:
                    print('Hahaha eu ganhei!')
                    linha()
                    bot = 1
                    winner = True
                    break
                elif posicao[2] == jogadaDoBot and posicao[5] == jogadaDoBot and posicao[8] == jogadaDoBot:
                    print('Hahaha eu ganhei!')
                    linha()
                    bot = 1
                    winner = True
                    break
                elif posicao[0] == jogadaDoBot and posicao[4] == jogadaDoBot and posicao[8] == jogadaDoBot:
                    print('Hahaha eu ganhei!')  
                    linha()
                    bot = 1
                    winner = True
                    break
                elif posicao[2] == jogadaDoBot and posicao[4] == jogadaDoBot and posicao[6] == jogadaDoBot:
                    print('Hahaha eu ganhei!')
                    linha()
                    bot = 1
                    winner = True
                    break
                elif posicao[1] == jogadaDoBot and posicao[4] == jogadaDoBot and posicao[7] == jogadaDoBot:
                    print('Hahaha eu ganhei!')
                    linha()
                    bot = 1
                    winner = True  
                    break      

                jogador = 0
                bot = 0



    if winner == True:
        if bot == 0 and jogador == 0:
            print(f'Atualmente o placar é de → Eu 0 | Você 0')
        elif bot == 1 and jogador == 0:
            contarVitoriasBot = 0 + bot
            if contarVitoriasBot == 0:
                print(f'Atualmente o placar é de → Eu 1 | Você {contarVitoriasJogador}')
                linha()
            elif contarVitoriasBot > 0:
                print(f'Atualmente o placar é de → Eu {contarVitoriasBot} | Você {contarVitoriasJogador}')
                linha()
        elif bot == 0 and jogador == 1:
            contarVitoriasJogador = 0 + jogador
            if contarVitoriasJogador == 0:
                print(f'Atualmente o placar é de → Eu {contarVitoriasBot} | Você 1')
                linha()
            elif contarVitoriasJogador > 0:
                print(f'Atualmente o placar é de → Eu {contarVitoriasBot} | Você {contarVitoriasJogador}')
                linha()
        reiniciarJogo = str(input('Quer uma revanche? (S/N) -> ')).lower()
        linha()
        if reiniciarJogo == "s":
            recomecar()
            startGame()
        elif reiniciarJogo == "n":
            pass
    else: 
        pass
