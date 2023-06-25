'''
beecrowd | 1120
Revisão de Contrato
'''
digito_problema = 1
numero = 1
while(digito_problema != 0 and numero != 0):
    digito_problema, numero = input().split(" ")
    numero = int(numero)
    auxiliar_split  = []
    auxiliar_split = [x for x in str(numero)]
    for i in range(len(auxiliar_split)):
        if(auxiliar_split[i] == str(digito_problema)):
            auxiliar_split.pop(i)
    auxiliar_split = ''.join(auxiliar_split)
    numero_final = auxiliar_split
    print(int(numero_final))