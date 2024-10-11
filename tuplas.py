# Tuplas
#
# Uma tupla é uma estrutura de dados imutavel e ordenada que permite armazenar uma coleção de elementos.
# Os elementos de uma tupla são encerrados entre parênteses (), separado por virgulas.
#
# Criação e acesso
# Para criar uma tupla, encerre os elementos entre parenteses:
ponto = (3,4)

# Para acessar os elementos de uma tupla, utilize o indice do elemento entre colchetes, similar as listas:
print(ponto[0]) # Imprime 3
print(ponto[1]) # Imprime 4

# Métodos de tuplas
#   Embora as tuplas sejam imutaveis, Python oferece vários métodos úteis para trabalhar com elas
#
#   count(elemento): devolve o número de vezes que um elemento aparece na tupla
#   index(elemento): devolve o índice da primeira aparição de um elemento na tupla. Opcionalmente, pode-se especificar o início e fim da busca
#   len(tupla): embora não seja um método de tupla propriamente dito, esta função incorporada devolve o comprimento da tupla.
minha_tupla = (1,2,3,2,4,2)

print(minha_tupla.index(2)) #saida: 1
print(minha_tupla.index(2, 2)) #saida: 3
print(minha_tupla.index(2,2,4)) #saida: 3