menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        print('Valor depositado com sucesso!')
        extrato += f'Depósito R$ {valor:.2f}\n'
    
    return saldo, extrato

def sacar(valor, saldo, limite, numero_saques, limite_saques, extrato):
    if valor > saldo:
        print("Saldo insuficiente!")
    
    elif valor > limite:
        print("Valor limite por operação excedido!")

    elif numero_saques >= limite_saques:
        print("Quantidade limite de saques excedida!")

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque R$ {valor:.2f}\n'
        numero_saques += 1
        print("Valor sacado com sucesso!")
    else:
        print("Valor inválido!")

    return saldo, extrato

def verificar_extrato(extrato):
    if extrato == "":
        print("Não foram realizadas movimentações na conta")
    else:
        print(f'Extrato: {extrato}')

while True:
    print("<------------- Atendimento iniciado ------------->")
    opcao_escolhida = input(menu)

    if opcao_escolhida == 'd':
        valor = float(input("Informe o valor para depósito: "))
        saldo, extrato = depositar(valor, saldo, extrato)

    elif opcao_escolhida == 's':
        valor = float(input("Informe o valor para saque: "))
        saldo, extrato =  sacar(
            valor=valor,
            saldo=saldo,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=limite_saques,
            extrato=extrato)
        
    elif opcao_escolhida == 'e':
        extrato = verificar_extrato(extrato)

    elif opcao_escolhida == 'q':
        break