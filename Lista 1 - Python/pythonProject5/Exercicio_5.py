print("")
print("Exercício 5 - Parede Quadrada\n")

larguraP = float(input("Digite a largura da parede quadrada: "))
larguraA = float(input("Digite a largura do azulejo quadrado: "))

print("")

areaP = (larguraP * larguraP)
areaA = (larguraA * larguraA)
qtdAzulejo = areaP / areaA

print("Será necessário um total de:",format(qtdAzulejo, ".1f"),"azulejos")
print("")
print("Fim do programa")
