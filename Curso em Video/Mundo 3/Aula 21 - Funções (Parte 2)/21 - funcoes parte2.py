# -*- coding: utf-8 -*-

# Interactive help - Ajuda interativa
#-----------------------------------
# help() - Digitar no terminal python
# help(print)
# print(print.__doc__)
#-----------------------------------


def mens():
    print('~' * 30)

    
mens()
print('Docstrings - string de documentação')
mens()

def contador(i, f, p):
    ''' Criar docstring
    --> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da cintagem
    :return: sem retorno
    '''
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('Fim!')


contador(2, 10, 2)
help(contador) #- mostra manual da função

mens()
print('Parâmetros opcionais')
mens()

def somar(a=0, b=0, c=0):
    # Ou def somar(a, b, c=0)
    s = a + b + c
    print(f'A soma vale {s}')
    

somar(3, 2, 5)
somar(8, 4)
# Ou
somar() 

mens()
print('Escopo de Variáveis Global/Local') # Onde a variável vai ou não existir
mens()

def teste(b):
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}') # Escopo local a = 8
    print(f'B dentro vale {b}') # Escopo local b = 4
    print(f'C dentro vale {c}') # Escopo local c = 2

                             
# Programa principal
a = 5                           # Escopo Global a = 5
teste(a)
print(f'A fora vale {a}')

print('##### Mudando escopo #######')

def testeee(bb):
    global aa
    aa = 8
    bb += 4
    cc = 2
    print(f'A dentro vale {aa}') 
    print(f'B dentro vale {bb}') # Escopo local b = 9
    print(f'C dentro vale {cc}') # Escopo local c = 2

                             
# Programa principal
aa = 5                           # Escopo Global a = 8
testeee(aa)
print(f'A fora vale {aa}')

mens()
print('Retornando Valores / Return') # Return
mens()

def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = soma(3, 6, 11)
r2 = soma(9, 1)
r3 = soma(3)
print(f'Os resultados foram {r1}, {r2}, {r3}')


mens()
print('Aula Prática') 
mens()

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

print('=== Par Ou Impar ===') 
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
    
numer = int(input('Digite um número: '))
if par(numer):
    print('É par!')
else:
    print('Não é par!')
