#FUP que leia um número e mostre uma mensagem indicando se este número é par ou ímpar e se é positivo ou negativo.
n = int(input('Digite um número:'))
resultado = n % 2
if resultado == 0:
    print ('Este número é PAR')
if n > 0:
    print ('Este número é POSITIVO')
if n < 0:
    print ('Este número é NEGATIVO')
else:
    print ('Este número é ÍMPAR')
