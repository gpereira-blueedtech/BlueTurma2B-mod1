"""
lista1 = [1, 2, 3, "String", "String2"]
tupla1 = ("Nome","123-456")
lista3 = [("Nome","123-456"), 2, 3, "String", "String2"] # Coloquei a tupla dentro da lista, como um dos elementos dela
"""

# Criando lista com tuplas
lista_contatos = [("Ana Paula","123-456"),("Joao","456-789"),("Fabricio","444-777"),("Ricardo","777-888"),("Bruno","999-888")]
print(len(lista_contatos))
print(type(lista_contatos))
print(lista_contatos)
print(lista_contatos[0])
print(lista_contatos[0][0])
print()

# Criando um dicionário a partir da lista acima com a função dict()
contatos = dict(lista_contatos) # dicionario = dict(lista_a_ser_convertida)
print(contatos)
print("Type de contatos:")
print(type(contatos))
print()

# Acessando um valor dentro de um dicionário
print('Acessando o valor da chave "Ana Paula"')
print(contatos.get("Ana Paula"))
print(contatos["Ana Paula"])

# print(contatos["Eurico"]) # KeyError - A chave não existe

print(contatos.get("Eurico","Nome não encontrado")) # Retorna um valor padrão caso a chave não seja encontrada

nome = input("Digite o nome: ") # Recebendo uma entrada para procurar o valor
print(contatos.get(nome,"Nome não encontrado")) 


#Criando um dicionario "na mão"
"""
dicionario_contatos = {"Alexandre":"555-444", "Talita":"111-222", "Nadja":"666-333"}
print(dicionario_contatos)
print(len(dicionario_contatos))
"""
