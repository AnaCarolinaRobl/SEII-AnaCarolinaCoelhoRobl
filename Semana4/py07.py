#Loops

#Parando quando encontra
nums = [1, 2, 3, 4,5]

for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)

#Continunando após encontrar
for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)

#
for num in nums:
    for letter in 'abc':
        print(num, letter)

#Usando o Range para rodar um loop X vezes

for i in range(1, 11):
    print(i)

x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

#Loop Infinito (comentando a condição if e o break teremos o loop infinito), basta cricar cntrl+c para sair
x = 0
while True:
    if x == 5:
        break
    print(x)
    x += 1

