##############################################################################
# Exercícios Aula 5 - Slide
# Nome: Kauê Loviz de Oliveira
# Faculdade: Universidade Cruzeiro do Sul
# Data: 26/04/2022
# Site: https://github.com/KaueLoviz
##############################################################################

print("\nExercício 3 - Comerciante\n")

nomeProduto = str(input("Digite o nome do produto: "))
valorCompra = float(input("Digite o valor da compra: "))

if(valorCompra < 10):
    valorVenda = valorCompra + (valorCompra * 70 / 100)
    print("O produto",nomeProduto,"foi comprado por R$",valorCompra,"e o Valor da Venda com LUCRO de 70% foi de: R$",valorVenda)
    print("\nFim do programa")
else:
    if(valorCompra <= 10 and valorCompra < 30):
        valorVenda = valorCompra + (valorCompra * 50 / 100)
        print("O produto",nomeProduto,"foi comprado por R$",valorCompra,"e o Valor da Venda com LUCRO de 50% foi de: R$",valorVenda)
        print("\nFim do programa")
    else:
        if(valorCompra <= 30 and valorCompra < 50):
            valorVenda = valorCompra + (valorCompra * 40 / 100)
            print("O produto",nomeProduto,"foi comprado por R$",valorCompra,"e o Valor da Venda com LUCRO de 40% foi de: R$",valorVenda)
            print("\nFim do programa")
        else:
            if(valorCompra >= 50):
                valorVenda = valorCompra + (valorCompra * 30 / 100)
                print("O produto",nomeProduto,"foi comprado por R$",valorCompra,"e o Valor da Venda com LUCRO de 30% foi de: R$",valorVenda)
                print("\nFim do programa")
            