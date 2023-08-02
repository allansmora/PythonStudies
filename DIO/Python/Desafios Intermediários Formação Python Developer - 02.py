'''
Desafios Intermediários Formação Python Developer
2 / 3 - Aproveite a Oferta
'''
T = int(input())
garrafa_final = 0
for i in range(T):
    n,k = input().split(" ")
    n = int(n)
    k = int(k)

    garrafa_final = (n//k) +(n%k)
    print(garrafa_final)