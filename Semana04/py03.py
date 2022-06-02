#Criando um número inteiro e averiguando seu tipo
num = 3
print(type(num))

#Criando um número float e averiguando seu tipo
num = 3.14
print(type(num))

#Operações matemáticas
print(3+2)
print(3-2)
print(3*2)
print(3/2)
print(3//2)
print(3**2)
print(6%2)
print(3*2+1)
print(3*(2+1))

num = 2
num += 1
print(num)

num = 2
num *= 10
print(num)

#Removendo sinal de números negativos

print(abs(-3))

#Arredondando numeros

print (round(5.67, 1))

#Comparadores

num_1 = 3
num_2 = 2

print (num_1 == num_2)
print (num_1 != num_2)
print (num_1 > num_2)
print (num_1 < num_2)
print (num_1 <= num_2)
print (num_1 >= num_2)

#Usando fazendo operações matemáticas a partir de strings

num_1 = '100'
num_2 = '200.25'

num_1 = int(num_1)
num_2 = float(num_2)

print(num_1+num_2)