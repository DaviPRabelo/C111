pessoa1 = {'nome': 'Roberto', 'idade': 30, 'genero': 'm'}
pessoa2 = {'nome': 'Julio', 'idade': 21, 'genero': 'm'}
pessoa3 = {'nome': 'Roberta', 'idade': 25, 'genero': 'f'}
pessoa4 = {'nome': 'Kaike', 'idade': 18, 'genero': 'm'}
pessoa5 = {'nome': 'Julia', 'idade': 35, 'genero': 'f'}
pessoa6 = {'nome': 'Rebeca', 'idade': 14, 'genero': 'f'}
pessoa7 = {'nome': 'Adriana', 'idade': 12, 'genero': 'f'}
pessoa8 = {'nome': 'Pamela', 'idade': 19, 'genero': 'f'}
pessoa9 = {'nome': 'Flavia', 'idade': 47, 'genero': 'f'}

todasPessoas = [pessoa1,pessoa9,pessoa8,pessoa4,pessoa5,pessoa6,pessoa7,pessoa3,pessoa2]
media = 0
qntFMenorVinte = 0
for a in range (len(todasPessoas)):
    media += todasPessoas[a]['idade']
    if todasPessoas[a]['genero'] == 'f' and todasPessoas[a]['idade'] < 20:
        qntFMenorVinte +=1


print('Media de idade é', media/len(todasPessoas))
print(qntFMenorVinte)
