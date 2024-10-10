# Estruturas condicionais

# IF 
# A estutura if é utilizada para executar um bloco de codigo se uma condição for verdadeira. A sintaxe básica é a seguinte:

# if condição:
#   Bloco de codigo a executar se a condição for verdadeira
#   intruções

idade = 18

if idade >= 18:
    print ("Você é maior de idade")

# IF-ELSE
# A estrutura if-else nos permite especificar um bloco de codigo alternativo que será executado se a condição do if for falsa. A sintaxe basica é a seguinte:

idade = 15

if idade >= 18:
    print ("você é maior de idade")
else:
    print ("Você é menor de idade")

# IF-ELIF-ELSE
# A estrutura if-elif-else nos permite especificar multiplas condições e blocos de codigos alternativos. A sintaxe basica é a seguinto:

#   if condicao1:
#       Blocode código a executar se a condicao1 for verdadeira
#       Intruções
#   elif condicao2:
#       Bloco de código a executar se a condicao2 for verdadeira
#       Instruções
#   else:
#       Bloco de código a executar se nenhuma condição anterior for verdadeira
#       Instruções

nota = 85

if nota >= 90:
    print ("Excelente")

elif nota >= 80:
    print ("Muito bom")

elif nota >= 70:
    print ("Bom")

else:
    print ("Precisa melhorar")