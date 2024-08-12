# EXEMPLO 1
valor = 20


# A função não é pura, pelos seguintes motivos:
# ela não depende apenas dos parâmetros de entrada, ela também depende de uma variável global
# ela não retorna um valor, ela apenas imprime o resultado
def multiplica(fator):
    global valor
    valor = valor * fator
    print("Resultado", valor)


multiplica(3)
multiplica(3)

# EXEMPLO 2
valores = [10, 20, 30]


# A função não é pura, pelos seguintes motivos:
# ela viola o princípio da imutabilidade modificando o valor de um dos elementos da lista original ao invés de retornar uma nova cópia da lista
def altera_lista(lista):
    lista[2] = lista[2] + 10
    return lista


print("Nova lista", altera_lista(valores))
print("Nova lista", altera_lista(valores))
