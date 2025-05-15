## Desafio: Criando um Sistema Bancário com Python
from colorama import Fore, Style, init
from datetime import datetime, time, timezone, timedelta
import pytz
init(autoreset=True) # Initialize colorama

## Função para depósito ##
def depositar(*,valor, saldo, extrato, numero_transacao, limite_transacao):
    if numero_transacao > limite_transacao:
        print("Operação falhou! Número limite de transações diária atingida.")
    else:
        if valor > 0:
            saldo += valor
            time = datetime.now().strftime("%d/%m/%Y %H:%M")
            extrato += Fore.BLUE + f"Depósito\tR${valor:.2f} \t {time}\n \n"
            numero_transacao += 1
            print("\n Depósito realizado com sucesso")
    
        else:
            print("Operação falhou! O valor informado é inválido")

    return saldo, extrato, numero_transacao



## Função para saque ##
def saque(*,valor, saldo, extrato, limite, numero_de_saques, limite_de_saques, numero_transacao, limite_transacao):
    if numero_transacao > limite_transacao:
        print("Operação falhou! Número limite de transações diária atingida.")
    else:    
        if valor > saldo:
            print("Você não tem saldo suficiente para realizar esse saque.")
        
        elif valor > limite:
            print("A operação falhou! O valor de saque excede o limite.")

        elif numero_de_saques >= limite_de_saques:
            print("A operação falhou! Número de saques excedido")

        elif valor > 0:
            saldo -= valor
            time = datetime.now().strftime("%d/%m/%Y %H:%M")
            extrato += Fore.RED +f"Saque\t \tR${valor:.2f} \t {time}\n \n"
            numero_de_saques += 1
            numero_transacao += 1
            print("Saque realizado com sucesso")

        else:
            print("A operação falhou! O valor informado é invalido")

    return saldo, extrato, numero_de_saques, numero_transacao


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
numero_transacao = 0
LIMITE_TRANSACAO = 10
LIMITE_SAQUES =3    
ultimo_dia = datetime.now().date()

while True:
    
    agora = datetime.now()
    print(agora)
    if agora.date() != ultimo_dia:
        numero_transacao = 0
        numero_saques = 0
        ultimo_dia = agora.date()
    
    opcao = input(menu)
    
    
    

    if opcao == "1":
        print("==== Depósito ====")
        valor = float(input("Digite o valor a ser depositado: R$"))
        saldo, extrato, numero_transacao = depositar(valor = valor, saldo = saldo, extrato=extrato, numero_transacao=numero_transacao, limite_transacao=LIMITE_TRANSACAO)

    elif opcao == "2":
        print("==== Saque ====")
        valor = float(input("Digite o valor a ser sacado: R$"))
        saldo, extrato, numero_saques, numero_transacao = saque(valor = valor, saldo = saldo, extrato =extrato, 
                                              limite = valor_limite_saque, numero_de_saques=numero_saques, limite_de_saques=LIMITE_SAQUES, 
                                              numero_transacao=numero_transacao, limite_transacao=LIMITE_TRANSACAO )

    elif opcao == "3":
        print("==== Extrato ====")
        exibir_extrato(saldo, extrato=extrato)
        print("=================")
        

    elif opcao == "4":
        break

    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")