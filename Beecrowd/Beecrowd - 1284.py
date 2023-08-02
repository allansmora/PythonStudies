'''
beecrowd | 1284
Digitando no Telefone Celular
'''
palavras = []
lista_apoio = []
contador_palavra_unica = 0
n = int(input())
for i in range(n):
    palavra = input()
    palavras.append(palavra)
palavras.sort()
lista_apoio = palavras
lista_teste = ["testte","saco","bola","cu","caceta"]
print(lista_teste[1][1])
#Descobrir se existe palavra com apenas 1 letra
for i in range(len(palavras),1):
    if(palavras[i][i] != lista_apoio[i][i]):
        contador_palavra_unica +=1
print(contador_palavra_unica)
print(palavras[0][0])
print(lista_apoio[0][0])
print(palavras)