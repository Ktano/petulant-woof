from projecto1 import *
from random import *

def array_votacoes():
    x=0
    votacoes =()
    while x < 22:
        votacao = (randrange(0,100000),randrange(0,100000),randrange(0,100000),randrange(0,100000),randrange(0,100000),randrange(0,100000),randrange(0,100000),randrange(0,100000),randrange(0,100000),randrange(0,100000),randrange(0,100000),randrange(0,100000),randrange(0,100000),randrange(0,100000),randrange(0,100000))
        votacoes += (votacao,)
    
        x+=1
    return votacoes

m=0
while m<100:
    a=array_votacoes()
    print(max_mandatos(a))
    m+=1


#def gera_lista():
    #a=0
    #lista=[]
    #while a<15:
        #lista+=[randrange(0,10000000), ]
        #a+=1
        #soma=()
    #while len(soma)<16:
        #for i in lista:
            #i= ((randrange(0,1000000), randrange(0,100000), randrange(0,100000), randrange(0,100000),randrange(0,100000),randrange(0,100000),randrange(0,100000),randrange(0,100),randrange(0,100),randrange(0,100),randrange(0,100),randrange(0,100),randrange(0,100),randrange(0,10000),randrange(0,100000)), )
            #soma+=i
    #return soma