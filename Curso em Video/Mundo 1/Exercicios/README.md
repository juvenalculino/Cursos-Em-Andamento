```
"""
EXERCÍCIO 001: Olá, Mundo!

Crie um programa que escreva "Olá, Mundo!" na tela.
"""
msg = 'Olá, Mundo!'
print(msg)
```

```
"""
EXERCÍCIO 002: Respondendo ao Usuário

Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
"""
nome = input('Digite seu nome: ')
print('É um prazer te conhecer, {}!'.format(nome))
```


```
"""
EXERCÍCIO 003: Somando Dois Números

Crie um programa que leia dois números e mostre a soma entre eles.
"""
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
print('A soma entre {} e {} é igual a {}!'.format(n1, n2, s))
```


```
"""
EXERCÍCIO 004: Dissecando uma Variável

Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.
"""
a = input('Digite algo: ')
print('O tipo primitivo deste valor é: {}'.format(type(a)))
print('Só tem espaços? {}'.format(a.isspace()))
print('É um número? {}'.format(a.isnumeric()))
print('É alfabético? {}'.format(a.isalpha()))
print('É alfanumérico? {}'.format(a.isalnum()))
print('Está em maiúsculas? {}'.format(a.isupper()))
print('Está em minúsculas? {}'.format(a.islower()))
print('Está capitalizada? {}'.format(a.istitle()))
```


```
"""
EXERCÍCIO 005: Antecessor e Sucessor

Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
"""
n = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}!'.format(n, (n - 1), (n + 1)))
```


```
"""
EXERCÍCIO 006: Dobro, Triplo, Raiz Quadrada

Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""
n = int(input('Digite um número: '))
print('O dobro de {} vale {}.'.format(n, (n * 2)))
print('O triplo de {} vale {}.'.format(n, (n * 3)))
print('A raiz quadrada de {} é igual a {:.2f}.'.format(n, pow(n, (1 / 2))))
```


```
"""
EXERCÍCIO 007: Média Aritmética

Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1 + n2) / 2
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}.'.format(n1, n2, m))
```


```
"""
EXERCÍCIO 008: Conversor de Medidas

Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""
medida = float(input('Uma distância em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a:'.format(medida))
print('{} km\n{} hm\n{} dam\n{:.0f} dm\n{:.0f} cm\n{:.0f} mm'.format(km, hm, dam, dm, cm, mm))
```


```
"""
EXERCÍCIO 009: Tabuada

Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
"""
num = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
print('{} x {:2} = {}'.format(num, 1, num * 1))
print('{} x {:2} = {}'.format(num, 2, num * 2))
print('{} x {:2} = {}'.format(num, 3, num * 3))
print('{} x {:2} = {}'.format(num, 4, num * 4))
print('{} x {:2} = {}'.format(num, 5, num * 5))
print('{} x {:2} = {}'.format(num, 6, num * 6))
print('{} x {:2} = {}'.format(num, 7, num * 7))
print('{} x {:2} = {}'.format(num, 8, num * 8))
print('{} x {:2} = {}'.format(num, 9, num * 9))
print('{} x {:2} = {}'.format(num, 10, num * 10))
print('-' * 12)
```


```
"""
EXERCÍCIO 010: Conversor de Moedas

Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos Dólares ela pode comprar.

Considere U$ 1,00 = R$ 3,27
"""
real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 3.27
print('Com R$ {:.2f} você pode comprar U$ {:.2f}.'.format(real, dolar))
```


```
"""
EXERCÍCIO 011: Pintando Parede

Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área de 2 m².
"""
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
tinta = area / 2
print('Sua parede tem as dimensões de {} x {} e sua área é de {} m².'.format(larg, alt, area))
print('Para pintar essa parede, você precisará de {} litros de tinta.'.format(tinta))
```


```
"""
EXERCÍCIO 012: Calculando Descontos

Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""
preco = float(input('Qual é o preço do produto? R$ '))
novo = preco - (preco * 5 / 100)
print('O produto que custava R$ {:.2f}, na promoção com desconto de 5% vai custar R$ {:.2f}.'.format(preco, novo))
```


```
"""
EXERCÍCIO 013: Reajuste Salarial

Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""
salario = float(input('Qual é o salário do funcionário? R$ '))
novo = salario + (salario * 15 / 100)
print('Um funcionário que ganhava R$ {:.2f}, com 15% de aumento, passa a receber R$ {:.2f}.'.format(salario, novo))
```


