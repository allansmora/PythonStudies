'''
beecrowd | 3048
Sequência Secreta
'''

n = int(input())
lista = []
contador = 0
for i in range(n):
    lista.append(int(input()))
for i in range(1,len(lista)):
    if(lista[i] == lista[i-1]):
        contador+=1
print(len(lista) - contador)