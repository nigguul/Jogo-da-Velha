#########################################
#         FEITO POR nigguul             # 
#        discord → nigguul#1159         #
# e-mail:guilherme.l.lima1104@gmail.com #
#########################################


################################
#           Imports            # 
################################

from functions import *

################################
#         Main Program         # 
################################

head('Menu Principal')
while True:
    menu(['Iniciar Jogo','Sair Do Jogo'])
    linha()
    choice = input(str("Sua escolha -->"))
    linha()
    if choice == '1':
        game = True
        jogadores()
        print(f'Vamos jogar!')
        sleep(2)
        head('O Jogo é facil, primeiro você realiza a jogada depois eu!')
        if game == True:
            menuGame()
            startGame()
    elif choice == '2':
        break
    else: 
        head('ERRO. DIGITE UM VALOR VALIDO!') 
