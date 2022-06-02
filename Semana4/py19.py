#Colocando na ordem
#li = [9, 1, 8, 2,7,3,6,4,5]
li = [-9, -1, 8, 2,7,3,6,4,5]
tup = (9, 1, 8, 2,7,3,6,4,5)

s_tup = sorted(tup)
#s_li = sorted(li)
s_li = sorted(li, key=abs)
s_li = sorted(li, reverse=True)

print('Sorted Variable:\t', s_li)
print('Tuple:\t', s_tup)

li.sort()

print('Sorted Variable:\t', li)


class Objeto():
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario
    def __repr__(self) -> str:
        return f'({self.nome}, {self.idade}, {self.salario})'


user1 = Objeto('Ana', '21', '1000')
user2 = Objeto('Carolina', '19', '2000')
user3 = Objeto('Ronaldo', '30', '3000')
usuarios = [user1, user2, user3]


print(sorted(usuarios, key=lambda user: user.nome))

from operator import attrgetter

print(sorted(usuarios, key=attrgetter('idade')))