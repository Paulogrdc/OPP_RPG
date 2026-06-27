from classes.personagem import * 
from funcionalidades.função import  * 


def main(): # função principal 
    m1 = Monstro()
    menu()
    navegar = int(input("Escolha uma opção: "))

    while navegar != 4: 

        match navegar: 

            case 1: 
                print("1-Guerreiro")
                print("2-Mago")
                try: 
                    personagem = int(input("Escolha o personagem: "))
                    if personagem == 1: 
                        nome_personagem = str(input("Escolha um nome para o Guerreiro: "))
                        p1 = Guerreiro(nome_personagem)
                        print("Personagem criado com sucesso!")
                        menu()
                        navegar = int(input("Escolha uma opção: "))
                    else: 
                        nome_personagem = str(input("Escolha um nome para o Mago: "))
                        p1 = Mago(nome_personagem) 
                        print("Personagem criado com sucesso!")
                        menu()
                        navegar = int(input("Escolha uma opção: "))

                except ValueError: 
                    print("Valor invalido! Digite o núemro 1 ou 2,respectivamente,para escolher o personagem.")
            case 2: 
                print(f"O {nome_personagem} tem {p1._vida} pontos de vida e seu nivel é {p1._nivel_personagem}")
                menu()
                navegar = int(input("Escolha uma opção: "))
            case 3:
                p1.atacar(m1)
                m1.atacar(p1)
                cont_batalhando = input("Você quer continuar batalhando? Y/N: ")
                if  cont_batalhando.upper() == "N":
                    print("Você voltou Para o menu principal")
                    menu()
                    navegar = int(input("Escolha uma opção: "))
                verificar_morte(p1,m1)
               
                    


if __name__ == "__main__":
    main()