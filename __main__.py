from classes.personagem import * 
from funcionalidades.função import  * 

def main(): # função principal 
    m1 = Monstro()
    menu()
    navegar = int(input("Escolha uma opção: "))

    # Cria um menu interativo 
    while navegar !=4 : 
        match navegar: 

            # case 1: escolher os personagens
            case 1: 
                print("[#716C59]1-Guerreiro")
                print("[#6F5F48]2-Mago")
                try: 
                    personagem = int(input("Escolha o personagem: "))
                    if personagem == 1: 
                        nome_personagem = str(input(" Escolha um nome para o Guerreiro: "))
                        p1 = Guerreiro(nome_personagem)
                        print("[green]Personagem criado com sucesso![/]")
                        menu() 
                        navegar = int(input("Escolha uma opção: "))
                    else: 
                        nome_personagem = str(input("Escolha um nome para o Mago: "))
                        p1 = Mago(nome_personagem) 
                        print("[green]Personagem criado com sucesso![/]")
                        menu()
                        navegar = int(input("Escolha uma opção: "))

                except ValueError: 
                    print("Valor invalido! Digite o núemro 1 ou 2,respectivamente,para escolher o personagem.")

            # case 2: Ver os status do personagem 
            case 2:
                try: 
                    p1.status_personagem()
                    menu()
                    navegar = int(input("Escolha uma opção: "))
                except UnboundLocalError: 
                    print("Você não criou nenhum personagem. Escolha a opção para criar um personagem")
                    menu()
                    navegar = int(input("Escolha uma opção: "))

            # case 3: Batalhar 
            case 3:
                try:
                    p1.atacar(m1)
                    m1.atacar(p1) 
                    if p1.vida <=0:
                        m1.reiniciar_nivel()
                        menu()
                        navegar = int(input("Escolha uma opção: "))
                    elif m1.vida <= 0: 
                        m1.dar_xp(p1)
                        p1.aumentar_nivel()
                        p1.curar()
                        m1.aumentar_nivel(p1)
                        cont_batalhando = input("Você quer continuar batalhando? Y/N: ")
                        if  cont_batalhando.upper() == "N":
                            print("Você voltou Para o menu principal")
                            menu()
                            navegar = int(input("Escolha uma opção: "))
                        if p1.chegou_nivel_max() == True or m1.chegou_nivel_max() == True: 
                            navegar = 4

                except UnboundLocalError: 
                    print(f"Escolha um personagem antes de começar a batalha.")
                    menu()
                    navegar = int(input("Escolha uma opção: ")) 
            # case 4: Sair do jogo        
            case 4:
                break 

if __name__ == "__main__":
    main()