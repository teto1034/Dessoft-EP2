#Exercício 7 do PrairieLearn
from funcoes import define_posicoes
from funcoes import posicao_valida

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
} 

navios = {
    'porta-aviões' : [4],
    'navio-tanque' : [3, 3],
    'contrapedreiro' : [2, 2, 2],
    'submarino' : [1, 1, 1, 1]
}

for tipo in navios:
    for i in range(len(navios[tipo])):
        tamanho = navios[tipo][i]
        print(f'Insira as informações referentes ao navio {tipo} que possui tamanho {tamanho}')
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        if tamanho > 1:
            orientacao = int(input('[1] Vertical [2] Horizontal >'))
        if orientacao == 1:
            orientacao = 'vertical'
        elif orientacao == 2:
            orientacao = 'horizontal'
        if posicao_valida(frota, linha, coluna, orientacao, tamanho) == True:
            frota[tipo].append(define_posicoes(linha, coluna, orientacao, tamanho))
        else:
            while posicao_valida(frota, linha, coluna, orientacao, tamanho) == False:
                print('Esta posição não está válida!')
                print(f'Insira as informações referentes ao navio {tipo} que possui tamanho {tamanho}')
                linha = int(input('Linha: '))
                coluna = int(input('Coluna: '))
                if tamanho > 1:
                    orientacao = int(input('[1] Vertical [2] Horizontal >'))
            frota[tipo].append(define_posicoes(linha, coluna, orientacao, tamanho))
print(frota)