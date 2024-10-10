## For
# O loop é utilizado para iterar sobre uma sequência(Como uma lista, uma tupla ou uma string) ou qualquer objeto iteravel. A sintaxe básica é a seguinte:
# for variavel in sequencia:
#   Bloco de codigo a repetir
#   Instruções

frutas = ["Maça", "banana", "laranja"]

for fruta in frutas:
    print (fruta)

## While
# O loop while é utilizado para repetir um bloco de código enquanto uma condição for verdadeira. A sintaxe básica é a seguinte:
# while condicao:
#   Bloco de codigo a repetir
#   Instruções

contador = 0

while contador < 5:
    print(contador)
    contador += 1

## Controle de loops

# Break
# A instrução break é utilizada para sair prematuramente de um loop, independente da condição. Quando um break é encontrado, o loop é interrompido e o fluxo de execução
# continua com a proxima instrulção fora do loop

contador = 0

while True:
   print(contador)
   contador += 1

   if contador == 5:
       break
   
# Continue
# A instrução continue é utilizazda pra pular o restante do bloco de código dentro de um loop e passar para a proxima iteração

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# Pass
# A Instrução pass é uma operação nula que não faz nada. É utilizada como um marcador de posição quanto uma instrução é sintaticamente
# necessaria, mas nenhuma ação é desejada.

for i in range(5):
    pass