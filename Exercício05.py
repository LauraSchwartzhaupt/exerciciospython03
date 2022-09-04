#FUP para ler dois números. Se os números forem iguais, imprimir a mensagem: "NÚMEROS IGUAIS" e encerrar a execução; caso contrário, imprimir o de maior valor.
n1 = int(input('Digite um número:'))
n2 = int(input('Digite um número:'))
if n1 == n2:
    print ('NÚMEROS IGUAIS')
if n1 > n2:
    print (f' {n1}')
if n2 > n1:
    print (f' {n2}')
