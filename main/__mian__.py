from abc import ABC, abstractmethod

class Personagem(ABC): 
    def __init__(self):
        pass 


    def atacar(self):
        pass 

    def receber_dano(self):
        pass 

    @abstractmethod
    def aumentar_nivel(self): 
        pass  

    @abstractmethod
    def curar(self): 
        pass


class Guerreiro(Personagem):
    def __init__(self, nome):
        pass 



    def aumentar_nivel(self):
        pass 

    def curar(self):
        pass



class Mago(Personagem):
    def __init__(self, nome):
        pass


    def aumentar_nivel(self):
        pass 

    def curar(self):
        pass


class Monstro(Personagem): 
    def __init__(self):
        pass


    def aumentar_nivel(self):
        pass 

    def dar_xp(self):
        pass 

    def curar(slef): 
        pass 
