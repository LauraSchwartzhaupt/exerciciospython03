#FUP para ler dois valores numéricos e apresentar a diferença do maior pelo menor.
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
if n1 > n2:
    diferenca = n1 - n2
    print (f' A diferença de {n1} para {n2} é:{diferenca}')
if n2 > n1:
    diferenca = n2 - n1
    print (f' A diferença de {n2} para {n1} é:{diferenca}')
