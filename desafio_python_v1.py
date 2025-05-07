## Desafio: Criando um Sistema Bancário com Python
from colorama import Fore, Style, init
init(autoreset=True) # Initialize colorama

## Função para depósito ##
def depositar(*,valor, saldo, extrato):

    if valor > 0:
        saldo += valor
        extrato += Fore.BLUE + f"Depósito\tR${valor:.2f}\n"
        print("\n Depósito realizado com sucesso")
    
    else:
        print("Operação falhou! O valor informado é inválido")

    return saldo, extrato



## Função para saque ##
def saque(*,valor, saldo, extrato, limite, numero_de_saques, limite_de_saques):
    
    if valor > saldo:
        print("Você não tem saldo suficiente para realizar esse saque.")
    
    elif valor > limite:
        print("A operação falhou! O valor de saque excede o limite.")

    elif numero_de_saques >= limite_de_saques:
        print("A operação falhou! Número de saques excedido")

    elif valor > 0:
        saldo -= valor
        extrato += Fore.RED +f"Saque\t \tR${valor:.2f}\n"
        numero_de_saques += 1
        print("Saque realizado com sucesso")

    else:
        print("A operação falhou! O valor informado é invalido")

    return saldo, extrato, numero_de_saques


## Função para Extrato ##
def exibir_extrato(saldo,/,*, extrato):
    if not extrato:
        print("Não foram realizadas movimentações")
    else:
        print(f"{extrato} \n")
        print(f"Saldo: R${saldo:.2f}")
    return saldo, extrato


menu = """
===== ESCOLHA A OPERAÇÃO =====

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair

"""

saldo = 0 
valor_limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES =3    


while True:
    
    opcao = input(menu)

    if opcao == "1":
        print("==== Depósito ====")
        valor = float(input("Digite o valor a ser depositado: R$"))
        saldo, extrato = depositar(valor = valor, saldo = saldo, extrato=extrato)

    elif opcao == "2":
        print("==== Saque ====")
        valor = float(input("Digite o valor a ser sacado: R$"))
        saldo, extrato, numero_saques = saque(valor = valor, saldo = saldo, extrato =extrato, limite = valor_limite_saque, numero_de_saques=numero_saques, limite_de_saques=LIMITE_SAQUES)

    elif opcao == "3":
        print("==== Extrato ====")
        exibir_extrato(saldo, extrato=extrato)
        print("=================")
        

    elif opcao == "4":
        break

    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")