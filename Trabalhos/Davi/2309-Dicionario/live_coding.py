print("Texto explicativo\n")

questionario = {}

pontuacao = 0
contador = 1
opcoes = ['a', 'b', 'c']

while True:
    pergunta_texto = input("Digite a sua pergunta (digite 0 para sair): ")

    if pergunta_texto == "0":
        break

    print("adicione as opções:")

    alternativas = {}
    for opcao in opcoes:
        alternativas[opcao] = input(f"Digite a alternativa {opcao} da pergunta: ")

    opcao_correta = input("Digite a alternativa correta: ")

    questionario[str(contador)] = {
        'pergunta': pergunta_texto,
        'opções': alternativas,
        'resposta': opcao_correta
    }

    print("")
    contador += 1

for chave, valor in questionario.items():
    print(f"Pergunta {chave}: {valor['pergunta']}")
    print(f"    Alternativas:")
    for alternativa, texto in valor['opções'].items():
        print(f"    {alternativa}) {texto}")

    resposta = input("Resposta: ")

    if resposta == valor['resposta']:
        pontuacao += 1
        print("Você acertou!\n")
    else:
        print(f"Você errou. A alternativa correta era {valor['resposta']}\n")

print(f"Você acertou {pontuacao} de {len(questionario)}")
print(f"Porcentagem de acertos: {pontuacao*100/len(questionario)}%")
