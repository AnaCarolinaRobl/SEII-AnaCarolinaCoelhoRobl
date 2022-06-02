#Condicionais

language = 'Python'

if language == 'Python':
    print ('É Python')

elif language == 'Java':
    print ('É Java')
else :
    print('Condicional Falsa')

#Usando o or/and

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

logged_in = False
if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

#Usando o not
if not logged_in:
    print('Please Log in')
else:
    print('Welcome')


#Usando o is

a =[1, 2, 3]
b= [1, 2, 3]
print(id(a))
print(id(b))
print(a is b)

a = b
print(id(a))
print(id(b))
print(a is b)

#Usando a Condition 

condition = False

if condition:
    print('To True')
else:
    print('To False')

condition = None

if condition:
    print('To True')
else:
    print('To False')

condition = []

if condition:
    print('To True')
else:
    print('To False')

condition = 'Test'

if condition:
    print('To True')
else:
    print('To False')
