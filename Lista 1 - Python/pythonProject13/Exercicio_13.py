print("")
print("Exercício 13 - Estoque\n")

totalEstoque = int(input("Digite o Total de um objeto no Estoque: "))
totalVendas  = int(input("Digite o Total de Vendas desse objeto: "))

print("")

percentualObVe = totalVendas * 100 / totalEstoque

print("Foram realizada(s) a(s) venda(s) de:", format(percentualObVe, ".1f"),"objeto(s)")
print("")
print("Fim do programa")