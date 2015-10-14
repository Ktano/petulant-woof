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
    
    
    
    
    
    
    
    
    
    
    votacoes = ((0, 15729, 220408, 1297, 0, 3040, 993, 0, 1354, 1046,\
0, 3284, 99652, 19327, 0), (0, 19000, 23173, 255, 0, 532, 201, 0, 306,\
232, 0, 1980, 22307, 3890, 0), (0, 23731, 244971, 1959, 0, 2710, 1465,\
0, 1094, 1114, 0, 4264, 159476, 20488, 0), (0, 1956, 47716, 282, 0, 0,\
175, 0, 165, 247, 0, 417, 19728, 1732, 0), (0, 5384, 52325, 403, 0,\
770, 543, 0, 428, 0, 0, 1454, 38317, 4609, 0), (0, 14138, 113419, 662,\
0, 2535, 600, 0, 591, 557, 0, 2014, 66199, 13034, 0), (0, 18967,\
31260, 237, 0, 649, 216, 0, 168, 207, 0, 1810, 25010, 4225, 0), (0,\
17255, 99745, 2076, 0, 3285, 0, 0, 1069, 700, 0, 3160, 46082, 16347,\
0), (0, 3299, 53450, 251, 0, 520, 199, 0, 178, 191, 0, 755, 26263,\
3114, 0), (0, 12351, 148762, 977, 0, 3029, 633, 0, 595, 453, 0, 2502,\
51518, 0, 0), (0, 111661, 560365, 4135, 0, 16913, 2410, 0, 5897, 4270,\
0, 14419, 322034, 66874, 0), (0, 7910, 26257, 176, 0, 333, 162, 0,\
151, 135, 0, 1031, 19963, 2753, 0), (0, 61832, 488402, 2413, 0, 9072,\
3386, 0, 1551, 1525, 0, 9640, 318113, 51002, 0), (0, 21347, 118028,\
1454, 0, 2220, 692, 0, 832, 726, 0, 3413, 61194, 13712, 0), (0, 82159,\
156444, 1682, 0, 6282, 1133, 0, 1595, 847, 0, 0, 112764, 29667, 0),\
(0, 6648, 76961, 384, 0, 926, 0, 0, 213, 331, 0, 1473, 35327, 5928,\
0), (0, 3656, 71840, 304, 0, 617, 254, 0, 147, 574, 0, 675, 34825,\
2784, 0), (0, 5810, 123184, 696, 0, 1229, 465, 0, 266, 626, 0, 1456,\
54107, 5786, 0), (0, 2288, 53518, 314, 0, 756, 293, 0, 219, 271, 0,\
669, 23189, 3965, 0), (0, 5096, 87597, 2560, 0, 2385, 2992, 0, 617,\
538, 0, 1967, 20360, 5568, 0), (0, 803, 6306, 101, 0, 192, 83, 0, 48,\
50, 0, 132, 7205, 602, 0), (0, 127, 8938, 87, 0, 0, 0, 0, 64, 47, 0,\
52, 2714, 165, 0))

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

