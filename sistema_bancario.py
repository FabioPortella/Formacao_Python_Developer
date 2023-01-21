import textwrap

saldo = 0
numero_saques = 0
extrato = ""

LIMITE_VALOR_SAQUE = 500.00
LIMITE_QUANTIDADE_SAQUES = 3


def menu(): 

    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    return input(textwrap.dedent(menu))


def depositar(valor, saldo, extrato):

    if valor > 0:
        saldo += valor
        extrato += f"     Depósito: R$ {valor:8.2f} +\n"
    else:
        print(f"Operação falhou! O valor <{valor}> é inválido")

    return saldo, extrato


def sacar(valor, saldo, numero_saques, extrato, LIMITE_VALOR_SAQUE):

    if valor <= saldo and valor <= LIMITE_VALOR_SAQUE:
        numero_saques += 1
        saldo -= valor
        extrato += f"     Saque...: R$ {valor_saque:8.2f} -\n"
    else:
        if valor > saldo: 
            print(f"Saldo insuficiente")
        elif valor > LIMITE_VALOR_SAQUE:
            print(f"Você não pode sacar um valor que excede R$ {LIMITE_VALOR_SAQUE:.2f}")
        else:
            print(f"Operação falhou! O valor informado não é válido")

    return saldo, numero_saques, extrato


def exibir_extrato(extrato):

    print("\n============ EXTRATO =============\n")
    print(extrato)
    print(f"     Saldo  => R$ {saldo:8.2f}\n")
    print("==================================")
    print(f"OBS: Foram feitos {numero_saques} saques hoje.")


while True:
    
    opcao = menu()

    if opcao == 'd':
        try:
            valor_deposito = float(input("Informe o valor do depósito: "))
        except ValueError: 
            print(f"Operação falhou! O valor informado não é válido")
        else:
            saldo, extrato = depositar(valor_deposito, saldo, extrato)

    elif opcao == 's':
        if numero_saques == LIMITE_QUANTIDADE_SAQUES:
            print(f"Você temo limite de <{LIMITE_QUANTIDADE_SAQUES}> saques diários.")
        else:
            try:
                valor_saque = float(input("Informe o valor do saque: "))
            except ValueError: 
                print(f"Operação falhou! O valor informado não é válido")
            else:
                saldo, numero_saques, extrato = sacar(valor_saque, saldo, numero_saques, extrato, LIMITE_VALOR_SAQUE)

    elif opcao == 'e':
            exibir_extrato(extrato)

    elif opcao == 'q':
        break

    else:
        print(f"Operação <{opcao}> inválida, por favor selecione novamente a operação desejada")