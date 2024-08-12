from multiprocessing import Process

minha_lista = []


def funcao_a(indice):
    for i in range(100000):
        minha_lista.append(1)
    print("Término processo ", indice)


# O código abaixo cria 10 processos, cada uma incrementando a lista minha_lista 100.000 vezes de forma paralela.
if __name__ == '__main__':
    tarefas = []  # É função do programador armazenar uma referência para as suas threads ou processos, de maneira que possamos verificar seu estado ou interrompê-las.
    for indice in range(10):
        tarefa = Process(target=funcao_a, args=(indice,))
        tarefas.append(tarefa)
        tarefa.start()

    print("Antes de aguardar o término!", len(minha_lista)) # Será zero, pois as áreas de memória dos processos não são compartilhadas tal como ocorre com as threads. Cada processo acaba criando uma versão própria da variável minha_lista.

    # Percorremos as tarefas (processos) para garantir que todos tenham terminado (utilizando o método join) antes de prosseguir.
    for tarefa in tarefas:
        tarefa.join()

    print("Após aguardar o término!", len(minha_lista)) # Será zero, pois as áreas de memória dos processos não são compartilhadas tal como ocorre com as threads. Cada processo acaba criando uma versão própria da variável minha_lista.

# Resumo: Processos rodam paralelamente, mas não compartilham a mesma área de memória. Cada processo tem sua própria cópia da memória.