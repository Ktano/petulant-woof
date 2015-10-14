#Grupo 34
#n. 56564 Pedro Filipe Lopes Caetano
#n. 82607 Joao Pedro Goncalves Loureiro


def mandatos (nr_mandatos,nr_votos):
    mandato=1
    nr_candidaturas = len(nr_votos)
    #e necessario um tuplo com o comprimento igual ao numero de candidaturas
    mandatos_atribuidos = cria_mandatos(nr_candidaturas) 
    while mandato <= nr_mandatos:
        mandatos_atribuidos = atribui_mandato(nr_votos,mandatos_atribuidos)
        mandato+=1
    return mandatos_atribuidos

def cria_mandatos(candidaturas):
    """
    Esta funcao cria um tuplo com o comprimento=candidaturas e 0 em todas
    as entradas
    """
    mandatos_zero=(0,)
    while len(mandatos_zero)<candidaturas:
        mandatos_zero+=(0,)
    return mandatos_zero

def atribui_mandato(votos,mandatos_atuais):
    """"
    Retorna um tuplo de mandatos com mais um mandato atribuido a proxima
    candidatura de acordo com o metodo de D'Hondt
    """
    total_candi = len(mandatos_atuais)
    #inicia as variaveis para percorrer todas as candidaturas
    candi_actual=0
    candi_venc=candi_actual
    #os votos para comparar sao calculados atraves do numero de votos a dividir
    #pelo numero de deputados ja atribuidos a candidatura mais 1
    votos_venc = votos[candi_venc]/(mandatos_atuais[candi_venc]+1)
    
    while candi_actual<(total_candi-1):
        candi_actual+=1
        votos_act = votos[candi_actual]/(mandatos_atuais[candi_actual]+1)
        #se a candidatura actual tiver mais votos ajustados que a vencedora a
        #actual passa a ser a vencedor se existir um empate a que tem menor
        #numero de votos total ganha
        if votos_venc < votos_act or \
           (votos_venc==votos_act and votos[candi_actual]<votos[candi_venc]):
            candi_venc=candi_actual
            votos_venc = votos_act
        
    return mandatos_atuais[:candi_venc] + (mandatos_atuais[candi_venc]+1,) +\
           mandatos_atuais[candi_venc+1:]
    

#utilizaremos a funcao mandatos, anteriormente definida 
#o primeiro parametro corresponde ao numero de mandatos correspondente a cada circulo,
#indicado pelo nome da variavel 

#para o numero de votos em cada partido, e num determinado circulo 
#recorreremos ao indice n do tuplo votacoes- que contem os votos para cada partido 
#num determindado circulo eleitoral


aveiro=mandatos(16,votacoes[0])
beja=mandatos(3,votacoes[1])
braga=mandatos(19,votacoes[2])
braganca=mandatos(3,votacoes[3])
castelo_branco=mandatos(4, votacoes[4])
coimbra=mandatos(9, votacoes[5])
evora=mandatos(3, votacoes[6])
faro=mandatos(9, votacoes[7])
guarda=mandatos(4, votacoes[8])
leiria=mandatos(10, votacoes[9])
lisboa=mandatos(47, votacoes[10])
portalegre=mandatos(2, votacoes[11])
porto=mandatos(39, votacoes[12])
santarem=mandatos(9, votacoes[13])
setubal=mandatos(18, votacoes[14])
viana_castelo=mandatos(6, votacoes[15])
vila_real=mandatos(5, votacoes[16])
viseu=mandatos(9, votacoes[17])
acores=mandatos(5, votacoes[18])
madeira=mandatos(6, votacoes[19])
europa=mandatos(2, votacoes[20])
fora_europa=mandatos(2, votacoes[21])

#tuplo com os resultados das candidaturas distribuidas por circulo eleitoral de modo a facilitar a manipulacao dos dados
candidaturas_votos=(aveiro, beja, braga, braganca, castelo_branco, coimbra, evora, faro, guarda, leiria, lisboa, portalegre, porto, santarem, setubal, viana_castelo, vila_real, viseu, acores, madeira, europa, fora_europa)


    
def assembleia (votacoes):
    numero_candidatura=0
    final=()
    while numero_candidatura<15:
        #coloca o numero de mandatos num tuplo 
        final+=(somas_por_candidatura(candidaturas_votos,numero_candidatura), )
        numero_candidatura+=1
    return final



def somas_por_candidatura (candidaturas_votos,numero_candidatura):
    #numero_candidatura representa o numero da candidatura como definido na tabela 
    
    """
    A partir do tuplo candidaturas_votos e de um inteiro correspondente ao numero da candidatura,
    devolve o numero total de mandatos por candidatura
    """
    soma=0                 
    while 1:            
        for i in candidaturas_votos:
            soma+=i[numero_candidatura]
        return soma

def mandatos_circulo (nr_circulo):
    """
    Calcula o numero de mandatos num determinado circulo
    """
    mandatos=(16,3,19,3,4,9,3,9,4,10,47,2,39,9,18,6,5,9,5,6,2,2)
    return mandatos[nr_circulo]