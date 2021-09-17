n1 = int(input("Informe um valor: "))
n2 = int(input("Informe um valor: "))
n3 = int(input("Informe um valor: "))

if n1 > n2 and n1 > n3:
    if n2 > n3:
        print(f'{n1} é o maior número!')
        print(f'{n3} é o menor número!')
    else:
        print(f'{n1} é o maior número!')
        print(f'{n2} é o menor número!')

elif n2 > n1 and n2 > n3:
    if n1 > n3:
        print(f'{n2} é o maior número!')
        print(f'{n3} é o menor número!')
    else:
        print(f'{n2} é o maior número!')
        print(f'{n1} é o menor número!')

elif n3 > n1 and n3 > n2:
    if n1 > n2:
        print(f'{n3} é o maior número!')
        print(f'{n2} é o menor número!')
    else:
        print(f'{n3} é o maior número!')
        print(f'{n1} é o menor número!')

else:
    print("Há numeros iguais, reinicie o programa...!")
