# Como lidar com condições de corrida? Segue abaixo exemplo de uma condição de corrida.
from threading import Thread

contador = 0


def funcao_a(indice):
    global contador
    for i in range(1000000):
        contador += 1
    print("Término thread ", indice)


if __name__ == '__main__':

    tarefas = []

    for indice in range(10):
        tarefa = Thread(target=funcao_a, args=(indice,))
        tarefas.append(tarefa)
        tarefa.start()

    print("Antes de aguardar o término!", contador)

    for tarefa in tarefas:
        tarefa.join()

    print("Após aguardar o término!", contador)

"""
Conclusão: O método utilizado para inserir um elemento na lista (append) no arquivo threads.py, na visão do GIL, é atômico,
ou seja, ele é executado de forma segura e não pode ser interrompido no meio de sua execução. Já o contador inteiro utilizado
neste exemplo não é atômico, pois ele é composto por duas operações: leitura e escrita. Portanto, a operação de incremento do
contador não é atômica e pode ser interrompida no meio de sua execução. Isso pode resultar em um valor final do contador menor 
do que o esperado. Por exemplo:

Cada thread é executada em um determinado tempo t:
# Em t1, a thread1 lê e incrementa o contador, que passa a valer 1. 
# Em t2, a thread2 lê o contador (valor 1). 
# Em t3, a thread3 lê e incrementa o contador, que passa a valer 2. 
# Em t4, a thread2 incrementa o contador, porém a partir do valor que ela leu, que era 1.
No final, o contador passa a valer 2, erroneamente. 
Esse resultado inesperado devido à sincronia na concorrência de threads (ou processos) se chama condição de corrida.

Este é um exemplo clássico de condição de corrida. Outro exemplo é o próprio print 'Término thread' que fica desordenado pois o print
também não é uma operação atômica. Para evitar condições de corrida, é possível utilizar locks, semáforos, entre outros mecanismos de sincronização.

Em Python, a forma mais comum de evitar condições de corrida é utilizando a primitiva lock (trava). Um objeto desse tipo tem somente
dois estados: travado e destravado. Quando criado, ele fica no estado destravado. Esse objeto tem dois métodos: acquire e release.
Quando no estado destravado, o acquire muda o estado dele para travado e retorna imediatamente. 
Quando no estado travado, o acquire bloqueia a execução até que outra thread faça uma chamada ao método release e destrave o objeto.
"""
