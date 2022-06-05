print("\nExercício 4 - Idade\n")

idade = int(input("Digite a sua idade: "))
print("")
if idade <= 3:
    print("Você é um Bebê!")
elif idade <= 10:
    print("Você é Infantil!")
elif idade <= 14:
    print("Você é Júnior!")
elif idade <= 17:
    print("Você é Adolescente!")    
elif idade <= 30:
    print("Você é Jovem!")
else:
    print("Você é Adulto!")
    
