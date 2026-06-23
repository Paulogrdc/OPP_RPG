from classes.personagem import * 
from funcionalidades.função import  * 


def main(): 
    menu()
    navegar = int(input("Escolha uma opção: "))

    match navegar: 

        case 1: 
            print("1-Guerreiro")
            print("2-Mago")
            try: 
                personagem = int(input("Escolha o personagem: "))
                if personagem == 1: 
                    nome_personagem = str(input("Escolha um nome para o personagem: "))
                    p1 = Guerreiro(nome_personagem)
                    print("Personagem criado com sucesso!")
                else: 
                    nome_personagem = str(input("Escolha um nome para o personagem: "))
                    p1 = Mago(nome_personagem) 
                    print("Personagem criado com sucesso!")
            except ValueError: 
                print("Valor invalido! Digite o núemro 1 ou 2,respectivamente,para escolher o personagem.")
            
            

if __name__ == "__main__":
    main()