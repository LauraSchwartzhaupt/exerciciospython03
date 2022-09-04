#FUP para ler e escrever três números. Se o primeiro for positivo, imprimir sua raiz quadrada, caso contrário, imprimir o seu quadrado; 
# se o segundo número for maior que 10 e menor que 100, imprimir a mensagem: "NÚMERO ESTÁ ENTRE 10 E 100 - INTERVALO PERMITIDO";
#  se o terceiro número for menor que o segundo, calcular e escrever a diferença entre eles, caso contrário, calcular e escrever a soma entre eles. 
n1 = float(input('Digite um número:'))
n2 = float(input('Digite outro número:'))
n3 = float(input('Digite outro número:'))
if n1 > 0:
    raiz = float (n1) ** 0.5
    print (f'{raiz}')
else:
     quadrado: n1 * n1
     print (f'{raiz}')
if n2 > 10 and n2 < 100:
    print ('NÚMERO ESTÁ ENTRE 10 E 100 - INTERVALO PERMITIDO')    
if n3 < n2: 
    diferenca = n3 - n2 
    print (f' A diferença entre {n3} e {n2} é: {diferenca}')
else:
    soma = n3 + n2
    print (f' A Soma entre {n3} e {n2} é: {soma}')