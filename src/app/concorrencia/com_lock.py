from threading import Thread, Lock

contador = 0
lock = Lock()
print_lock = Lock()


def funcao_a(indice):
    global contador
    for i in range(1000000):
        lock.acquire()
        contador += 1
        lock.release()
    print_lock.acquire()
    print("Término thread ", indice)
    print_lock.release()


if __name__ == '__main__':
    tarefas = []
    for indice in range(10):
        tarefa = Thread(target=funcao_a, args=(indice,))
        tarefas.append(tarefa)
        tarefa.start()
    print("Antes de aguardar o término!", contador)

    for tarefa in tarefas:
        tarefa.join(0.5)

    print("Após aguardar o término!", contador)
