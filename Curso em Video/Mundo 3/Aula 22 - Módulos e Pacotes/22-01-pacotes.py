# -*- coding: utf-8 -*-
from pacotes import numeros
# Pacotes
# Para criar pacotes tem que criar pastas separadas em uteis -> cores,datas,numeros,strings
#
#

num = int(input('Digite um valor:'))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O triplo de {num} é {numeros.triplo(num)}')
