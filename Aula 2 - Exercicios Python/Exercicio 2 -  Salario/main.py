##############################################################################
# Exercícios Aula 2 - Slide
# Nome: Kauê Loviz de Oliveira
# Faculdade: Universidade Cruzeiro do Sul
# Data: 14/04/2022
# Site: https://github.com/KaueLoviz
##############################################################################
print("")
print("Exercício 2 - Salário \n")

salarioAtual = int(input("Digite o seu salário atual: "))

print("")

salarioNovo = salarioAtual + ((salarioAtual*5)/100)
aumento = salarioNovo - salarioAtual

print("Aumento no salário de:",format(aumento,".0f"))
print("")
print("Seu salário atual com a comissao de 5% é: R$",format(salarioNovo,".1f"))
print("")
print("Fim do programa")