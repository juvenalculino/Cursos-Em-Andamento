# -*- coding: utf-8 -*-
import uteismodulo as ut
# Módulos
# Para criar modulos tem que criar a função separada e importar
# from uteismodulo import dobro, fatorial
num = int(input('Digite um valor:'))
fat = ut.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {ut.dobro(num)}')


# Vantagens da modularização
# Organização do código
# Facilidade na manutenção
# Ocultação do código detalhado
# Reutilizar em outros projetos

