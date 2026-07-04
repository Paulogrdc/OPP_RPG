from classes.personagem import * 
from rich import print

def menu(): 
    print(" Digite 1 para criar personagem")
    print(" Digite 2 para ver o status do personagem")
    print(" Digite 3 para batalhar")
    print(" Digite 4 para sair do jogo")

def verificar_fim_jogo(heroi):
    resposta = heroi.chegou_nivel_max()
    if resposta == True:
        return 4
        
         
        # fazer com que o navegar receba o numeor 4 e finalize o jogo. 
