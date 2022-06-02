""" def hello_func():
    pass

print(hello_func)
print(hello_func()) """

#DRY

""" def hello_func():
    print('Hello Function!')

hello_func() """

#Função retornando argumentos
""" def hello_func():
    return('Hello Function.')

print(hello_func())
print(hello_func().upper()) """
#print(len('Test'))

#Passando argumentos para a função

from operator import is_


def hello_func(greeting, name = 'You'):
    return'{}, {}'.format(greeting, name)

print(hello_func('Hi', 'Carol'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
courses = ['Math', 'Art']
info =  {'name': 'Carol', 'age': 22}

#student_info('Math', 'Art', name = 'Carol', age=22)
#student_info(courses, info)
student_info(*courses, **info)

#EXEMPLO

dias = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def dias_no_mes (year , mes):

    if not 1 <= mes <= 12:
        return "Mes Invalido"

    if mes == 2 and is_leap(year):
        return 29
    
    return dias[mes]

print(is_leap(2017))
print(is_leap(2020))
print(dias_no_mes(2017, 2))
