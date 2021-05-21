vingadores = {"Chris Evans": "Capitão América", "Mark Ruffalo": "Hulk", "Tom Hiddleston": "Loki",
"Chris Hemworth": "Thor", "Robert Downey Jr": "Homem de Ferro", "Scarlett Johansson": "Viúva Negra"}

# Métodos para retornar o valor de uma chave
"""
print(vingadores["Chris Evans"])

ator = input("Digite o nome do ator: ")
print(vingadores.get(ator, "Desculpe, não encontrei esse ator"))
"""

# Alterando o valor de uma chave
"""
vingadores["Chris Evans"] = ["Tocha Humana","Capitão"]
print(vingadores)
"""

# Verificando se um item existe como chave ou como valor
"""
print("Hulk" in vingadores.values())
print("Hulk" in vingadores)
print("Mark Ruffalo" in vingadores)
print(vingadores.items())
"""

#Adicionando novos valores
"""
vingadores ["Nick Castle"] = "Michael Myers"
vingadores ["Gal Gadot"] = "Mulher Maravilha"
vingadores ["Joaquin Phoenix"] = "Coringa"
print(vingadores)
"""

#Deletando valores
"""
del vingadores["Nick Castle"] # desvantagem - Dá errro caso a chave não exista
print()
print(vingadores.pop("Gal Gadot","Ator não encontrado")) # Remove a chave e retorna uma mensagem padrão caso ela não exista
print(vingadores.pop("Heath Ledger","Ator não encontrado"))
print()
print(vingadores)
print()
excluido = vingadores.pop("Joaquin Phoenix") # Exclui o valor da chave indicada e armazena na var definida
lista_excluidos = []
lista_excluidos.append(vingadores.pop("Chris Evans"))
lista_excluidos.append(vingadores.pop("Mark Ruffalo"))
print(excluido)
print(lista_excluidos)
print(vingadores)
print()
excluido_popitem = vingadores.popitem() # Remove o último valor. Retorna chave e valor como tupla (pode ser armazenado em uma var)
print(excluido_popitem)
print(vingadores)
"""


animais = {"Cachorro":"Vira Lata Caramelo","Cavalo":"Mangalarga","Gato":"Siamês"}

# Unindo duas listas usando for
"""
for item_percorrido in animais:
    print(item_percorrido)
    vingadores[item_percorrido] = animais[item_percorrido]
    # vingadores["Cachorro"] = animais["Cachorro"] - adicionando um elemento novo
    # vingadores["Cachorro"] = "Vira Lata Caramelo" - Criar a chave nova com o valor atribuido
    print(vingadores)
"""
# UNINDO DOIS DICIONARIOS COM O MÉTODO .update
"""
vingadores.update(animais)
print(vingadores)
"""
