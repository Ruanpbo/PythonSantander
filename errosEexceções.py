# Quando escrevemos programas, é comum nos deppararmos com situação insperadas ou erros durante a execução. Python fornece um mecanismo
# para lidar com esses erros de maneira controlada utilizando  o tratamento de exceções. Isso nos permite capturar e lidar com erros especificos
# sem que o programa pare abruptamente.
#
# Erros comuns em python
# Antes de mergulharmos nos tratamento de exceçõe, vejamos alguns erros comuns que você pode encontrar em python.
#
# Erro de sintaxe(SyntaxError)
# Ocorre quando o código não segue as regras de sintaxe do python como esquecer dois opntos após uma declaração de função ou um loop
#
def minha_funcao() #Faltam os dois pontons
    print("Ola")
#
# Erro de nome(NameError)
# Ocorre quando se faz referencia a uma variável ou função que não foi definida.
#
print(variavel_não_definida)
#
# Erro de tipo(TypeError)
# Ocorre quando se realiza uma operação com tipos de dados incompativeis, como tentar somar um número e umma string
#
resultado = 5 + "10"
#
# Erro de indice(IndexError)
# Ocorre quando se tenta acessar um indice fora do intervalo válido de uma lista ou sequencia
#
lista = [1,2,3]
print(lista[3]) # O indice 3 esta fora do intervalo
#
# Try
# O bloco Try contém o código que pode ferara uma exceção. Se ocorrer uma exceção dentro do bloco try , o fluxo de execução é transferido para o bloco except correspondente
try:
    #codigo que pode gerar uma exceção
    resultado = 10/0 # Divisão por 0
    print(resultado)
except zeroDivisionError:
    print("Erro: Divisão por zero")

# Except
# O bloco except especifica o tipo de exceção que se deseja capturar e lidar. Você pode ter  multiplos blocos except para lidar com diferentes tipos de exceções
try:
    # Código que pode gerar uma exceção
    resultado = 10/0 # Divisão por zero
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")
except ValueError:
    print("Erro: valor invalido")

# Finally
# O bloco finally é opcional e é executado sempre, independente de ter ocorrido uma exceção ou não. É comumente utilizado para realizar tarefas de limpeza
# ou liberação de recurso
try:
    # código que pode gerar uma exceção
    arquivo = open("arquivo.txt", "r")
    # Realizar operações com o arquivo
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
finally:
    arquivo.close() # Fecha o arquivo sempre, mesmo se ocorrer uma exceção