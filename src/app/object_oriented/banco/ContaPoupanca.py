import datetime


class ContaPoupanca:

    def __init__(self, taxa_remuneracao):
        self.taxa_remuneracao = taxa_remuneracao
        self.saldo = 0
        self.data_hora_abertura = datetime.datetime.now()

    def calcular_remuneracao_conta(self):
        self.saldo += self.saldo * self.taxa_remuneracao
