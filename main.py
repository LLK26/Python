'''import math

def areaCirculo(raio):
    result = math.pi * raio * raio
    return result

print(areaCirculo(raio = int(input('Digite o raio do circulo: '))))
'''

def menu():
    print('|| Menu ||')
    print('1-| Adição |')
    print('2-|Subtração|')
    print('3-|Multiplicação|')
    print('4-|Divisão')
    op = int(input('opção: '))
    return op

def adicao(n1, n2):
    r = n1 + n2
    return r

def subtracao(n1, n2):
    r = n1 - n2
    return r

def multiplicacao(n1, n2):
    r = n1 * n2
    return r

def divisao(n1, n2):
    r = n1 / n2
    return r

def result(op):
    if op == 1:
        print(adicao(n1 = int(input('Digite o primeiro número: ')), n2 = int(input('Digite o segundo número: '))))

    if op == 2:
        print(subtracao(n1 = int(input('Digite o primeiro número: ')), n2 = int(input('Digite o segundo número: '))))

    if op == 3:
        print(multiplicacao(n1=int(input('Digite o primeiro número: ')), n2=int(input('Digite o segundo número: '))))

    if op == 4:
        print(divisao(n1=int(input('Digite o primeiro número: ')), n2=int(input('Digite o segundo número: '))))

    else:
        print('Opção inválida, por favor reinicie o programa :)')

op = menu()
result(op)


