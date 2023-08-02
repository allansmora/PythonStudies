
'''
beecrowd | 1019
Conversão de Tempo
'''

n = int(input())

horas = n//3600
minutos = (n/3600 - horas)*60
segundos = (minutos - int(minutos)) * 60
minutos = int(round(minutos,7))
segundos = int(round(segundos,7))
print(f"{horas}:{minutos}:{segundos}")

