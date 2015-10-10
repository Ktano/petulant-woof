def mandatos (nr_mandatos,nr_votos):
    mandato=1
    nr_candidaturas = len(nr_votos) 
    mandatos_atribuidos = cria_mandatos(nr_candidaturas) #cria um tuplo com o comprimento igual ao numero de candidaturas
    while mandato <= nr_mandatos:
        mandatos_atribuidos = atribui_mandato(nr_votos,mandatos_atribuidos)
        mandato+=1

def cria_mandatos(candidaturas):
    """
    Esta funcao cria um tuplo com o comprimento=candidaturas e 0 em todas as entradas
    """
    mandatos_zero=(0,)
    while len(mandatos_zero)<candidaturas:
        mandatos_zero+=(0,)
