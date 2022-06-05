##############################################################################
# Exercícios Aula 3 - Slide
# Nome: Kauê Loviz de Oliveira
# Faculdade: Universidade Cruzeiro do Sul
# Data: 19/04/2022
# Site: https://github.com/KaueLoviz
##############################################################################
print("")
print("Exercício 1 - Volume \n")

altura = float(input("Digite o valor da altura do tronco da pirâmide: "))
baseMenor = float(input("Digite o valor da Base Menor do tronco da pirâmide: "))
baseMaior = float(input("Digite o valor da Base Maior do tronco da pirâmide: "))

print("")

volume = altura/3*(baseMaior**2 + baseMenor**2 + (baseMaior**2 * baseMenor**2)**0.5)

print("")
print("O valor do volume do tronco da pirâmide é: ",format(volume,".1f"))
print("")
print("Fim do programa")