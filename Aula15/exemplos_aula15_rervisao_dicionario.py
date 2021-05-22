dicionario = {"Aluno1":"Marcio", "Aluno2": "Rafael", "Aluno3": "Ana Paula"}
"""
print (dicionario)
print (dicionario["Aluno1"])
dicionario["Aluno1"] = "Ycaro" # Alterando o valor de uma chave
print()
print (dicionario)
print (dicionario["Aluno1"])

dicionario["Aluno4"] = "Italo" # Adiciona uma nova chave e valor
print()
print (dicionario)
print (dicionario["Aluno4"])
"""
# Deletando chaves
"""
aluno = input("Nome do aluno: ")
print()
deletados = dicionario.pop(aluno,"Aluno não encontrado") #Apaga a chave informada, ou retorna uma mensagem padrão caso ela não seja encontrada
                                                         #Se atribuído à uma variável, armazena o valor apagado
deletados2 = dicionario.popitem() #Apaga a última chave do dicionário e retorna uma tupla com a chave e valor apagados, pode ser armazenada
print()
print (dicionario)
print(deletados)
print(deletados2)

aluno2 = input("Nome do aluno: ")
del dicionario[aluno2] #Desvantagem: quebra o programa caso não encontre a chave
print()
print(dicionario)
"""

#Criando novos dicionarios
"""
lista = [("Animal","Macaco"),["Fruta","Abacaxi"],("País","Brasil")] # A lista para ser criado o dicionário tem que estar nesse formato, 
                                                                    # uma lista de itens, cada item com 2 elementos

print(len(lista)) # tamanho da lista
dicionario2 = dict(lista) # Criando um dicionário novo a partir de uma lista
dicionario3 = dict()
dicionario4 = {}
print(dicionario2)
print()
dicionario.update(dicionario2) # Juntando dois dicionários
print(dicionario)
"""
# percorrendo o dicionário com chave e valor
for item in dicionario: # Percorre as chaves do dicionário
    print(item)
print()
for item in dicionario.values(): # Percorre os valores do dicionário
    print(item)
print()
for chave, valor in dicionario.items(): #Percorre chave e valor
    print(f"A chave é{chave} e o valor é {valor}")