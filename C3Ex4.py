pessoa1 = {'Nome': 'Roberto', 'Peso': 79}
pessoa2 = {'Nome': 'Julio', 'Peso': 60}
pessoa3 = {'Nome': 'Jorge', 'Peso':75}

pessoas = [pessoa1, pessoa2, pessoa3]
maispeso=0
numMais = 0
menospeso=9999
numMenos = 0
for a in range (len(pessoas)):
    if maispeso < pessoas[a]['Peso']:
        maispeso = pessoas[a]['Peso']
        numMais = a

    if menospeso > pessoas[a]['Peso']:
        menospeso = pessoas[a]['Peso']
        numMenos = a

print("A pessoa mais pesada é",pessoas[numMais]['Nome'])
print("A pessoa mais leve é", pessoas[numMenos]['Nome'])