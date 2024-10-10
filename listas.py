## Listas
# Uma lista é uma estrutura de dados mutável e oredenada que permite armazenar uma coleção de elementos.
# Os elementos de uma lista podem ser de diferentes tipos de dados e são encerrados entre colchetes[], separados por virgulas.

# Criar uma lista
# Para criar uma lista, simplesmente encerre os elementos entre colchetes:
frutas = ["Maça", "banana", "laranja"]

# Para acessar os elementos de uma lista, utilize o indice do elemento entre colchetes. Os indices começam a partir de 0.
print(frutas[0]) # Imprime "Maça"
print(frutas[1]) # Imprime "banana"
print(frutas[2]) # Imprime "laranja"

# Você tambem pode acessar os elementos a partir do final da lista utilizando indices negativos. O indice -1 representa o 
# ultimo elemento, -2 representa o penultimo, e assim por diante.
print(frutas[-1])
print(frutas[-2])
print(frutas[-3])

# Metodos de listas
#
# As listas em python têm varios métodos incorporados que nos permitem manipular e modificar so elementos da lista. Alguns métodos comuns são:
#   
#   append(elemento): adiciona um elemento ao final da lista.
#   insert(indice, elemento): insere um elemento em uma posição especifica da lista.
#   remove(elemento): remove a primeira ocorrência de um elemento na lista
#   pop(indice): remove e retorna o elemento em uma posição especifica da lista 
#   sort(): ordena os elementos da lista em ordem ascendente.
#   reverse(): inverte a ordem dos elementos na lista.
frutas = ["maçã", "banana", "laranja"]

frutas.append("pera")
print(frutas) # Imprime ["maça", "banana", "laranja", "pera"]

frutas.insert(1, "uva")
print(frutas) # Imprime ["maça", "uva", "banana", "laranja", "pera"]

frutas.remove("banana")
print(frutas) # Imprime ["maçã", "uva", "laranja", "pera"]

fruta_removida = frutas.pop(2)
print(frutas) # Imprime ["maça", "uva", "pera"]
print(fruta_removida) # Imprime "laranja"

frutas.sort()
print(frutas) # Imprime ["maça", "pera", "uva"]

frutas.reverse()
print(frutas) # Imprime ["uva", "pera", "maça"]

# Lista de compreensão
#
# As listas de compreensão são uma forma concisa de criar novas listas baseadas em uma sequencia existente.
# Permitem filtrar e transformar os elementos de uma lista em uma única linha de código.
# nova_lista = [expressão for elemento in sequência if condição]
numeros = [1,2,3,4,5]
quadrados = [x ** 2 for x in numeros if x %2 ==0]
print(quadrados) # Imprime [4, 16]