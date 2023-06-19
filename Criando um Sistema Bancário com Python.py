menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Qual valor deseja depositar?"))
        saldo += deposito
    
    elif opcao == "2":
        if(numero_saques <  LIMITE_SAQUES):
            if(saldo == 0):
                print("Não será possível sacar o dinheiro por falta de saldo")
            else:
                saque = float(input("Qual valor deseja sacar?"))
                if(saque > 500):
                    print("Valor acima do limite diário de saque (500R$)")
                    saque = float(input("Qual valor deseja sacar?"))

                saldo -= saque
                numero_saques += 1
                print("Obrigado por utilizar nossos serviços")
        else:
            print("Obrigado por utilizar nossos serviços, seu limite de saque diário foi atingido")
    
    elif opcao == "3":
        print("Extrato: {:.2f}".format(saldo))
    
    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")