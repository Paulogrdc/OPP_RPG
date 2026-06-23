from abc import ABC, abstractmethod
import random

class Personagem(ABC): 
    def __init__(self):
        self.nome = ""
        self._vida = 1 # Protegido(#)
        self._nivel_personagem = 1 # Protegido(#)
        self.golpes = []

    def atacar(self,alvo, forca = 50):
         # Só ataca se a vida de ambos for maior que 0 
        if self._vida > 0 and alvo._vida > 0: 
            # gerar um golpe aleatório 
            golpe = self.golpes[random.randrange(0,len(self.golpes))]
            print(f"{self.nome}({self._nivel_personagem}) atacou o {alvo.nome}({alvo._nivel_personagem}) com um {golpe} de forca {forca}")
            alvo.receber_dano(forca)

    def receber_dano(self,dano):
         # Gerar um numeor de 1 até a força(dano), para ver quanto de dano o alvo sofre. como se fosse um dado. 
        fator = random.randint(1,dano)
        self._vida -= fator
        if self._vida <= 0: 
            print(f"{self.nome}({self._nivel_personagem}) recebeu {fator} de dano e Morreu!")
        else: 
            print(f"{self.nome}({self._nivel_personagem}) recebeu dano de {fator} e ficou com {self._vida} de vida ") 

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
        if self._barra_xp > 50: 
            self._nivel_personagem += 1 

    def curar(self):
        fator = random.randint(0,self._vida)
        self._vida += fator
        print(f"{self.nome} usou uma poção de curar e recuperou {fator} pontos de sua vida")


class Mago(Personagem):
    def __init__(self, nome):
        self.nome = nome
        self._barra_xp = 0
        self._nivel_personagem = 1 
        self._vida = self._nivel_personagem * 15
        self.golpes = ["Esfera negra ", "Raio de luz", "Bola de fogo"]


    def aumentar_nivel(self):
        if self._barra_xp > 50: 
            self._nivel_personagem += 1

    def curar(self):
        fator = random.randint(1,self._vida)
        self._vida += fator
        print(f"{self.nome} usou uma magía de cura e recuperou {fator} pontos de vida")


class Monstro(Personagem): 
    def __init__(self):
        self.nome = "monstro de level"
        self._nivel_personagem = 1  # Protegido (#)
        self._vida = self._nivel_personagem * 10 # Protegido(#)
        self._xp = 1 # Protegido (#)
        self.golpes = ["cuspir fogo", "soco", "machado cortante"] 


    def aumentar_nivel(self):
        self._nivel_personagem += 1
        self._vida = self._nivel_personagem * 10
        if self._nivel_personagem == 100: 
            print("Você chegou no boss de nível máximo") 

    def dar_xp(self):
        pass

    def curar(self):
        fator = random.randint(1,self._vida) 
        if self._nivel_personagem >= 90:
            print(f"O {self.nome}({self._nivel_personagem}) usou uma magia negra e recuperou {fator} pontos de vida. ") 
        else: 
            print(f"O {self.nome}({self._nivel_personagem}) tentou usar magia negra para reupearar sua vida, mas ele não tem o nível necessário")

