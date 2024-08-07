import datetime


class Extrato:
    def __init__(self):
        self.__transacoes = []

    def adicionar_transacao(self, tipo_descricao, valor):
        self.__transacoes.append([tipo_descricao, valor, "Data", datetime.datetime.now()])

    def imprimir_transacoes(self):
        print("# Transações Realizadas")
        for transacao in self.__transacoes:
            print(f"{transacao[0]:15s}"
                  f"{transacao[1]:10.2f}"
                  " | "
                  f"{transacao[2]:10s}"
                  f"{transacao[3].strftime('%d/%m/%Y %H:%M:%S')}")