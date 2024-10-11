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