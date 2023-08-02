'''
beecrowd | 1017
Gasto de Combustível
'''

tempo_gasto = int(input())
velocidade_media = int(input())
distancia_dirigida = velocidade_media*tempo_gasto
litragem = distancia_dirigida/12

print(f"{litragem:.3f}")