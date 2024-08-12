from multiprocessing import Value, Process


def funcao_a(indice, cont):
    for i in range(1000000):
        with cont.get_lock(): # O Python já disponibiliza essa trava nos objetos do tipo value, não sendo necessário criar uma variável específica para a trava (lock). Observe como foi realizada a trava utilizando o método get_lock()
            cont.value += 1
    print("Término processo ", indice)


if __name__ == '__main__':
    contador = Value('i', 0) # i = integer e valor inicial (0)
    tarefas = []
    for indice in range(10):
        tarefa = Process(target=funcao_a, args=(indice, contador))
        tarefas.append(tarefa)
        tarefa.start()

    print("Antes de aguardar o término!", contador.value)

    for tarefa in tarefas:
        tarefa.join()

    print("Após aguardar o término!", contador.value)
