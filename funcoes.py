#Exercício 1 do Prairielearn
def define_posicoes(linha, coluna, orientacao, tamanho):
    listafinal = []
    if orientacao == 'vertical':
        for i in range(tamanho):
            listafinal.append([linha + i, coluna])
    elif orientacao == 'horizontal':
        for i in range(tamanho):
            listafinal.append([linha, coluna + i])
    return listafinal

#Exercício 2 do Prairielearn
def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    navio_posicao = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio not in frota:
        frota[nome_navio] = [navio_posicao]
    else:
        frota[nome_navio].append(navio_posicao)
    return frota