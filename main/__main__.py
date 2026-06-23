from personagem import * 

def main(): 
    p1 = Guerreiro("kratos") 
    m1 = Monstro()

    p1.atacar(m1,10)
    m1.atacar(p1, 15)
    m1.curar()
    p1.curar()



if __name__ == "__main__":
    main()