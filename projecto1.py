#Grupo 34
#n. 56564 Pedro Filipe Lopes Caetano
#n. 82607 Joao Pedro Goncalves Loureiro

def mandatos (nr_mandatos,nr_votos):
    mand=1
    nr_cand = len(nr_votos)
    #e necessario um tuplo com o comprimento igual ao numero de candidaturas
    mand_atri = cria_mand(nr_cand) 
    while mand <= nr_mandatos:
        mand_atri = atribui_mand(nr_votos,mand_atri)
        mand+=1
    return mand_atri

def cria_mand(nr_cand):
    """
    Esta funcao cria um tuplo com o comprimento=nr_cand e 0 em todas
    as entradas
    """
    mand_zero=(0,)
    while len(mand_zero)<nr_cand:
        mand_zero+=(0,)
    return mand_zero

def atribui_mand(votos,mand_atuais):
    """"
    Retorna um tuplo de mandatos com mais um mandato atribuido a proxima
    candidatura de acordo com o metodo de D'Hondt
    """
    total_candi = len(mand_atuais)
    #inicia as variaveis para percorrer todas as candidaturas
    candi_actual=0
    candi_venc=candi_actual
    #os votos para comparar sao calculados atraves do numero de votos a dividir
    #pelo numero de deputados ja atribuidos a candidatura mais 1
    votos_venc = votos[candi_venc]/(mand_atuais[candi_venc]+1)
    
    while candi_actual<(total_candi-1):
        candi_actual+=1
        votos_act = votos[candi_actual]/(mand_atuais[candi_actual]+1)
        #se a candidatura actual tiver mais votos ajustados que a vencedora a
        #actual passa a ser a vencedor se existir um empate a que tem menor
        #numero de votos total ganha
        if votos_venc < votos_act or \
           (votos_venc==votos_act and votos[candi_actual]<votos[candi_venc]):
            candi_venc=candi_actual
            votos_venc = votos_act
        
    return mand_atuais[:candi_venc] + (mand_atuais[candi_venc]+1,) +\
           mand_atuais[candi_venc+1:]





def tuplo_mandatos(votacoes):
    """
    Cria um tuplo de tuplos com os mandatos distribuidos pelo respectivo circulo
    eleitoral apos fornecido um tuplo em que cada entrada tem um tuplo de votos 
    em cada uma das candidaturas para um determinado circulo
    """
    mand_atrib_circ=()
    circ=0
    total_circ=len(votacoes)
    while circ<total_circ:
        mand_atrib_circ+=(mandatos(mand_cir(circ), votacoes[circ]), )
        circ+=1
    return mand_atrib_circ



def somas_por_candidatura (nr_candidatura,mand_circ):
    #nr_candidatura representa o numero da candidatura como definido na tabela
    #usaremos esta funcao para somar os mandatos por candidatura distribuidos
    #pelos diferentes circulos eleitorais
    
    """
    Para um numero de candidatura (como definido na tabela), soma os mandatos
    dos diferentes circulos eleitorais
    """
    soma_dos_mandatos=0                 
    for i in mand_circ:
        soma_dos_mandatos+=i[nr_candidatura]
    return soma_dos_mandatos
    
    

def assembleia (votacoes):
    #reune todas as somas por candidatura num tuplo com 15 entradas-
    #correspondentes as candidaturas
    nr_candidatura=0
    mand_circ=tuplo_mandatos(votacoes)
    tuplo_assembleia=()
    while nr_candidatura<15:
        tuplo_assembleia+=(somas_por_candidatura(nr_candidatura,mand_circ), )
        nr_candidatura+=1
    return tuplo_assembleia


def mand_cir (nr_cir):
    """
    Calcula o numero de mandatos num determinado circulo
    """
    nr_mand=(16,3,19,3,4,9,3,9,4,10,47,2,39,9,18,6,5,9,5,6,2,2)
    return nr_mand[nr_cir]

def max_mandatos(votacoes):
    assembleia_final=assembleia(votacoes)
    candi_act=0
    candi_venc=candi_act
    empate=False
    total_candi=len(assembleia_final)
    while  candi_act<total_candi:
        if assembleia_final[candi_act]>assembleia_final[candi_venc]:
            candi_venc=candi_act
            empate=False
        elif assembleia_final[candi_act]==assembleia_final[candi_venc]:
            empate=True
        candi_act+=1
    if empate:
        return 'Empate tecnico'
    return nome_candidatura(candi_venc)
    




def nome_candidatura(posicao):
    designacao = ('Partido Democratico Republicano',\
                  'CDU - Coligacao Democratica Unitaria',\
                  'Portugal a Frente',\
                  'Partido da Terra',\
                  'LIVRE/Tempo de Avancar',\
                  'Pessoas-Animais-Natureza',\
                  'Agir',\
                  'Juntos pelo Povo',\
                  'Partido Nacional Renovador',\
                  'Partido Popular Monarquico',\
                  'Nos, Cidadaos!',\
                  'Partido Comunista dos Trabalhadores Portugueses',\
                  'Partido Socialista',\
                  'Bloco de Esquerda',\
                  'Partido Unido dos Reformados e Pensionistas')
                  
                  
    abreviatura =('PDR',\
                  'PCP-PEV',\
                  'PPD/PSD-CDS/PP',\
                  'MPT',\
                  'L/TDA',\
                  'PAN',\
                  'PTP-MAS',\
                  'JPP',\
                  'PNR',\
                  'PPM',\
                  'NC',\
                  'PCTP/MRPP',\
                  'PS',\
                  'B.E.',\
                  'PURP')
    
    return  abreviatura[posicao] +'\t' + designacao[posicao]
