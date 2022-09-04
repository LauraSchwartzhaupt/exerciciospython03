#FUP que leia o número da conta bancária e o saldo de um cliente. Caso a conta tenha saldo negativo,
#  o programa deve enviar a seguinte mensagem: CONTA ESTOURADA, caso contrário CONTA NORMAL.
conta = float(input('Digite o número da sua conta bancária:'))
saldo = float(input('Digite o saldo da sua conta bancária:'))
if saldo < 0:
    print ('CONTA ESTOURADA')
if saldo > 0:
    print ('CONTA NORMAL')