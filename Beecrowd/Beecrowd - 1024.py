'''
beecrowd | 1024
Criptografia
'''
def criptografar(texto):
    auxiliar_inverter = []
    texto = list(texto)
    for i in range(len(texto)):
        texto[i] = str(texto[i])
        if(isinstance(texto[i], str)):
            if((65 <= ord(texto[i]) <= 90) or (97 <= ord(texto[i]) <= 122)):
                texto[i] = chr(ord(texto[i]) + 3)
    for i in range(len(texto)):
        auxiliar_inverter.insert(0,texto[i])
    texto = auxiliar_inverter
    for i in range(((len(texto)//2)),len(texto)):
        texto[i] = chr(ord(texto[i]) - 1)
    print(''.join(texto))


numero_casos = int(input())
for i in range(numero_casos):
    texto_criptografar = input()
    criptografar(texto_criptografar)
