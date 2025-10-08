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

#Exercício 3 do Prairielearn
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    elif tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    return tabuleiro

#Exercício 4 do Prairielearn
def posiciona_frota(frota):
    tabuleiro = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        tabuleiro.append(linha)

    for tipo in frota:
        for unidade in frota[tipo]:
            for i in range(10):
                for j in range(10):
                    if [i, j] in unidade:
                        tabuleiro[i][j] = 1
    return tabuleiro

#Exercício 5 do PraireLearn
def afundados(frota, tabuleiro):
    quantos_afundados = 0
    for tipo in frota:
        for navio in frota[tipo]:
            afundado = True
            for posicao in navio:
                if tabuleiro[posicao[0]][posicao[1]] == 1:
                    afundado = False
                    continue
            if afundado:
                quantos_afundados += 1
    return quantos_afundados