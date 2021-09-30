file=open('line.txt', 'r')

for line in file.readlines():
    print(line)
file.close()