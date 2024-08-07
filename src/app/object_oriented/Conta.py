import datetime

from src.app.object_oriented.Extrato import Extrato


class Conta:
    def __init__(self, clientes, numero, saldo):
        self.__numero = numero
        self.__saldo = saldo
        self.__clientes = clientes
        self.__data_abertura = datetime.datetime.now()
        self.__extrato = Extrato()

    # Obs: Importante ressaltar que, em Python, não é obrigatório ter um método construtor na classe,
    # apenas se for necessária alguma ação na construção do objeto, como inicialização e/ou atribuição de valores.

    @staticmethod
    def __valida_valor(valor):
        """
        Função estática privada que valida o valor de depósito.
        :param valor: Valor a ser validado
        """
        if valor is None:
            raise ValueError("Valor de depósito não pode ser nulo.")
        elif valor <= 0:
            raise ValueError("Valor de depósito deve ser maior que zero.")
        elif not isinstance(valor, (int, float)):
            raise ValueError("Valor de depósito deve ser um número inteiro ou real.")

    def depositar(self, valor):
        self.__valida_valor(valor)
        self.__saldo += valor
        print("Depósito realizado com sucesso!")
        self.__extrato.adicionar_transacao("Depósito", valor)

    def sacar(self, valor):
        self.__valida_valor(valor)
        if self.__saldo >= valor:
            self.__saldo -= valor
            print("Saque realizado com sucesso!")
            self.__extrato.adicionar_transacao("Saque", valor)
        else:
            raise ValueError("Saldo insuficiente para realizar o saque.")

    def transferir(self, valor, conta_destino):
        try:
            self.__valida_valor(valor)
            self.sacar(valor)
            conta_destino.depositar(valor)
            print("Transferencia realizada com sucesso!")
            self.__extrato.adicionar_transacao("Transferência", valor)
        except ValueError as e:
            raise ValueError(f"Não foi possível realizar a transferência: {e}")

    def gerar_extrato(self):
        print("--------------------------------------")
        print(f"EXTRATO BANCÁRIO \nConta: {self.__numero} - Saldo: R${self.__saldo:.2f}")
        self.__extrato.imprimir_transacoes()
        print("--------------------------------------")

    def imprimir_clientes(self):
        clientes = [self.__clientes] if not isinstance(self.__clientes, list) else self.__clientes
        for cliente in clientes:
            cliente.imprimir_cliente()
