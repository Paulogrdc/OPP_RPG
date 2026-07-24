from abc import ABC, abstractmethod
import random
from rich import print
from rich.console import Console
from rich.table import Table 

class Personagem(ABC): 
    #Atributo da classe
    max_nivel_personagem = 20 
    _nivel_personagem = 1 

    def __init__(self, nome, vida): 
        # Atributos
        self.nome = nome
        self._vida = vida  # Protegido(#)
        self.golpes = []

    # Métodos acessores 
    @property  # fazendo isso as classe filhas já herdam esse método acessor
    def vida(self): 
        return self._vida 

    @vida.setter 
    def vida(self, valor): 
        if valor <= 0: 
            self._vida = 0 
        else: 
            self._vida = valor 

    def atacar(self,alvo):
        forca = self._nivel_personagem * 5
        fator = random.randint(1,forca)
         # Só ataca se a vida de ambos for maior que 0 
        if self.vida > 0 and alvo.vida > 0: 
            # gerar um golpe aleatório 
            golpe = self.golpes[random.randrange(0,len(self.golpes))]
            print(f"[#AEA897]{self.nome}({self._nivel_personagem}) atacou o {alvo.nome}({alvo._nivel_personagem}) com um {golpe} de forca {fator}[/] \n")
            alvo.receber_dano(fator)

    def receber_dano(self,dano):
         # Gerar um numeor de 1 até a força(dano), para ver quanto de dano o alvo sofre. como se fosse um dado. 
        self.vida -= dano
        if self.vida <= 0: 
            print(f"[red]{self.nome}({self._nivel_personagem}) recebeu {dano} de dano e Morreu![/]")
        else: 
            print(f"[red]{self.nome}({self._nivel_personagem}) recebeu dano de {dano} e ficou com {self.vida} de vida[/]") 

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

class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, Personagem._nivel_personagem * 20) # nesse super init, eu só passo o que estiver dentro do init da classe mãe  
        self._barra_xp = 0 # Protegido(#)
        self._barra_xp_completar = self._nivel_personagem * 50 # Protegido(#)
        self.golpes = ["soco", "joelhada", "chute"] 

    def aumentar_nivel(self):
        if self._barra_xp >= self._barra_xp_completar:
            self._nivel_personagem += 1
            self._barra_xp = self._barra_xp_completar - self._barra_xp            
            print(f"{self.nome} Subiu de nivel e agora esta no nivel {self._nivel_personagem}")


    def chegou_nivel_max(self):
        if self._nivel_personagem == self.max_nivel_personagem: 
            print(f" [blue] O {self.nome}({self._nivel_personagem}) chegou no nivel máximo e o jogo terminou[/]")
            return True 
        

    def curar(self):
        vida_cheia = self._nivel_personagem * 20
        # se o personagem morrer, ele não pode se cuarar 
        if self.vida <= 0: 
            print(f" O {self.nome}({self._nivel_personagem}) tentou se curar, mas ele não consegiu!")
            
        # Só recupera a vida se ela estiver abaixo da vida total
        elif self.vida < vida_cheia:
            # ver o quanto de vida ele vai recuperar
            vida_curar = vida_cheia - self.vida  
            print(f"{self.nome} usou uma poção de curar e recuperou {vida_curar} pontos de sua vida")
            self.vida += vida_curar
            


class Mago(Personagem):
    def __init__(self,nome):
        super().__init__(nome,Personagem._nivel_personagem * 20) # nesse super init, eu só passo o que estiver dentro do init da classe mãe
        self._barra_xp = 0 # Protegido(#)
        self._barra_xp_completar = self._nivel_personagem * 50 # Protegido(#) 
        self.golpes = ["Esfera negra ", "Raio de luz", "Bola de fogo"]


    def aumentar_nivel(self):
        if self._barra_xp >= self._barra_xp_completar: 
            self._nivel_personagem += 1 
            self._barra_xp = self._barra_xp_completar - self._barra_xp 
            print(f"{self.nome} Subiu de nivel e agora esta no nivel {self._nivel_personagem}")


    def chegou_nivel_max(self):
        if self._nivel_personagem == self.max_nivel_personagem:
            print(f" [blue] O {self.nome}({self._nivel_personagem}) chegou no nivel máximo e o jogo terminou[/]")
            return True


    def curar(self):
        vida_cheia = self._nivel_personagem * 20
        if self.vida == 0:
            print(f"[red]O {self.nome}({self._nivel_personagem}) Não pode se curar, pois ele morreu![/]")

        elif self.vida < vida_cheia: 
            vida_curar = vida_cheia  - self.vida
            print(f"[green]{self.nome} usou uma magía de cura e recuperou {vida_curar} pontos de vida[/]")
            self.vida += vida_curar


class Monstro(Personagem): 
    max_nivel_personagem = 25 
    def __init__(self):
        super().__init__("monstro de level", Personagem._nivel_personagem * 5) 
        self._xp = 1 # Protegido (#)
        self.golpes = ["cuspir fogo", "soco", "machado cortante"] 


    def aumentar_nivel(self,alvo):
        self._nivel_personagem += 1
        self.vida = self._nivel_personagem * 5
    
    def reiniciar_nivel(self): 
        self._nivel_personagem = 1
    
    def chegou_nivel_max(self):
        if self._nivel_personagem == Monstro.max_nivel_personagem and self.vida >= 0: 
            print(f"[red]O {self.nome} máximo foi derrotado e o jogo terminou![/]")
            return True

    def dar_xp(self,alvo):
        if self.vida <= 0: 
            self._xp = self._nivel_personagem * 35
            print(f"[yellow] O {self.nome}({self._nivel_personagem}) deu {self._xp} de xp [/]")
            alvo._barra_xp += self._xp
            print(f"[yellow] O {alvo.nome} recebeu {self._xp} de xp. XP: {alvo._barra_xp}/{alvo._barra_xp_completar} [/]")
        
