#Funções básicas de contagens de palavras, achando palavras, descobrindo tamanho do texto e alterar formatação.
message = """Carol's World"""
print(message.lower())
print(len(message))
print(message[0:5])
print(message.count('l'))
print(message.find('l'))

#Substituindo parte do texto

message = message.replace('World', 'Universe')
print(message)

#Juntando strings metodo 1

greeting = 'Hello'
name = 'Carol'

message = greeting + ', '+  name + '. Welcome!'
print(message)

#Juntando strings metodo 2

message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

#Juntando strings metodo 3

message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

#Mostrado os metodos disponiveis e mostra oque o metodo faz

print(dir(name))
print(help(str))