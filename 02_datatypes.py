# Primeiro de tudo. Este aqui é um comentário.
# Toda linha que inicia com um "#" não é interpretado.
# Para que serve?
# Para documentar. Se o seu código for bem escrito não vai precisar de muitos comentários,
# mas nunca desprese esse recurso pois é muito este é um auxilio poderoso para o leitor.


#################################################################
##                          Strings                            ##
#################################################################


"Isso é uma string."

'Isso Também'

"""
Esta é uma String de multiplas linhas.
Normalmente usam esse tipo de string para documentar alguma função, porque dá pra organizar bem.
"""

'''
Lembrando que esta aqui tbm é string.... aspas duplas e simples tem o mesmo resultado, ainda assim é útil ter essas opções.
Imagina que você precisa incluir as aspas na string, já que são delimitadoras você precisa de duas opções.
Ainda tem a opção de escapar a aspa.

Por exemplo:
'''

"\" <- esta aspa está escapada... significa que o interpretador não vai considerar ela como um delimitador da string."

# Lembrando que uma String é uma classe... isso significa que cada string têm funções para operar sobre elas.

"bla bla".upper()

# Isso aí vai deixar a string maiuscula

"1 2 3 4 5 6 7".split()

# Isso vai separar a string em uma lista. Experimente fazer o mesmo num interpretador. O resultado vai ser uma lista de strings numéricas.
# Poderia ser varios nomes na string e isso iria separar cada nome.
# Tambem pode ser uma lista de palaras separadas por virgula. Ex: "um,dois,tres,batata".split(",")

"um,dois,tres,batata".split(",")

# Existem muitas outras operações que valem a pena dar uma olhada.
# Pode olhar esse link que alem de explicações tem um interpretador para praticar. https://www.w3schools.com/python/python_strings.asp

# Uma lista de algumas operações bastante úteis:

# Concatenação, isso une as strings.

"String um" + "String dois"

# o mesmo pode ser feito com um join

"String um".join("Outra String")

# obter o tamanho da string

len("String")

# O Interpretador do python tem uma função para ajudar a descobrir como funcionam as coisas.

# Experimente usar a função help, que vai explicar quais funções existem na string.

help(str)


#################################################################
##                          Numeros                            ##
#################################################################

# Os dois tipos básicos de numeros são o int e o float, de inteiro e ponto flutuante
# Não tenho muito a falar deles, as operações que se fazer são os mesmos que a matemática faz.


#################################################################
##                          Listas                             ##
#################################################################

# Armazenam uma coleção de elementos, estes que podem ser de qualquer tipo, inclusive outras listas.

["Essa é uma", 'lista', 1, 1.1, str]

# Dá pra armazenar de um tudo nelas... Se quisermos iterar por uma lista podemos usar o statement for

lista = ["um", "dois", "tres"]

for i in lista:
    print(i.upper())

# o código vai digitar cada uma das strings em caixa alta

# As listas do python são bastante versáteis
# Você pode facilmente criar fatias, são os slices

[1,2,3,4,5][:2]

# Isso cria uma lista com o primeiro elemento até o de indice 2 exclusive.
# Ou seja, o numero 3 que está no indice 2 não faz parte do resultado.