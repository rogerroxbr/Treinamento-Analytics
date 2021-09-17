nome = input(f'Informe o nome do aluno: ')

pontos = 0
questao = 1

while questao <= 3:
    resposta = input(f'Resposta da questão {questao} : ')

    if questao == 1 and resposta == "b" or resposta == "B":
        pontos = pontos + 1
    if questao == 2 and resposta == "a" or resposta == "A":
        pontos = pontos + 1        
    if questao == 3 and resposta == "d" or resposta == "D":
        pontos = pontos + 1

    questao += 1

print(f"O Aluno '{nome}' fez {pontos} ponto(s)!")