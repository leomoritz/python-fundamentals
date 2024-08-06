# Fundamentos do Python

Este repositório contém um projeto com vários arquivos Python que cobrem os fundamentos da programação em Python. O objetivo deste projeto é fornecer exemplos práticos e didáticos para iniciantes que desejam aprender Python.

## Módulos
### Criando seu próprio módulo
Os desenvolvedores podem criar seus próprios módulos de forma a reutilizar as funções que já escreveram e organizar melhor seu trabalho. Para isso, basta criar um arquivo .py e escrever nele suas funções. É importante observar que o arquivo do módulo precisa estar na mesma pasta do arquivo para onde ele será importado.

## Pacotes externos
### Atenção
Quando estiver trabalhando com pacotes externos, é extremamente recomendado o uso de ambientes virtuais (em inglês virtual environments ou simplesmente virtualenvs). Esses ambientes isolam o projeto em que você está trabalhando, e uma das vantagens disso é que você consegue saber exatamente quais pacotes externos estão sendo usados no projeto.

É possível usar pacotes externos sem o uso de ambientes virtuais, porém isso pode causar uma confusão caso você tenha vários projetos Python no seu computador.

Pesquise mais sobre ambientes virtuais e configure um em cada projeto. Não é muito difícil e vai te ajudar a deixar o seu código mais profissional!

### Instalando pacotes externos
Para instalar um pacote externo disponível no PyPI, basta abrir o seu terminal (clique no botão do Windows e digite “cmd” ou “prompt de comando”), ative o seu ambiente virtual (se você estiver usando um) e digite o seguinte comando: d: \Projects\exemplo_pacotes>pip install <nome_do_pacote>

Substitua <nome_do_pacote> pelo pacote que você deseja usar. Temos inúmeros pacotes prontos à nossa disposição. Cada pacote normalmente possui um site que apresenta a sua documentação, de forma similar à documentação oficial do Python.

Abaixo você encontra uma lista com alguns dos pacotes externos mais comuns e utilizados no mercado:

| Nome do Módulo   | Para que Serve                                                       |
|------------------|----------------------------------------------------------------------|
| `numpy`          | Cálculos, operações matemáticas e simulações                         |
| `pandas`         | Manipulação de dados                                                 |
| `scikit-learn`   | Modelos de aprendizado de máquina                                    |
| `matplotlib`     | Visualização de dados                                                |
| `requests`       | Biblioteca de comandos de comunicação pelo protocolo HTTP            |
| `flask`          | Construção de aplicações web                                         |

### Dica
Antes de começar o seu próprio módulo, é sempre recomendado pesquisar se o que você quer fazer já existe em algum pacote popular. Se existir, procure pela documentação e instale esse pacote.

O uso de módulos oriundos de pacotes externos é idêntico ao uso dos módulos da biblioteca padrão, basta utilizar o import nome_do_modulo no seu código.

