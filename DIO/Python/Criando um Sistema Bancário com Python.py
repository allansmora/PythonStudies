from random import randint

def sacar(saldo,extrato,limite,numero_saques,LIMITE_SAQUES):
    if(numero_saques <  LIMITE_SAQUES):
            if(saldo == 0):
                print("Não será possível sacar o dinheiro por falta de saldo")
            else:
                saque = float(input("Qual valor deseja sacar?"))
                if(saque > limite):
                    print("Valor acima do limite diário de saque (500R$)")
                    saque = float(input("Qual valor deseja sacar?"))

                saldo -= saque
                numero_saques += 1
                print("Obrigado por utilizar nossos serviços")
    else:
       print("Obrigado por utilizar nossos serviços, seu limite de saque diário foi atingido")
    return saldo,extrato
def depositar(saldo):
    deposito = float(input("Qual valor deseja depositar?"))
    saldo += deposito
    return saldo
def visualizarHistorico(saldo):
    print("Extrato: {:.2f}".format(saldo))
def validadorCPF(numero_cpf):
    numero_cpf = numero_cpf.replace("-","")
    numero_cpf = numero_cpf.replace(".","")
    return numero_cpf
def criarUsuario(lista_usuarios):
    usuario = {'nome':"",'cpf':0,'endereco':"",'data_nascimento':""}
    usuario['nome'] = input("Digite seu nome completo: ")
    numero_cpf = input("Digite seu CPF: ")
    usuario['cpf'] = validadorCPF(numero_cpf)
    usuario['endereco'] = input("Digite seu endereço completo: (Logradouro - bairro - Cidade/UF)")
    usuario['data_nascimento'] = input("Digite sua data de nascimento: (DD/MM/YYYY)")
    lista_usuarios.append(usuario)
    return lista_usuarios
def criarContaCorrente(lista_contas,lista_numeros_contas):
    conta_corrente = {'usuario':"",'numero_conta' :0,'numero_agencia':'0001'}
    print("Criação de conta inicializada...")
    conta_corrente["usuario"] = input("Digite seu nome completo: ")
    numero_conta = randint(1000,9999)
    for i in lista_numeros_contas:
        if i == numero_conta:
            numero_conta = randint(1000,9999)
        else:
            conta_corrente["numero_conta"] = numero_conta
            lista_numeros_contas.append(numero_conta)
    print(f"Conta criada com sucesso com os seguintes dados: {conta_corrente}")
    lista_contas.append(conta_corrente)
    return lista_contas

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
[CC] Criar Conta Corrrente
[UC] Criar Usuário

=> """
lista_numeros_contas = [0]
lista_contas = []
lista_usuarios = []
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        depositar(saldo)
    
    elif opcao == "2":
        sacar(saldo,extrato,limite,numero_saques,LIMITE_SAQUES)
    
    elif opcao == "3":
        visualizarHistorico(saldo)
    
    elif opcao == "4":
        break
    elif opcao == "CC":
        criarContaCorrente(lista_contas,lista_numeros_contas)
    elif opcao == "UC":   
        criarUsuario(lista_usuarios)
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")