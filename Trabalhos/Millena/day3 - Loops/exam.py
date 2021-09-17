pontos = 0
questao = 1

while questao <= 3:
    resposta = input(f"Resposta da questao {questao}: ").lower()

    # Ou usando o string.lower para tratar o input do usuario
    print(f"Resposta em minusculo: {resposta}")

    if questao == 1 and (resposta == 'b' or resposta == 'B'):
        pontos += 1
    if questao == 2 and (resposta == 'a' or resposta == 'A'):
        pontos += 1
    if questao == 3 and (resposta == 'd' or resposta == 'D'):
        pontos += 1
    questao += 1

print(f"O aluno fez {pontos} ponto(s)")
