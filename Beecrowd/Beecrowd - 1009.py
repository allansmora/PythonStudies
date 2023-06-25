'''
beecrowd | 1009
Salário com Bônus
'''

nome = input()
salario = float(input())
vendas = float(input())

salario_final = salario + (vendas *0.15)

print(f"TOTAL = R$ {salario_final:.2f}")