def calcula_delta(coef_a, coef_b, coef_c):
    # Delta da equação de 2º grau: b^2 - 4.a.c
    delta_result = coef_b ** 2 - 4 * coef_a * coef_c
    return delta_result


def encontra_raiz_delta(delta_result):
    if delta_result > 0:
        print("A equação tem 2 raízes reais.")
    elif delta_result == 0:
        print("A equação tem 1 raiz real.")
    else:
        print("A equação não tem raiz real.")


a = eval(input("Entre com o coeficiente 'a' da equação: "))
b = eval(input("Entre com o coeficiente 'b' da equação: "))
c = eval(input("Entre com o coeficiente 'c' da equação: "))

delta = calcula_delta(a, b, c)  # Função é o próprio nome dado para uma função que retorna algo
print(f"O valor de delta é: {delta}")
encontra_raiz_delta(delta)  # Procedimento é o nome dado para uma função que não possui retorno
