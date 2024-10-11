# Criação e acesso
#
# Para criar um dicionário, utilize chaves e separe as chaves e valores com dois pontos.
pessoa = {"nome":"Joao","idade":25,"cidade":"madri"}

# Para acessar os valores de um dicionario, utilize a chave correspondente entre cochetes:
print(pessoa["nome"]) # Imprime "Joao"
print(pessoa["idade"]) # Imprime 25
print(pessoa["cidade"]) # Imprime "Madri"

# Você também podem utilizar o método get() para obter o valor de uma chave
#
# Métodos de dicionários
# Os dicionario em python têm varios métodos incorporados para manipular e acessar os elementos. Alguns metodos comuns sao:
#   keys(): retorna uma visualização de todas as chaves do dicionario
#   values(): retorna uma visualização de todos os valores do dicionario
#   items(): retorna uma visualização de todos os pares chave-valor do dicionario
#   update(outro_dicionario): atualiza o dicionario com os pares chaves-valor de outro dicionario

pessoa = {"nome":"Joao","idade":25,"cidade":"Madri"}

print(pessoa.keys()) # Imprime dict_keys(["nome","idade","cidade"])
print(pessoa.values()) # Imprime dic_value(["João",25,"Madri"])
print(pessoa.items()) # Imprime dict_items([("nome","João"),("idade",25),("cidade","Madri")])

pessoa.update({"profissao": "Engenheiro"}) # Atualiza o dicionario pessoa adicionando a chave profissao e o valor engenheiro
print(pessoa) # Imprime {"nome": "João", "idade":25, "cidade": "Madri", "profissao": "Engenheiro"}