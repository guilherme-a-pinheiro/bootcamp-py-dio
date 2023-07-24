# valorHamburguer = float(input())
# quantidadeHamburguer = int(input())
# valorBebida = float(input())
# quantidadeBebida = int(input())
# valorPago = float(input())

# valorTotalHamburguers = valorHamburguer * quantidadeHamburguer
# valorTotalBebidas = valorBebida * quantidadeBebida
# totalPedido = valorTotalBebidas + valorTotalHamburguers

# if valorPago - totalPedido > 0:
#     troco = valorPago - totalPedido
# else:
#     troco = 0

# print(f"O preço final do pedido é R$ {totalPedido:.2f}. Seu troco é R${troco:.2f}")

teste = "O preço final do pedido é R$ 24.00. Seu troco é R$ 26.00."
teste2 = "O preço final do pedido é R$ 24.00. Seu troco é R$26.00."

print(teste == teste2)