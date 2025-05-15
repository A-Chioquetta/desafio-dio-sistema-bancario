## Desafio: Criando um Sistema Bancário com Python
from colorama import Fore, Style, init
from datetime import datetime, time, timezone, timedelta
import textwrap
init(autoreset=True) # Initialize colorama

   
def menu():
    menu = """
    ======== MENU ========

    [D]\tDepositar
    [S]\tSacar
    [E]\tExtrato
    [NU]\tNovo usuário
    [NC]\tNova conta
    [LC]\tListar contas
    [Q]\tSair

    """
    return input(textwrap.dedent(menu)).upper()


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
        print(textwrap.dedent(f"{extrato} \n"))
        print(textwrap.dedent(f"Saldo: R${saldo:.2f}"))
    return saldo, extrato


## Função para criar novo usuário ##
def criar_usuario(*, usuarios):
    cpf = input("Informe o CPF (somente números):")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print(Fore.RED + "\n Usuário já cadastrado!")
        return 
    else:    
        nome = input("Informe nome completo: ")
        data_de_nascimento = input("Informa  data de nascimento (dd-mm-aa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estadoo): ")
        usuarios.append({"nome": nome, "data_de_nascimento": data_de_nascimento, "cpf": cpf, "endereco": endereco, "lista_de_contas": None})
        print(Fore.GREEN + "\n Novo usuário registrado com sucesso! \n ")
        print(f" Nome: {nome} \n Data de nascimento: {data_de_nascimento} \n CPF: {cpf} \n Endereço: {endereco}")  
        return usuarios


## Função para criar conta corrente ##
def criar_conta_corrente(*,agencia, usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        numero_da_conta = len(contas)+1
        contas.append({"agencia": agencia, "numero_da_conta": numero_da_conta, "usuario": usuario})
        
        print("Nova conta criada com sucesso!")
        print(f" Dados: \n Agencia: {agencia} \n Número da conta: {numero_da_conta} \n Nome: {usuario["nome"]} \n CPF: {usuario["cpf"]}")
    else:
        print(Fore.RED + "Usuário não encontrado, fluxo de criação de conta encerrado!")


    return contas


## Função para criar usuário ##
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
        

## Função para listar todas as contas ##        
def listar_contas(contas):
    for usuario in contas:
        print(f"Agência: {usuario["agencia"]} \n C/C: {usuario["numero_da_conta"]}\n Titular: {usuario["usuario"]["nome"]} \n")





saldo = 0 
valor_limite_saque = 500
extrato = ""
numero_saques = 0
numero_transacao = 0
ultimo_dia = datetime.now().date()
usuarios = []
contas = []
numero_da_conta = 0
LIMITE_TRANSACAO = 10
LIMITE_SAQUES =3  
AGENCIA = "0001"  


while True:
    opcao = menu()

    agora = datetime.now()
    if agora.date() != ultimo_dia:
        numero_transacao = 0
        numero_saques = 0
        ultimo_dia = agora.date()
    
    
    

    if opcao == "D":
        print("==== Depósito ====")
        cpf = input("Digite o CPF:")
        valor = float(input("Digite o valor a ser depositado: R$"))
        saldo, extrato, numero_transacao = depositar(valor = valor, saldo = saldo, extrato=extrato, numero_transacao=numero_transacao, limite_transacao=LIMITE_TRANSACAO)

    elif opcao == "S":
        print("==== Saque ====")
        valor = float(input("Digite o valor a ser sacado: R$"))
        saldo, extrato, numero_saques, numero_transacao = saque(valor = valor, saldo = saldo, extrato =extrato, 
                                              limite = valor_limite_saque, numero_de_saques=numero_saques, limite_de_saques=LIMITE_SAQUES, 
                                              numero_transacao=numero_transacao, limite_transacao=LIMITE_TRANSACAO )

    elif opcao == "E":
        print("==== Extrato ====")
        exibir_extrato(saldo, extrato=extrato)
        print("=================")
        

    elif opcao == "NU":
        print("=== Criar novo usuário ===")
        criar_usuario(usuarios=usuarios)

    elif opcao == "NC":
        print("=== Criar nova conta ===")
        criar_conta_corrente(agencia = AGENCIA, usuarios=usuarios)

    elif opcao == "LC":
        print("=== Lista de contas === \n")
        listar_contas(contas)


    elif opcao == "Q":
        break

    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")