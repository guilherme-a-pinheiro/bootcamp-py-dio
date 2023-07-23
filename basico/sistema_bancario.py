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

while True:
    opcao_escolhida = input(menu)

    if opcao_escolhida == 'd':
        valor = float(input("Informe o valor para depósito: "))
        if valor <= 0:
            print('Operação cancelada - Valor inválido')
        else:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Valor de R$ {valor:.2f}\n depositado com sucesso")
            print(f"Seu saldo atual é de R$ {saldo:.2f}\n")

    elif opcao_escolhida == 's':
        valor = float(input("Informe o valor para saque: "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite_valor = valor > limite

        excedeu_limite_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Saldo insuficiente!")

        elif excedeu_limite_valor:
            print("Valor limite por operação excedido!")

        elif excedeu_limite_saques:
            print("Quantidade limite de saques excedida!")

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
        else: print("Valor inválido!")
    
    elif opcao_escolhida == 'e':
        if extrato == "":
            print("Não foram realizadas movimentações na conta")
        else:
            print(f'Extrato: {extrato}')
            print(f'Saldo = R$ {saldo:.2f}\n')

    elif opcao_escolhida == 'q':
        break
