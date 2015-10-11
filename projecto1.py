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
