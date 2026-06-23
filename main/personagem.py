from abc import ABC, abstractmethod

class Personagem(ABC): 
    def __init__(self):
        self.nome = ""
        self._vida = 1 # Protegido(#)
        self._nivel_personagem = 1 # Protegido(#)
        self.golpes = []

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
        self.nome = nome 
        self._barra_xp = 0 
        self._nivel_personagem = 1
        self._vida = self._nivel_personagem * 15
        self.golpes = ["soco", "joelhada", "chute"]


    def aumentar_nivel(self):
        pass 

    def curar(self):
        pass



class Mago(Personagem):
    def __init__(self, nome):
        self.nome = nome
        self._barra_xp = 0
        self._nivel_personagem = 1 
        self._vida = self._nivel_personagem * 15
        self.golpes = ["Esfera negra ", "Raio de luz", "Bola de fogo"]


    def aumentar_nivel(self):
        pass 

    def curar(self):
        pass


class Monstro(Personagem): 
    def __init__(self):
        self.nome = "monstro de level"
        self._nivel_personagem = 1  # Protegido (#)
        self._vida = self._nivel_personagem * 10 # Protegido(#)
        self._xp = 1 # Protegido (#)
        self.golpes = ["cuspir fogo", "soco", "machado cortante"] 


    def aumentar_nivel(self):
        pass 

    def dar_xp(self):
        pass 

    def curar(slef): 
        pass 
