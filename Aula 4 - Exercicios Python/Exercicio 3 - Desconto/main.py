##############################################################################
# Exercícios Aula 4 - Slide
# Nome: Kauê Loviz de Oliveira
# Faculdade: Universidade Cruzeiro do Sul
# Data: 26/04/2022
# Site: https://github.com/KaueLoviz
##############################################################################

print("\nExercício 3 - Desconto\n")

valor = float(input("Digite o valor da compra: "))

if(valor > 200):
    precoDesconto = valor - (valor * 20 / 100)
    print("O valor da compra COM o desconto de 20% é: R$",format(precoDesconto,".2f"))
    print("Fim do programa")
else:
    if(valor <= 200):
        valor = valor
        print("O valor da compra SEM o desconto de 20% é: R$",format(valor,".2f"))
        print("Fim do programa")