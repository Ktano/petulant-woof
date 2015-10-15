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





def tuplo_mandatos():
    """
    Cria um tuplo de tuplos com os mandatos distribuidos pelo respectivo circulo eleitoral apos fornecido um tuplo, ''votacoes''
    """
    mandatos_circulo=(16,3,19,3,4,9,3,9,4,10,47,2,39,9,18,6,5,9,5,6,2,2)
    tuplo_mandatos_circulo=()
    circulos=0
    while circulos<22:
        for i in mandatos_circulo:
            tuplo_mandatos_circulo+=(mandatos(i, votacoes[circulos]), )
            circulos+=1
    return tuplo_mandatos_circulo



def somas_por_candidatura (nr_candidatura):
    #nr_candidatura representa o numero da candidatura como definido na tabela
    #usaremos esta funcao para somar os mandatos por candidatura distribuidos pelos diferentes circulos eleitorais
    
    """
    Para um numero de candidatura (como definido na tabela), soma os mandatos dos diferentes circulos eleitorais
    """
    THIS_IS_A_COMIC_RELIEF=tuplo_mandatos()
    soma_dos_mandatos=0                 
    while 1:
        for i in THIS_IS_A_COMIC_RELIEF:
            soma_dos_mandatos+=i[nr_candidatura]
        return soma_dos_mandatos
    
    

def assembleia (votacoes):
    #reune todas as somas por candidatura num tuplo com 15 entradas- correspondentes às candidaturas
    nr_candidatura=0         
    tuplo_assembleia=()
    while nr_candidatura<15:
        tuplo_assembleia+=(somas_por_candidatura(nr_candidatura), )
        nr_candidatura+=1
    return tuplo_assembleia
