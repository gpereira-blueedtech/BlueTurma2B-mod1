pessoas = {'Albert Einstein': '1879',
        'Benjamin Franklin': '1706',
        'Chuck Norris': '1940',
        'Bruce Lee': '1940',
        'Rowan Atkinson': '1955'}

print("Bem vindo! Nós temos essas pessoas cadastradas:")
for item_percorrido in pessoas:
    print(item_percorrido)

# print(pessoas[nome]) #Método mais fácil, mas não tem validação
# SINTAXE: dicionario[chave] -> retorna o valor da chave especificada

nome = input("Digite o nome: ").title() # title() -> Altera a string, colocando as primeiras
                                        # letras de todas as palavras em maiúsculuas

print(pessoas.get(nome,f"Desculpe, o nome {nome} não foi encontrado."))
# SINTAXE: dicionario.get(chave) # Retorna o valor da chave especificada
ano = int(pessoas[nome])
idade = 2021 - ano
print(f"A idade de {nome} é {idade}")



        ### RETORNO 21:33 ###

