#FUP para ler dois valores: NUM1 e NUM2, e se NUM1 for maior que NUM2 executa a soma de NUM1 e NUM2; caso contrário, executa uma subtração.
num1 = int(input('Digite um número:'))
num2 = int(input('Digite outro número:'))
if num1 > num2: 
    soma = num1 + num2
    print (f' O resultado é: {soma}')
else:
    sub = num1 - num2
    print (f' O resultado é: {sub}')