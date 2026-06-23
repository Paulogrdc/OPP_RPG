from personagem import * 

def main(): 
    p1 = Guerreiro("kratos") 
    m1 = Monstro()

    p1.atacar(m1)
    m1.atacar(p1)



if __name__ == "__main__":
    main()