a= 2378
print("Numero 2378")
b =a%10
c = a%100
d = a%1000
e = a%10000
print("Numero da unidade",b)
print("Numero da dezena", int((c - b)/10))
print("Numero da centena",int((d -c)/100))
print("Numero do milhar",int((e-d)/1000))