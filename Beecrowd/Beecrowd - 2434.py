'''
beecrowd | 2434
Saldo do Vovô
'''
numero_dias,saldo_conta = input().split(" ")
numero_dias = int(numero_dias)
saldo_conta = int(saldo_conta)
valores_conta = []

for i in range(numero_dias):
    movimentacao = int(input())
    saldo_conta += movimentacao
    valores_conta.append(saldo_conta)
print(min(valores_conta))