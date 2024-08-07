class Cliente:
    def __init__(self, nome, cpf, endereco):
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco

    def imprimir_cliente(self):
        print(f"Nome: {self.__nome:<25}"
              f"| CPF: {self.__cpf:<15}"
              f"| Endereço: {self.__endereco:<30}")
