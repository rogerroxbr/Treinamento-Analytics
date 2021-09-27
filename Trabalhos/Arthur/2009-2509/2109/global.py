def funcao():
    global variavel
    variavel = 'teste'    

funcao()
print(variavel) # não pode ser acessada se a função não é executada antes!