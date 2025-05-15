# Desafio Dio: Criando um Sistema Bancário
Desafio proposto no BootCamp  **NTT DATA - Engenharia de Dados com Python** da plataforma [Dio](https://web.dio.me/).

**Abaixo segue a proposta do desafio.**


## Objetivo Geral
 Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato

## Desafio
Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

### Operação de depósito
Deve ser possível depositar valores positivos para a conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação extrato.

### Operação de saque
O sistema deve permitir realizar 3 saques diários com limite máximo de R$500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação extrato.

### Operação de extrato
Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:

1500.45 = R$ 1500.45


## Update do Desafio (v1.1)

Novas funcionalidades para o sistema:

- Estabelecer um limite de 10 transações diárias.

- Se o usuário tentar fazer uma transação após atingir o limite, deve ser informado que ele excedeu o número de transações permitidas para aquele dia.

- Mostrar no extrato, a data e hora de todas as transações.


## Update do Desafio (v2)

Novas funcionalidades para o sistema:

 - Criação de novos usuário

 - Criação de contas

 - Listagem de contas