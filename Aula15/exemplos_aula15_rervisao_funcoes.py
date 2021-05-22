# importa funções específicas dentro de um módulo
# Quando eu for chamá-las (as funções), é só chamar pelo nome()
#from faz_tudo import principal, secundaria #from nome_do_arquivo import funcoes, funcoes

# Importa tudo de um módulo. Para chamar cada função, devo usar modulo.nome_da_funcao()
import faz_tudo

num1 = float(input("Digite a primeira nota: "))
num2 = float(input("Digite a segunda nota: "))

final = faz_tudo.principal(num1,num2) # Executa e guarda o retorno em final
# faz_tudo.secundaria() # Executa a função e não guarda o retorno

print(type(final))
aluno = {"nome":"Aluno", "Nota 1": num1, "Nota 2":num2, "Média":final[0], "Soma das notas":final[1]}
print(aluno)


# Esemplo de argumentos padrão
# for i in range(5,10,2): # Padrão: range(0,n,1)
#     print (i)





