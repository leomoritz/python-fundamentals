print("EXEMPLO - FUNÇÃO DE ORDEM SUPERIOR")
print("É uma função que retorna outra função e permite a criação de funções mais genéricas e reutilizáveis.")


def multiplicar_por(multiplicador):
    def multiplicar(multiplicando):
        return multiplicando * multiplicador

    return multiplicar


multiplicar_por_10 = multiplicar_por(10)
print(multiplicar_por_10(5))  # 50
print(multiplicar_por_10(10))  # 100

multiplicar_por_5 = multiplicar_por(5)
print(multiplicar_por_5(5))  # 25
print(multiplicar_por_5(10))  # 50
