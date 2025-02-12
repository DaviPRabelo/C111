MouF = ''

while MouF != 'm' and MouF != 'f':
    MouF = input("Insira seu sexo (Masculino(m) ou Feminino(f)):  ")

    if MouF != 'm' and MouF !='f':
        print("Selecione um caracter valido (m ou f)")

if MouF == "m" :
    print("Você é Homem")
elif MouF == "f":
    print("Você é mulher")