def obter_n_cardinalidade():
    '''
    () -> lista
    function: que obtem a cardinalidade de uma matriz (linha e coluna)
    return: uma lista contendo o numero de linhas e colunas obtidas pelo usuario
    '''
    cardinalidade = []
    linhas = int(input('Linhas: '))
    cardinalidade.append(linhas)
    colunas = int(input('Colunas: '))
    cardinalidade.append(colunas)
    return cardinalidade

def criar_matriz(cardinalidade):
    '''
    (int, int) -> matriz
    recebe o numero de linhas e colunas, cria e preenche a matriz
    return: a matriz preenchida com as temperaturas medias no periodo definido pelo usuario
    '''
    matriz = []
    for i in range(cardinalidade[0]):
        linha = []
        for j in range(cardinalidade[1]):
            temp = int(input('Temperatura: '))
            linha.append(temp)
        matriz.append(linha)
    return matriz

def obter_soma_temperaturas(matriz):
    soma = 0
    for linha in matriz:
        for coluna in linha:
            soma += coluna
    return soma

def obter_maior_menor_temperatura(matriz):
    menor = matriz[0][0]
    maior = matriz[0][0]
    for linha in matriz:
        for coluna in linha:
            if coluna < menor:
                menor = coluna
            if coluna > maior:
                maior = coluna
    lista = [menor, maior]
    return lista

def obter_temperaturas_negativas(matriz):
    temp_negativas = []
    for linhas in matriz:
        for coluna in linhas:
            if coluna < 0:
                temp_negativas.append(coluna)
    return temp_negativas

def obter_media_temperaturas(matriz):
    media = obter_soma_temperaturas(matriz) / (len(matriz) * len(matriz[0]))
    return media

def imprimir_dados(matriz, soma, m_m, media, temp_negativas):
    print('================================================')
    print('==============   Relatório   ===================')
    print('================================================')
    print(f'Matriz: {matriz}')
    print(f'Soma: {soma}')
    print(f'Menor: {m_m[0]} | Maior: {m_m[1]}')
    print(f'Média: {media:.2f}')
    print(f'Temperaturas Negativas: {temp_negativas}')

def principal():
    cardinalidade = obter_n_cardinalidade()
    matriz = criar_matriz(cardinalidade)
    soma = obter_soma_temperaturas(matriz)
    m_m = obter_maior_menor_temperatura(matriz)
    media = obter_media_temperaturas(matriz)
    temp_negativas = obter_temperaturas_negativas(matriz)
    imprimir_dados(matriz, soma, m_m, media, temp_negativas)

#PROGRAMA PRINCIPAL
principal()