print("Qual a ditancia de sua viagem?")
dist = float(input())

if dist <= 200:
    print("Valor da passagem: R$", dist*0.5)
elif dist >200:
    print("valor da passagem: R$", dist*0.45)
