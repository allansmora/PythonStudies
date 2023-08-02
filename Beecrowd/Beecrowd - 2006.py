'''
beecrowd | 2006
Identificando o Chá
'''

t = input()
a,b,c,d,e = input().split(" ")
contador = 0
if a == t:
    contador+=1
if b == t:
    contador+=1
if c == t:
    contador+=1
if d == t:
    contador+=1
if e == t:
    contador+=1
print(contador)