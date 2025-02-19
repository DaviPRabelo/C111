print("Coloque o nome do aluno e sua nota")
nome = input()
nota = int(input())

dadosAluno = {"Nome": nome, "Nota" : nota}

if dadosAluno['Nota'] >= 50:
    print("O aluno", dadosAluno['Nome'], 'foi AP')
else:
    print("O aluno", dadosAluno['Nome'],  'foi RP')