def calculaDelta(a, b, c):
    # Delta da equação de 2º grau: b^2 - 4.a.c
    delta = b ** 2 - 4 * a * c
    return delta


def encontraRaizDelta(delta):
    if delta > 0:
        print("A equação tem 2 raízes reais.")
    elif delta == 0:
        print("A equação tem 1 raiz real.")
    else:
        print("A equação não tem raiz real.")


a = eval(input("Entre com o coeficiente 'a' da equação: "))
b = eval(input("Entre com o coeficiente 'b' da equação: "))
c = eval(input("Entre com o coeficiente 'c' da equação: "))

delta = calculaDelta(a, b, c) ## Função é o próprio nome dado para uma função que retorna algo
print(f"O valor de delta é: {delta}")
encontraRaizDelta(delta) ## Procedimento é o nome dado para uma função que não possui retorno