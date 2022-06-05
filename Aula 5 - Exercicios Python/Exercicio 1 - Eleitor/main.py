##############################################################################
# Exercícios Aula 5 - Slide
# Nome: Kauê Loviz de Oliveira
# Faculdade: Universidade Cruzeiro do Sul
# Data: 26/04/2022
# Site: https://github.com/KaueLoviz
##############################################################################

print("\nExercício 1 - Eleitor\n")

idade = int(input("Qual a sua idade? "))

print("Você tem ",idade,"anos\n")

if (idade < 16):
    print("Você NÃO é Eleitor!\n")
    print("Fim do programa")
elif (idade >=18 and idade <= 65):
    print("Você é Eleitor OBRIGATÓRIO a votar!\n")
    print("Fim do programa")
elif ((idade >= 16 and idade <= 18) or (idade > 65)):
    print("Você é Eleitor FACULTATIVO!\n")
    print("Fim do programa")