from multiprocessing import Process
from threading import Thread


def funcao_a(nome):
    print(nome)


if __name__ == '__main__':
    t = Thread(target=funcao_a, args=("Minha Thread",))  # Cria uma thread com a função funcao_a e passa o argumento "Minha Thread" para a função funcao_a
    t.start()  # Inicia a thread

    p = Process(target=funcao_a, args=("Meu Processo",))  # Cria um processo com a função funcao_a e passa o argumento "Meu Processo" para a função funcao_a
    p.start()  # Inicia o processo
