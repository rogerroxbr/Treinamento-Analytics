def exibir_preco (*, nome_produto, preco): # nome_produto e preco precisam ser nomeados!
    # def exibir_preco (nome_produto, *, preco): # preco precisa ser nomeado!
    """ Exibe o nome e o preço c/ uma váriavel que precisa ser nomeada! """
    print(f'{nome_produto} : R${preco}')

# exibir_preco('Iphone', 1000) : Erro
# exibir_preco('Iphone', preco=1000) : Erro
exibir_preco(nome_produto='Iphone', preco=1000)

def exibir_preco(nome_produto='Iphone', preco=1000): # Valor padrão!
    """ Exibe o preço c/ valores padrões! """
    print(f'{nome_produto} : R${preco}')

exibir_preco('Carro', 20000)
exibir_preco()

def exibir_nome(first_name, middle_name, last_name=''): # last_name é um valor não obrigatório!
    full_name = first_name + " " + middle_name + " " + last_name
    return full_name.title()

print(exibir_nome("Arthur", "Diesel"))

def num_indeterminado_params(*args):
    # Os argumentos são passados como uma lista!
    contagem_valores = 0
    for x in args:
        print(x, end=" ")
        contagem_valores += 1
    print('\n')
    print(f"Foram passados {contagem_valores} valores como argumento!")

num_indeterminado_params('a', 'b', 'c', 1,2,3,4,5,6,7,8,9   )
num_indeterminado_params()