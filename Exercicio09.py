#FUP para ler três valores quaisquer e escrever o maior dos 3.
valor1 = int(input('Digite um número:'))
valor2 = int(input('Digite outro número:'))
valor3 = int(input('Digite mais um número:'))
maior = valor1
if (valor2 > maior):
    maior = valor2
if (valor3 > maior):
    maior = valor3
print(f' O número maior é: {maior}')