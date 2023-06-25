'''
beecrowd | 1279
Ano Bissexto ou Ano não Bissexto
'''
def verificarBissexto(ano):
  if((ano%400 == 0) or (ano%100 != 0 and ano%4 == 0)):
    return True
  else:
    return False
pula = 0
while True:
  try:
    if pula:
      print('')
    pula = 1
    ano = int(input())
    validador = 0
    if(verificarBissexto(ano)):
      validador+=4
    if(ano%15 == 0):
      validador+=15
    if(ano%55 == 0 and verificarBissexto(ano)):
      validador+=55
    if(validador == 4):
      print('This is leap year.')
    elif(validador == 19):
      print('This is leap year.')
      print('This is huluculu festival year.')
    elif(validador == 15):
      print('This is huluculu festival year.')  
    elif(validador == 74):
      print('This is leap year.')
      print('This is huluculu festival year.')
      print('This is bulukulu festival year.')
    elif(validador == 59):
      print('This is leap year.')
      print('This is bulukulu festival year.')  
    else:
      print('This is an ordinary year.')
  except EOFError:
    break