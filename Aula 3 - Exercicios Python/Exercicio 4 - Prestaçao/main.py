##############################################################################
# Exercícios Aula 3 - Slide
# Nome: Kauê Loviz de Oliveira
# Faculdade: Universidade Cruzeiro do Sul
# Data: 19/04/2022
# Site: https://github.com/KaueLoviz
##############################################################################
print("")
print("Exercício 4 - Prestação \n")

valorPrestacao = int(input("Digite o valor da Prestação: "))
multa = int(input("Digite a porcentagem de multa pelo atraso: "))
qntDias = int(input("Digite a quantidade de dias de atraso: "))

prestacao =  valorPrestacao + (valorPrestacao*(multa/100)*qntDias)

print("O valor da prestação atualizada é: R$",format(prestacao,".1f"))
print("")
print("Fim do programa")