"""
Classe criada apenas para demonstrar como criar um atributo de classe (estático) privado
e como acessá-lo atavés de um método de classe em Python.
"""


class Circulo:
    _total_circulos = 0  # atributo de classe (estático)

    def __init__(self, pontox, pontoy, raio):
        self.pontox = pontox
        self.pontoy = pontoy
        self.raio = raio
        type(self)._total_circulos += 1

    @classmethod
    def get_total_circulos(cls):
        """
        Os métodos de classe são a maneira indicada para se acessar os atributos de classe.
        Eles têm acesso diretamente à área de memória que contém os atributos de classe.
        :return: Total de círculos criados
        """
        return cls._total_circulos
