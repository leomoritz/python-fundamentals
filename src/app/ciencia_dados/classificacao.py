"""
Os algoritmos de classificação são do tipo supervisionado, nos quais passamos um conjunto de características sobre um determinado
item de uma classe de forma que o algoritmo consiga compreender, utilizando apenas as características, qual a classe de um item não mapeado.

Para este exemplo, vamos utilizar um conjunto de dados (dataset) criado em 1938 e utilizado até hoje: o dataset da flor de íris (Iris Dataset).
Ele contém informações de cinquenta amostras de três diferentes classes de Flor de Íris (Iris setosa, Iris virginica e Iris versicolor).

No total, são quatro características para cada amostra, sendo elas o comprimento e a largura, em centímetros, das sépalas e pétalas de rosas.

Por ser um dataset muito utilizado e pequeno, o Scikit-Learn já o disponibiliza internamente.

Vamos treinar dois algoritmos de classificação, árvore de decisão e máquina de vetor suporte (suport vector machine – SVM) para montar dois
 classificadores de flores de íris. A forma como são implementados esses algoritmos estão fora do escopo deste módulo.
"""

from sklearn.datasets import load_iris, fetch_kddcup99
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.svm import SVC

############# Pré-processamento #############

# Coleta e Integração
iris = load_iris()
caracteristicas = iris.data
rotulos = iris.target

print(f"Características: \n{caracteristicas[:2]}")
print(f"Rótulos: \n{rotulos[:2]}")
print("################################################################")

# Partição dos dados
carac_treino, carac_teste, rot_treino, rot_teste = train_test_split(caracteristicas, rotulos)

############# Mineração de Dados #############

# Árvore de Decisão
arvore = DecisionTreeClassifier(max_depth=2)
arvore.fit(X=carac_treino, y=rot_treino)

rot_preditos = arvore.predict(carac_teste)
acuracia_arvore = accuracy_score(rot_teste, rot_preditos)

# Máquina de Vetor Suporte
clf = SVC()
clf.fit(X=carac_treino, y=rot_treino)

rot_preditos_svm = clf.predict(carac_teste)
acuracia_svm = accuracy_score(rot_teste, rot_preditos_svm)

############# Pós-processamento #############
print(f"Acurácia da Árvore de Decisão: {round(acuracia_arvore, 5)}")
print(f"Acurácia SVM: {round(acuracia_svm, 5)}")
print("################################################################")

r = export_text(arvore, feature_names=iris['feature_names'])
print("Estutura da Árvore de Decisão: \n", r)


