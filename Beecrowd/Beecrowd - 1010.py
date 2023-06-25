'''
beecrowd | 1010
Cálculo Simples
'''

a1,b1,c1 = input().split(" ")
a2,b2,c2 = input().split(" ")
a1 = int(a1)
b1 = int(b1)
c1 = float(c1)
a2 = int(a2)
b2 = int(b2)
c2 = float(c2)

valor_final = (b1*c1) + (b2*c2)
print(f"VALOR A PAGAR: R$ {valor_final:.2f}") 