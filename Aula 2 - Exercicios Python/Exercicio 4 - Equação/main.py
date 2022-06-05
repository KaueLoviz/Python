##############################################################################
# Exercícios Aula 2 - Slide
# Nome: Kauê Loviz de Oliveira
# Faculdade: Universidade Cruzeiro do Sul
# Data: 16/04/2022
# Site: https://github.com/KaueLoviz
##############################################################################
print("")
print("Exercício 4 - Equação \n")

# ax^2+bx+c = 0
a = int(input("Digite o valor do Coeficiente a: "))
print("")
b = int(input("Digite o valor do Coeficiente b: "))
print("")
c = int(input("Digite o valor do Coeficiente c: "))
print("")

#delta = b^2 - 4ac
delta = b**2 - 4*a*c
print("O valor de delta é: ", delta)
print("")

# x = (-b +- raiz(delta))/2a
x1 = (-b + delta**0.5) / (2*a)
x2 = (-b - delta**0.5) / (2*a)
print("O valor de x1 é: ", x1)
print("")
print("O valor de x2 é: ", x2)
print("")
print("Fim do programa")