# Definição e chamada de função
# Para definir uma funçao python, utilizamos a palavra chave def seguida do nome da função e parenteses.
# Opcionalmente podemos espeficificar parametros dentro dos parenteses. O bloco de codigo é identado após dois pontos
# Para chamar um função, simplesmente escrevemos o nome da função seguida de parenteses:
def saudacao():
    print("Olá, mundo!")

saudacao() # Imprime "Ola, mundo!"

# Parametros e argumentos
# As funções podem aceitar parâmetros, que são valores que são passados para a função quando ela é chamada. Os paramentros
# são especificados dentro dos parenteses na definição da função.

def saudacao(nome):
    print(f"Olá, {nome}!")

# Ao chamar a função, fornecemos os argumentos correspondentes aos parâmetros:
saudacao("Joao") # Imprime "Olá, João!"
saudacao("Maria") # Imprime "Olá, Maria!"

# Valores de retorno
# As funções podem retornar valores usando a palavra-chave return. O valor de retorno pode ser usando pelo código que chama a função
def soma(a,b):
    return a + b

resultado = soma(3,4)
print(resultado) # Imprime 7

# Funções anônimas(lambda)
# Python permite criar funções anonimas ou funnções lambda, que são funções sem nome definidas em uma única linha. São comumente usadas para funções pequenas e concisas.

quadrado = lambda x: x ** 2
print(quadrado(5)) # Imprime 25

# Escopo de variaveis (local vs. gobal)
# As variiaveis definidas dedntro de uma finção tem um escopo local o que significa que são só acessiveis dentro da função. por outro lado as variaveis
# definidas fora de qualquer função tem um escopo global e podem se acessadas de qualuqer parte do programa

def funcao():
    variavel_local = 10
    print(variavel_local) # Acessivel dentro da função

variavel_global = 20

def funcao2():
    print(variavel_global) # Acessivel de qualquer lugar

funcao() # Imprime 10
funcao2() # Imprime 20
print(variavel_global) # Imprime 20
print(variavel_local) # Gera um erro, a variavel não está definida neste escopo

# Documentação de funções(Docstrings)
# É uma boa prática documentar nossas funções utilizando docstrings. Os docstrings são cadeias de texto que descrevem o propósito, os parâmetros e o valor 
# de retorno de uma função. São colocados imediatamente após a definição da função e são encerrados entre aspas duplas triplas
def area_retangulo(base, altura):
    """
    Calcula a área de um retângulo.

    Args:
        base(float): A base do retângulo.
        altura(float): A altura do retângulo

    returns:
        float: A área do retângulo.
    """
    return base * altura

# Funções com número variável de argumentos
# Python permite definir funções que aceitem um número variável de argumentos. Isso é feito utilizando o operador * antes do nome do parâmetro.
def soma_variavel(*numeros):
    total = 0
    for numero in numeros:
        tota += numero
    return total

print(soma_variavel(1,2,3,)) # Imprime 6
print(soma_variavel(4,5,6,7)) # Imprime 22