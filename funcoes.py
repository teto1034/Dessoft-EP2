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