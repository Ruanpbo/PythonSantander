# Criação e operações básicas
# Para criar um conjunto, utilize chaves ou função set():
frutas = {"maça", "banana", "laranja"}
numeros = set([1,2,3,4,5])

# Os conjuntos suportam operações matemáticas de conjuntos
#   União "|"
#   Interseção "&"
#   Diferença "-"
#   simétrica "^"
conjunto1 = {1,2,3}
conjunto2 = {3,4,5}

uniao = conjunto1 | conjunto2
print(uniao) # Imprime {1,2,3,4,5}

intersecao = conjunto1 & conjunto2
print(intersecao) # Imprime {3}

diferenca = conjunto1 - conjunto2
print(diferenca) # Imprime {1,2}

diferencaSimetrica = conjunto1 - conjunto2
print(diferencaSimetrica) # Imprime {1,2,4,5}

# Metodos de conjunto
# Os conjuntos em python têm varios métodos incorporados para manipular e acessar os elementos. Alguns métodos comuns são:
#   add(elemento): adiciona um elemento ao conjunto
#   remove(elemento): remove um elemento do conjunto. Se o elemento não exiter, gera um erro
#   discard(elemento): remove um elemento do conjunto se estiver presente. Se o elemento não existir, não faz nada.
#   clear(): remove todos os elementos do conjunto
frutas = {"maça","banana","laranja"}
print(frutas) # Imprime {'maça','laranja','banana'}

frutas.add("pera")
print(frutas) # Imprime {"maça","banana","laranja","pera"}

frutas.remove("banana")
print(frutas) # Imprime {"maça","laranja","pera"}

frutas.discard("uva")
print(frutas) # Imprime {"maça","laranja","pera"}

frutas.clear()
print(frutas) # Imprime set()