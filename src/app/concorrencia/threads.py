from threading import Thread

minha_lista = []


def funcao_a(indice):
    for i in range(100000):
        minha_lista.append(1)
    print("Término thread ", indice)


# O código abaixo cria 10 threads (multi threads), cada uma incrementando a lista minha_lista 100.000 vezes de forma concorrente.
if __name__ == '__main__':
    tarefas = []  # É função do programador armazenar uma referência para as suas threads ou processos, de maneira que possamos verificar seu estado ou interrompê-las.
    for indice in range(10):
        tarefa = Thread(target=funcao_a, args=(indice,))
        tarefas.append(tarefa)
        tarefa.start()

    print("Antes de aguardar o término!", len(minha_lista))

    # Percorremos as tarefas (threads) para garantir que todas tenham terminado (utilizando o método join) antes de prosseguir.
    for tarefa in tarefas:
        tarefa.join()

    print("Após aguardar o término!", len(minha_lista))

# Resumo: Threads rodam concorrentemente, compartilhando a mesma área de memória. Cuidado com condições de corrida!