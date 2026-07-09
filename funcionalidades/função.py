from classes.personagem import * 
from rich import print
from rich.panel import Panel 

def menu():
    conteudo = "[#A5A8AF]DIGITE 1 PARA CRIAR O PERSONAGEM[/]\n"
    conteudo += "[#A5A8AF]DIGITE 2 PARA VER O STATUS DO PERSONAGEM[/]\n"
    conteudo += "[#A5A8AF]DIGITE 3 PARA BATALHAR[/]\n"
    conteudo += "[#A5A8AF]DIGITE 4 PARA SAIR DO JOGO[/]"
    menu = Panel(conteudo, title="Menu",width=55)
    print(menu)

