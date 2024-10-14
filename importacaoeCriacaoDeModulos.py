# Em Python, um módulo é um arquivo que contém definições de funções, classes e variáveis que podem ser utilizadas 
# em outros programas. A importação de módulos nos permite acessar a funcionalidade definida em outros arquivos e 
# reutilizar código de maneira eficiente. Além disso, podemos criar nossos próprios módulos para organizar e modularizar nosso código.
#
## Importar módulos
#   Para utilizar um módulo em nosso programa, devemos importá-lo utilizando a declaração import. Podemos importatr um módulo completo ou funções
#   específicas de um modulo;
import math

resultado = math.sqrt(25)
print(resultado) # imprime 5.0

# Neste exemplo, importa-se o módulo math utilizando a declaração import. Em seguida, utiliza-se a função sqrt() do módulo math para calcular a raiz quadrada de 25.
# Também podemos importar funções específicas de um módulo utilizando a sintaxe from módulo import função.
from math import sqrt

resultado = sqrt(25)
print(resultado) # Imprime 5.0

## Funções e classes de módulos padrão
#   A biblioteca padrão de Python oferece uma ampla gama de módulos com funções e classes úteis. Alguns exemplos comuns incluem:
#   Math: Fornece funções matemáticas, como sqrt() (raiz quadrada), sin() (seno), cos() (cosseno), entre outras.
#   Random: Oferece funções para gerar números aleatórios, como random() (número aleatório entre 0 e 1), randint() (número inteiro aleatório em um intervalo), entre outras.
#   Datetime: Permite trabalhar com datas e horas, como datetime.now() (data e hora atual), datetime.date() (data), datetime.time() (hora), entre outras.
import random
import datetime

numeroAleatorio = random.randint(1,10)
print(numeroAleatorio) # Imprime um numero aleatorio de 1 a 10

dataAtual = datetime.datetime.now()
print(dataAtual) #imprime a data e hora atual