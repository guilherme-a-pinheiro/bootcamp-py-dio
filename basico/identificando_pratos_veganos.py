numPedidos = int(input())

numPedido = 1

for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    vegano = input()
    ehVegano = False

    if vegano == 's':
        ehVegano = True

    if ehVegano:
        print(f"Pedido {numPedido}: {prato} (Vegano) - {calorias} calorias")
    else:
        print(f"Pedido {numPedido}: {prato} (Nao-vegano) - {calorias} calorias")
    numPedido += 1