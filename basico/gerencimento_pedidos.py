def main():
    n = int(input())

 
    total = 0
 
    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor
    
    porcentagem_desconto = input()
    desconto_separado = porcentagem_desconto.split("%")
    valor_desconto = int(desconto_separado[0])

    valor_total = total - (total * (valor_desconto / 100))

    print(f"Valor total: {valor_total:.2f}")
 
 
 
main()