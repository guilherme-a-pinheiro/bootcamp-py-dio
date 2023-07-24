menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo usuário
    [nc] Nova conta
    [lc] Listar contas
    [q] Sair
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3
usuarios = []
contas = []
agencia = "0001"

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

def cadastrar_usuario(cpf, usuarios):
    usuario = verificar_usuario_existente(cpf, usuarios)

    if usuario:
        print("Usuário existente!")
        return
    
    nome = input("Informe o nome: ")
    data_nascimento = input("Informe a data de nascimento (dia-mes-ano): ")
    endereco = input("Informe o endereço completo (rua/avenida, número - bairro - cidade - sigla): ")

    usuarios.append({
        "nome": nome,
        "CPF": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    })

    print("Usuário cadastrado com sucesso!")

def verificar_usuario_existente(cpf, usuarios):
    check_usuario = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return check_usuario[0] if check_usuario else None


def cadastrar_conta(agencia, contas, usuarios):
    cpf = input("Informe o CPF: ")

    numero_conta = len(contas) + 1

    usuario = verificar_usuario_existente(cpf, usuarios)

    if usuario:
        contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
        print("Conta cadastrada com sucesso!")
    else:
        print("Usuário não encontrado!")

def listar_contas(contas):
    if contas == []:
        for conta in contas:
            print(f"""
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
            """)
    else:
        print("Sem contas cadastradas!")

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

    elif opcao_escolhida == 'nu':
        cpf = input("Informe o CPF para cadastro: ")
        usuarios = cadastrar_usuario(cpf, usuarios)

    elif opcao_escolhida == 'nc':
        contas = cadastrar_conta(agencia, contas, usuarios)

    elif opcao_escolhida == 'lc':
        contas = listar_contas(contas)