'''
beecrowd | 1020
Idade em Dias
'''

idade = int(input())
idade_anos = idade//365
idade_meses = (idade%365)//30
idade_dias = (idade%365)%30

print(f"{idade_anos} ano(s)")
print(f"{idade_meses} mes(es)")
print(f"{idade_dias} dia(s)")