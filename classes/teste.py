from personagem import * 
from rich import inspect 



p = Mago("Paulo")

p.vida = 50

inspect(p, private= True, methods=True)


