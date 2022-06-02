#Dicionário

from multiprocessing.sharedctypes import Value


estudante = {'nome': 'John', 'age': 25, 'cursos': ['Matematica', 'Comp']}

print(estudante)
print(estudante['cursos'])
 
#Configurando para não dar erro ao procurar algo que não existe e sim printar uma mensagem estipulada

print(estudante.get('nome'))
print(estudante.get('phone', 'Não Encontrado'))

#Adicionando uma nova entrada ao dicionário e atualizando

estudante['phone']= '555-5555'
estudante['nome']= 'Carol'
print(estudante)

#Atualizando tudo de uma vez

estudante.update({'nome': 'Joana', 'age': 20, 'phone': '4444-4444'})
print(estudante)

#Deletando

del estudante['age']
phone = estudante.pop('phone')
print(estudante)
print(phone)

#Verificando a quantidade de valores no dicionário

print(len(estudante))

#Vendo somente as chaves do dicionário
print(estudante.keys())

#Vendo somente os valores do dicionário
print(estudante.values())

#Vendo tudo
print(estudante.items())

for key, value in estudante.items():
    print(key, value)

