from abc import ABC, abstractmethod
import random
from rich import print
from rich.console import Console
from rich.table import Table 

class Personagem(ABC):
    max_nivel_personagem = 20 
    def __init__(self):
        self.nome = ""
        self._vida = 1 # Protegido(#)
        self._nivel_personagem = 1 # Protegido(#)
        self.golpes = []

    def atacar(self,alvo):
        forca = self._nivel_personagem * 5
        fator = random.randint(1,forca)
         # Só ataca se a vida de ambos for maior que 0 
        if self._vida > 0 and alvo._vida > 0: 
            # gerar um golpe aleatório 
            golpe = self.golpes[random.randrange(0,len(self.golpes))]
            print(f"{self.nome}({self._nivel_personagem}) atacou o {alvo.nome}({alvo._nivel_personagem}) com um {golpe} de forca {fator}")
            alvo.receber_dano(fator)

    def receber_dano(self,dano):
         # Gerar um numeor de 1 até a força(dano), para ver quanto de dano o alvo sofre. como se fosse um dado. 
        self._vida -= dano
        if self._vida <= 0: 
            print(f"{self.nome}({self._nivel_personagem}) recebeu {dano} de dano e Morreu!")
        else: 
            print(f"{self.nome}({self._nivel_personagem}) recebeu dano de {dano} e ficou com {self._vida} de vida ") 

    def status_personagem(self):
        # Colunas
        caixa = Table(title="Personagens")
        caixa.add_column("Categoria")
        caixa.add_column("Nome")
        caixa.add_column("Nivel")
        caixa.add_column("Vida")

        # Linhas 
        caixa.add_row(str(self.__class__.__name__), self.nome, str(self._nivel_personagem), str(self._vida))
        console = Console()
        console.print(caixa)

    @abstractmethod
    def aumentar_nivel(self): 
        pass  

    @abstractmethod
    def chegou_nivel_max(self):
        pass

    @abstractmethod
    def curar(self): 
        pass


class Guerreiro(Personagem):
    def __init__(self, nome):
        self.nome = nome 
        self._barra_xp = 0 # 175
        self._nivel_personagem = 1
        self._barra_xp_completar = self._nivel_personagem * 50
        self._vida = self._nivel_personagem * 20
        self.golpes = ["soco", "joelhada", "chute"]


    def aumentar_nivel(self):
        if self._barra_xp >= self._barra_xp_completar:
            self._barra_xp_completar = self._nivel_personagem * 50 
            self._barra_xp = self._barra_xp_completar - self._barra_xp 
            self._nivel_personagem += 1
            print(f"{self.nome} Subiu de nivel e agora esta no nivel {self._nivel_personagem}")


    def chegou_nivel_max(self):
        if self._nivel_personagem == self.max_nivel_personagem: 
            print(f" [blue] O {self.nome}({self._nivel_personagem}) chegou no nivel máximo e o jogo terminou[/]")
            return True 
        

    def curar(self):
        vida_cheia = self._nivel_personagem * 20
        # se o personagem morrer, ele não pode se cuarar 
        if self._vida <= 0: 
            print(f" O {self.nome}({self._nivel_personagem}) tentou se curar, mas ele não consegiu!")
            
        # Só recupera a vida se ela estiver abaixo da vida total
        elif self._vida < vida_cheia:
            # ver o quanto de vida ele vai recuperar
            vida_curar = vida_cheia - self._vida  
            print(f"{self.nome} usou uma poção de curar e recuperou {vida_curar} pontos de sua vida")
            self._vida = self._vida + vida_curar
            


class Mago(Personagem):
    def __init__(self, nome):
        self.nome = nome
        self._barra_xp = 0
        self._nivel_personagem = 1
        self._barra_xp_completar = self._nivel_personagem * 50 
        self._vida = self._nivel_personagem *20
        self.golpes = ["Esfera negra ", "Raio de luz", "Bola de fogo"]


    def aumentar_nivel(self):
        if self._barra_xp >= self._barra_xp_completar: 
            self._barra_xp_completar = self._nivel_personagem * 50 
            self._barra_xp = self._barra_xp_completar - self._barra_xp 
            self._nivel_personagem += 1
            print(f"{self.nome} Subiu de nivel e agora esta no nivel {self._nivel_personagem}")


    def chegou_nivel_max(self):
        if self._nivel_personagem == self.max_nivel_personagem:
            print(f" [blue] O {self.nome}({self._nivel_personagem}) chegou no nivel máximo e o jogo terminou[/]")
            return True


    def curar(self):
        vida_cheia = self._nivel_personagem * 20
        if self._vida == 0:
            print(f"O {self.nome}({self._nivel_personagem}) Não pode se curar, pois ele morreu!")

        elif self._vida < vida_cheia: 
            vida_curar = vida_cheia  - self._vida
            print(f"{self.nome} usou uma magía de cura e recuperou {vida_curar} pontos de vida")
            self._vida += vida_curar


class Monstro(Personagem): 

    def __init__(self):
        self.nome = "monstro de level"
        self._nivel_personagem = 1  # Protegido (#)
        self._vida = self._nivel_personagem * 5  # Protegido(#)
        self._xp = 1 # Protegido (#)
        self.golpes = ["cuspir fogo", "soco", "machado cortante"] 


    def aumentar_nivel(self):
        self._nivel_personagem += 1
        self._vida = self._nivel_personagem * 5
    
    def chegou_nivel_max(self):
        if self._nivel_personagem == self.max_nivel_personagem: 
            print(f"O {self.nome}({self._nivel_personagem}) chegou no nivel máximo. [red]Hora da batalha final![/] ")

    def dar_xp(self,alvo):
        if self._vida <= 0: 
            self._xp = self._nivel_personagem * 25
            print(f"O {self.nome} Morreu e deu {self._xp} de xp")
            alvo._barra_xp = self._xp
            print(f"O {alvo.nome} recebeu {self._xp} de xp. XP: {alvo._barra_xp}/{alvo._barra_xp_completar}")
        

    # ajustar o metodo curar do monstro
    def curar(self):
        vida_cheia = self._nivel_personagem * 10
        if self._vida == 0: 
            print(f"O {self.nome}({self._nivel_personagem}) não pode se curar, pois ele morreu!")

        elif self._vida < vida_cheia and self._nivel_personagem >= 90:
            vida_curar = self._vida - vida_cheia  
            self._vida += vida_curar
            print(f"O {self.nome}({self._nivel_personagem}) usou uma magia negra e recuperou {vida_curar} pontos de vida. ") 

        else: 
            print(f"O {self.nome}({self._nivel_personagem}) tentou usar magia negra para reupearar sua vida, mas ele não tem o nível necessário")

