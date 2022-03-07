print("")
print("Exercício 6 - Parede Retangular\n")

larguraP = float(input("Digite a largura da parede retangular: "))
alturaP = float(input("Digite a altura da parede retangular: "))
larguraA = float(input("Digite a largura do azulejo retangular: "))
alturaA = float(input("Digite a altura do azulejo retangular: "))

print("")

areaP = (larguraP * alturaP)
areaA = (larguraA * alturaA)
qtdAzulejo = areaP / areaA

print("Será necessário um total de:",format(qtdAzulejo, ".1f"),"azulejos")
print("")
print("Fim do programa")