# Além de utilizar os módulos padrão do python, tambem podemos criar nossos proprios modulos para organizar e reutilizar nosso codigo
#
## Criar e utilizar módulos personalizados
# Para criar um módulo personalizado, simplesmente criamos um novo arquivo Python com o nome desejado e definimos as funções, 
# classes e variáveis que queremos incluir no módulo. Por exemplo, criamos um arquivo (no mesmo diretório onde estamos executando 
# Python) chamado meu_modulo.py com o seguinte conteúdo:
# meu_modulo.py
def saudar(nome):
    print(f"ola,{nome}!")

def calcularSoma(a,b):
    return a + b

# Depois de importarmos e utilizar a função definida em meu _modulo.p em outro arquivo python.
import meu_modulo.py

meu_modulo.saudar("João") # Imprime "Ola, João!"
resultado = meu_modulo.calcular_soma(5,3)
print(resultado) # Imprime 8

# Operações.py
import meu_pacote.operacoes as operacoes

resultado = operacoes.somar(5,3)
operacoes.imprimir_mensagem(f"O resultado da soma é: {resultado}")

nome = operacoes.obter_nome_usuario()
operacoes.imprimir_mensagem(f"Olá, {nome}!")