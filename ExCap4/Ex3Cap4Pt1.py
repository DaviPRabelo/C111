

import numpy as np

mtz = np.zeros([2,2])
a = np.random.randint(0,2)
b = np.random.randint(0,2)

mtz[a][b] = 1

print("Bem vindo ao campo minado!!")
print("Selecione qual ligar ir: [0,0 0,1")
print("                          1,0 1,1]")

print("Selecione a coluna")
c = int(input())
print("Selecione a linha")
d = int(input())
qnt = 1
print(mtz)
while mtz[c][d] != 1 and qnt < 3:
    qnt += 1
    print("Passou, selecione outro")
    print("Selecione a coluna")
    c = int(input())
    print("Selecione a linha")
    d = int(input())

if qnt < 3:
    print("VocÊ falhou, tente denovo")
print(qnt)