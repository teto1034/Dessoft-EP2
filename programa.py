#Exercício 7 do PrairieLearn
from funcoes import define_posicoes, posicao_valida, preenche_frota

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
} 

navios = {
    "porta-aviões":[4],
    "navio-tanque":[3, 3],
    "contratorpedeiro":[2, 2, 2],
    "submarino": [1, 1, 1, 1],
}

for tipo in navios:
        for valor in navios[tipo]:
            tamanho = valor
            while True:
                print(f"Insira as informações referentes ao navio {tipo} que possui tamanho {tamanho}")
                linha = int(input("Linha: "))
                coluna = int(input("Coluna: "))
                if tipo != 'submarino':
                    orientacao = int(input("[1] Vertical [2] Horizontal >"))
                    if orientacao == 1:
                        orientacao = 'vertical'
                    elif orientacao == 2:
                        orientacao = 'horizontal'
                if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                    define_posicoes(linha, coluna, orientacao, tamanho)
                    preenche_frota(frota, tipo, linha, coluna, orientacao, tamanho)
                    break
                else: 
                    print("Esta posição não está válida!")
print(frota)
    