```
"""
EXERCÍCIO 014: Conversor de Temperaturas

Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.
"""
c = float(input('Informe a temperatura em ºC: '))
f = 9 * c / 5 + 32
print('A temperatura de {}ºC corresponde a {}ºF!'.format(c, f))
```


```
"""
EXERCÍCIO 015: Aluguel de Carros

Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
"""
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R$ {:.2f}!'.format(pago))
```


```
"""
EXERCÍCIO 016: Quebrando um Número

Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

Ex:
Digite um número: 6.127
O número 6.127 tem a parte inteira 6.
"""

"""
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}!'.format(num, trunc(num)))
"""

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}!'.format(num, int(num)))
```


```
"""
EXERCÍCIO 017: Catetos e Hipotenusa

Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
"""

"""
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1 / 2)
print('A hipotenusa vai medir {:.2f}!'.format(hi))
"""

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}!'.format(hi))
```


```
"""
EXERCÍCIO 018: Seno, Cosseno e Tangente

Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""
from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}!'.format(angulo, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}!'.format(angulo, cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}!'.format(angulo, tangente))
```


```
"""
EXERCÍCIO 019: Sorteando um Item na Lista

Um professor quer sortear um dos seus quatros alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
"""
from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}!'.format(escolhido))
```


```
"""
EXERCÍCIO 020: Sorteando uma Ordem na Lista

O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será:')
print(lista)
```


```
"""
EXERCÍCIO 021: Tocando um MP3

Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
"""

"""
import pygame
pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
pygame.event.wait()
"""

from pygame import mixer
from time import sleep
mixer.init()
mixer.music.load('musica.mp3')
mixer.music.play()
sleep(120)
```


```
"""
EXERCÍCIO 022: Analisador de Textos

Crie um programa que leia o nome completo de uma pessoa e mostre:

> O nome com todas as letras maiúsculas e minúsculas.
> Quantas letras ao todo (sem considerar espaços).
> Quantas letras tem o primeiro nome.
"""
nome = str(input('Digite seu nome completo: ')).strip()
separa = nome.split()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em minúsculas {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
# print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
```


```
"""
EXERCÍCIO 023: Separando Dígitos de um Número

Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

Ex:
Digite um número: 1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1
"""
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}...'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
```


```
"""
EXERCÍCIO 024: Verificando as Primeiras Letras de um Texto

Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
"""
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
```


```
"""
EXERCÍCIO 025: Procurando uma String Dentro de Outra

Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""
nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
```


```
"""
EXERCÍCIO 026: Primeira e Última Ocorrência de uma String

Faça um programa que leia uma frase pelo teclado e mostre:

> Quantas vezes aparece a letra "A".
> Em que posição ela aparece a primeira vez.
> Em que posição ela aparece a última vez.
"""
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A') + 1))
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A') + 1))
```


```
"""
EXERCÍCIO 027: Primeiro e Último Nome de uma Pessoa

Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.

Ex: Ana Maria de Souza
Primeiro = Ana
Último = Souza
"""
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}.'.format(nome[0]))
print('Seu último nome é {}.'.format(nome[len(nome) - 1]))
```

```
"""
EXERCÍCIO 028: Jogo da Adivinhação v1.0

Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import randint
from time import sleep
computador = randint(0, 5)  # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))  # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
```


```
"""
EXERCÍCIO 029: Radar Eletrônico

Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma
mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.
"""
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80 Km/h!')
    multa = (velocidade - 80) * 7
    print('Você deve pagar um multa de R$ {:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
```


```
"""
EXERCÍCIO 030: Par ou Ímpar?

Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""
numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é PAR!'.format(numero))
else:
    print('O número {} é IMPAR!'.format(numero))
```


```
"""
EXERCÍCIO 031: Custo da Viagem

Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.
"""

"""
distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a fazer uma viagem de {} Km.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preço da sua passagem será de R$ {:.2f}.'.format(preco))
"""

distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a fazer uma viagem de {} Km.'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R$ {:.2f}.'.format(preco))
```


```
"""
EXERCÍCIO 032: Ano Bissexto

Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
"""
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO!'.format(ano))
```


```
"""
EXERCÍCIO 033: Maior e Menor Valores

Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando qual é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando qual é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))
```


```
"""
EXERCÍCIO 034: Aumentos Múltiplos

Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para inferiores ou iguais, o aumento é de 15%.
"""
salario = float(input('Qual é o salário do funcionário? R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora.'.format(salario, novo))
```


```
"""
EXERCÍCIO 035: Analisando Triângulo v1.0

Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
"""
print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
```
