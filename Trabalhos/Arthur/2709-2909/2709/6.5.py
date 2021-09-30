# Adicionar Tarefa
# Listar Tarefa
# Opção de Desfazer
# Opção de Refazer

# [' Tarefa 1', 'Tarefa 2']
# ['Tarefa 1'] <- Desfazer
# ['Tarefa 1', 'Tarefa 2'] <- Refazer
# input <- Nova Tarefa

print("Código   | Ação")
print("0        | Sair")
print("1        | Adicionar")
print("2        | Listar")
print("3        | Desfazer")
print("4        | Refazer")

def listar_tarefas(tarefas):    
    print("\n")
    print("Tarefas: ")
    print(tarefas)
    print("\n")

def adicionar_tarefa(tarefa, tarefas):
    tarefas.append(tarefa)

def desfazer(tarefas, antes_tarefas):
    if not tarefas:
        print("Ainda não foi adicionada nenhuma tarefa!")
        return
    ultima_op = tarefas.pop()
    antes_tarefas.append(ultima_op)

def refazer(tarefas, antes_tarefas):
    if not antes_tarefas:
        print("Não há o que fazer!")
        return
    ultima_op = antes_tarefas.pop()
    tarefas.append(ultima_op)


if __name__ == "__main__":

    tarefas = []
    antes_tarefas = []

    while True:

        codigo = int(input("Informe o código da operação a ser realizada: "))

        if codigo == 0:
            print("Obrigado por usar o programa!")
            break

        if codigo == 1:
            tarefa = input("Informe o nome da tarefa a ser adicionada: ")
            adicionar_tarefa(tarefa, tarefas)
            continue

        elif codigo == 2:
            listar_tarefas(tarefas)
            continue

        elif codigo == 3:
            desfazer(tarefas, antes_tarefas)
            continue

        elif codigo == 4:
            refazer(tarefas, antes_tarefas)
            continue
        
        
        