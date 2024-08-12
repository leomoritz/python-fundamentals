print("EXEMPLO 1 - FUNÇÃO PURA")
valor = 20


# A função é pura, pois ela depende apenas dos valores de entrada e produz sempre a mesma saída para as mesmas entradas
def multiplica(valor, fator):
    valor = valor * fator
    return valor


print("Resultado", multiplica(valor, 3))
print("Resultado", multiplica(valor, 3))

print("\nEXEMPLO 2 - FUNÇÃO PURA: PRINCÍPIO DA IMUTABILIDADE")
valores = [10, 20, 30]


def altera_lista(lista):
    nova_lista = lista.copy()
    nova_lista[2] = nova_lista[2] + 10
    return nova_lista


print("Nova lista", altera_lista(valores))
print("Nova lista", altera_lista(valores))

print("\nEXEMPLO 3 - FUNÇÃO PURA: PRINCÍPIO ZERO LOOPS")
print("\nA função MAP é pura e de ordem superior, pois depende apenas de seus parâmetros e recebe uma função como parâmetro")
lista = [1, 2, 3, 4, 5]


def triplica(item):
    return item * 3

def impar(item):
    return item % 2 != 0

nova_lista = map(triplica, lista)
print("Nova lista usando map: ", list(nova_lista))
print("Nova lista usando map com lambda: ", list(map(lambda item: item * 3, lista)))

print("\nA função FILTER é pura e de ordem superior, pois depende apenas de seus parâmetros e recebe uma função como parâmetro")
nova_lista_filtrada = filter(impar, lista)
print("Nova lista filtrada (FILTER) apenas com números ímpares: ", list(nova_lista_filtrada))
print("Nova lista filtrada (FILTER com lambda) apenas com números ímpares: ", list(filter(lambda item: item % 2 != 0, lista)))



print("\nO objetivo da função pura é evitar efeitos colaterais ou indesejáveis, tornando o código mais previsível e fácil de testar.")
