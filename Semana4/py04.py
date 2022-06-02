#Trablhando com Listas
courses = ['História', 'Matemática', 'Fisica', 'CompSci']

print(len(courses))
print(courses)
print(courses[0])
print(courses[-1])
print(courses[0:2])
print(courses[:2])
print(courses[2:])

#Adicionando um elemento a Lista

courses.append('Artes') #Adicona ao final da lista
print(courses)

courses.insert(1,'Filosofia') #Adicona a uma posição especifica da lista
print(courses)

#Adicionando mais de um elemento a Lista

courses = ['História', 'Matemática', 'Fisica', 'CompSci']
courses_2 = ['Artes', 'Educação Fisica']
courses.extend(courses_2)
print(courses)

#Removendo Itens da lista

courses.remove('Matemática') #Remove uma parte a ser especificada 
print(courses)

popped =courses.pop() #Remove o ultimo termo
print(popped) #Mostrar qual foi removido
print(courses)

#Revertendo a lista

courses = ['História', 'Matemática', 'Fisica', 'CompSci']
courses.reverse()
print(courses)

#Colocando em ordem alfabetica e numeros em ordem

courses = ['História', 'Matemática', 'Fisica', 'CompSci']
nums = [1 , 5, 2, 4, 3]
courses.sort()
nums.sort()
print(nums)
print(courses)

#Colocando em ordem alfabetica CONTRARIA e numeros em ordem CONTRARIA

courses = ['História', 'Matemática', 'Fisica', 'CompSci']
nums = [1 , 5, 2, 4, 3]
courses.sort(reverse=True)
nums.sort(reverse=True)
print(nums)
print(courses)

#Pegando a ordem alfabetica da lista existente sem alterar a mesma

courses = ['História', 'Matemática', 'Fisica', 'CompSci']
sorted_courses = sorted(courses)
print(sorted_courses)

#Valores minimos, máximos e a soma total

nums = [1 , 5, 2, 4, 3]

print(min(nums))
print(max(nums))
print(sum(nums))

#Achando a posição de valores especificos

courses = ['História', 'Matemática', 'Fisica', 'CompSci']

print(courses.index('CompSci'))

#Verificando se a variavel existe na lista 

courses = ['História', 'Matemática', 'Fisica', 'CompSci']

print('Art' in courses)
print('Fisica' in courses)

#Printando cada item da lista

for item in courses:
    print(item)

for index, item in enumerate(courses):
    print(index, item)

for index, item in enumerate(courses, start=1):
    print(index, item)

#Transfromando a lista em uma string

courses = ['História', 'Matemática', 'Fisica', 'CompSci']
courses_str = ', '.join(courses)
new_list = courses_str.split(', ')
print(courses_str)
print(new_list)

#Trabalhando com listas

list_1 = ['História', 'Matemática', 'Fisica', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Artes'

print(list_1)
print(list_2)

#Tuple (não mutavel)
tuple_1 = ('História', 'Matemática', 'Fisica', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

#tuple_1[0] = 'Artes'

#print(tuple_1)
#print(tuple_2)

#Sets --> Não liga para ordem

cs_courses = {'História', 'Matemática', 'Fisica', 'CompSci', 'Matemática'}
art_courses = {'História', 'Matemática', 'Artes', 'Design'}

print(cs_courses)
print('Matemática' in cs_courses)
print(cs_courses.intersection(art_courses)) #Ve o que tem em comum
print(cs_courses.difference(art_courses)) #Ve as diferenças
print(cs_courses.union(art_courses)) #Combina os dois

#Cirando listas, tuple e sets empy

empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {} #ESTA ERRADO, não cria um empty set!!
empty_set = set()

