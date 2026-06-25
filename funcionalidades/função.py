from classes.personagem import * 

def menu(): 
    print(" Digite 1 para criar personagem")
    print(" Digite 2 para ver o status do personagem")
    print(" Digite 3 para batalhar")
    print(" Digite 4 para sair do jogo")

def verificar_nivel_max(heroi, monstro):
    level_max_h = heroi.chegou_nivel_max()
    level_max_m= monstro.chegou_nivel_max()

    if level_max_m == True: 
        print(f"O {monstro.nome}({monstro._nivel_personagem}) chegou no nivel máximo")
        menu()
        navegar = int(input("Escolha uma opção: "))
    elif level_max_h == True: 
        print(f"O {heroi.nome}({heroi._nivel_personagem}) chegou no nivel maáximo ")
        menu()
        navegar = int(input("Escolha uma opção: "))


