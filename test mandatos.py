from projecto1 import *
from random import randrange

x=0
votacoes =()
while x < 22:
    votacao = (randrange(-100000,100000),randrange(0,100000),randrange(0,100000),randrange(0,100000),randrange(0,100000),randrange(0,100000),randrange(0,100000),randrange(0,100000),randrange(0,100000),randrange(0,100000),randrange(0,100000),randrange(0,100000),randrange(0,100000),randrange(0,100000),randrange(0,100000))
    votacoes += (votacao,)
    print(x,votacao)
    print(x,mandatos(x,votacao))
    x+=1
print (votacoes)

print(assembleia(votacoes))



def gera_lista():
    a=0
    lista=[]
    while a<15:
        lista+=[random.randint(0,10000000), ]
        a+=1
        soma=()
    while len(soma)<16:
        for i in lista:
            i= ((random.randint(0,1000000), random.randint(0,100000), random.randint(0,100000), random.randint(0,100000),random.randint(0,100000),random.randint(0,100000),random.randint(0,100000),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,10000),random.randint(0,100000)), )
            soma+=i
    return soma