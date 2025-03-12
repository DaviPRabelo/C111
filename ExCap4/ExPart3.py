import numpy as np

dataset = np.loadtxt('../ExCap4/space.csv', delimiter=';', dtype='str', encoding='utf-8')
custo = dataset[1:, -2].astype(float)
valor = custo[custo > 0]
nomes = dataset[1:,1]
space = nomes == "SpaceX"
custosSX = custo[space]
nomesEmpresas, quantMissoes = np.unique(nomes, return_counts=True)
print("Porcentagem de missões que deram certo")
print(np.size(dataset[np.char.find(dataset,'Success')>=0])/np.size(dataset[1:,-1])*100,"%")
print("Média de gastos, baseados em valores disponíveis")
print(np.mean(valor))
print("Quantidade de missões feitas pelo EUA(USA)")
print(np.shape(dataset[np.char.find(dataset,'USA')>=0]))
print("Maior custo de um projeto da SpaceX")
print(np.max(custosSX))
print("Todas as Empresas e a quantidade de missoes")
for i in range(nomesEmpresas.size):
    print(f"{nomesEmpresas[i]}, Quantidade de missoes:{quantMissoes[i]}")


