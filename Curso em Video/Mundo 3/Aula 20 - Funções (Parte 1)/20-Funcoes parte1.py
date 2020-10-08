# -*- coding: utf-8 -*-
def lin(): # Função sem parâmetro
    print('--' * 15)
    
    
# Pular duas linhas
# Programa principal
lin()
print('  Curso de Python  ')
lin()

print('|||' * 10) # --------------------

def titulo(txt): # Função com parâmetro
    print('--' * 15)
    print(txt)
    print('--' * 15)

    
titulo('  Hacking Python  ')
titulo('  Python Teste    ')
titulo('  A vida é bela  ')

print('|||' * 10) # --------------------


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
    

# Programa principal
soma(4, 5)
soma(b=2, a=19)

print('|||' * 10) # --------------------



# Empcotar parâmetro
# *Desempacotar
def contador(*  num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')
    for valor in num:
        print(f'{valor} ', end='')
    print('Fim..')


contador(5, 7, 3, 1, 4)
contador(8, 4, 7)
contador(1, 9)

print('|||' * 10) # --------------------


# Trabalhando valores com listas
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)

print('|||' * 10) # --------------------


def somaa(* valoress):
    ss = 0
    for numm in valoress:
        ss += numm
    print(f'Somando os valores {valoress} temos {ss}')
    
somaa(5, 2)
somaa(2, 9, 4)

print('|||' * 10) # --------------------
