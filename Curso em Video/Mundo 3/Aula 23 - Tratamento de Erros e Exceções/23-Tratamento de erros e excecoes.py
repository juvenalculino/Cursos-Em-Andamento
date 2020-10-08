# -*- coding: utf-8 -*-
'''
try: # Tente
    operação

except: #alguma coisa  OU except Exception as erro: # ver erro
    falhou

else:
    deu certo

finally:
    certo/falha
try:
    b = int(input('Numerador: '))
    c = int(input('Denominador: '))
    r = b / c
except Exception as erro:
    print('Infelizmente tivemos um problema')
    print(f'Problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre')

'''
try:
    d = int(input('Numerador: '))
    e = int(input('Denominador: '))
    f = d / e
except (ValueError, TypeError):
    print('Tivemos um problema nos tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possivel dividir número por zero')
except KeyboardInterrupt:
    print('O usuário não informou os dados')
except Exception as erro:
    print('O erro encontrado foi {erro.__cause__}')


else:
    print(f'O resultado é {f}')
finally:
    print('Volte sempre')
