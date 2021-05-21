vingadores = {"Chris Evans": "Capitão América", "Mark Ruffalo": "Hulk", "Tom Hiddleston": "Loki",
"Chris Hemworth": "Thor", "Robert Downey Jr": "Homem de Ferro", "Scarlett Johansson": "Viúva Negra"}

# Substituindo o valor de uma chave específica
"""
print(vingadores)
vingadores["Mark Ruffalo"] = "Hulk Gladiador"
print(vingadores)
"""
print(vingadores.keys())
print(vingadores.values())
print()

# Printando chaves e valores com for
for chave, valor in vingadores.items():
    print(f"O valor da chave {chave} é: {valor}")

"""
ator = input("digite o nome do ator: ").title()

while ator not in vingadores:
    print("Nome não encontrado, tente novamente")
    ator = input("digite o nome do ator, ou digite 0 para sair: ")
    if ator == "0":
        break
print(vingadores.get(ator, "Nome não encontrado"))
"""

# print(vingadores.get(ator,"O nome não foi encontrado"))








        ### RETORNO 20:53 ###
        ### AS LISTAS ESTÃO POSTADAS ###




