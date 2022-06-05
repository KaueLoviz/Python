##############################################################################
# Exercícios Aula 3 - Slide
# Nome: Kauê Loviz de Oliveira
# Faculdade: Universidade Cruzeiro do Sul
# Data: 19/04/2022
# Site: https://github.com/KaueLoviz
##############################################################################
print("")
print("Exercício 3 - Idade \n")

data = int(input("Digite a data do seu nascimento: "))
mes = int(input("Digite o mês do seu nascimento: "))
ano = int(input("Digite o ano do seu nascimento: "))

data2 = int(input("\nDigite a data atual: "))
mes2 = int(input("Digite o mês atual: "))
ano2 = int(input("Digite o ano atual: "))

idadeAnos = ano2 - ano

if mes >= mes2:
    if mes == mes2:
        if data > data2:
            idadeAnos - 1
    else:
        idadeAnos - 1

diasPassados =  (30 - data) + ((12 - mes)*30) + ((mes2 - 1)*30) + data2 + (idadeAnos)*365
print("")
print("Você viveu",diasPassados,"dias.")
print("")
print("Fim do programa")