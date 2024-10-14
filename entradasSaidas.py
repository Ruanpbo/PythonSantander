# Para obter informações do usuário durante a execução do programa, podemos utilizar a função input().
# Essa função mostra uma mensagem na tela e espera que o usuário insira um valor.
nome = input("Insira seu nome: ")
idade = input("Insira sua idade")

print("Olá, "+ nome + "!")
print("você tem "+ idade + "anos.")

# A função input() sempre retorna uma cadeia de texto. Se você deseja trabalhar com outros tipos de dados,
# como numeros inteiros ou flutuantes, deve realizar uma conversão explicita utilizando funções como int()
# ou float
idade = int(input("Insira sua idade: "))

if idade >= 18:
    print("você é maior de idade.")
else:
    print("você é menor de idade.")

# Saida de dados
# Para mostrar informações na tela, utilizamos a função print(). Essa função recebe um ou mais argumentos e
# os mostra no console.
# Para utilizarmos a f-string(formatação de cadeias) para inserir variáveis diretamente dentro de uma cadeia
# de texto
nome = "Ruan"
idade = 25

print(f"Olá, meu nome é {nome} e tenho {idade} anos.")

# Neste caso, as variaveis são inseridas dentro da cadeia utilizando chaves {} e a cadeia é precedida pela letra f pra indicar que é uma f-string.