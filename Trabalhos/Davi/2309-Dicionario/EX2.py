frase = input("frase: ")

dic = {}

for c in frase:
    if c == " ":
        continue

    if c in dic.keys():
        dic[c] += 1
    else:
        dic[c] = 1

print(dic)
