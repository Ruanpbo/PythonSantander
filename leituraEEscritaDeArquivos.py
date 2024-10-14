# Python nos permite ler e escrever dados em arquivos externos. Podemos abrir arquivos em diferentes modos
# como leitura("r"), escrita("w") ou anexar("a") e realizar operações de leitura e escrita.
#
## Leitura de arquivos
#   Para ler o conteudo de um arquivo, primeiro devemos abri-lo utilizando a função open() em modo leitura("r")
#   depois podemos ler o conteúdo do arquivo utilizando métodos como read() ou readlines().
arquivo = open("README.md", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

## Escrita de arquivos
#   Para escrever dados em um arquivo, abrimos em modo de escrita("w") utilizando a função open(). Se o arquivo não existir, será criado automaticamente.
#   se o arquivo já existir, seu conteúdo sera sobrescrito.
arquivo = open("dados.txt", "w")
arquivo.write("Olá, mundo!")
arquivo.close()

#   Neste exemplo, o arquivo "dados.txt" é aberto em modo de escrita utilizando open(). Depois, a string "Ola, mundo!" é escrita no arquivo utilizando o 
#   método write(). Finalmente, o arquivo é fechado utilizando o metodo close()
#   você pode utilizar a declaração with para manejar a abertura e fechamento de arquivos de maneira automática.
with open ("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

#   Neste caso, o arquivo é aberto utilizando a declaração with e é fechado automaticamente uma vez que se sai do bloco with, mesmo se ocorrer uma exceção.