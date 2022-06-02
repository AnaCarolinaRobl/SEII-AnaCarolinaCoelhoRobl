import os
from datetime import  datetime
from posixpath import dirname

#print(dir(os))
#print(os.getcwd())

#os.chdir('/Users/anaca/Desktop')


#Criando diretório
#os.mkdir('OS-Demo-2')
#os.makedirs('OS-Demo-2/Sub-Dir-1')

#Deletando os diretorios 
#os.rmdir('OS-Demo-2')
#os.removedirs('OS-Demo-2/Sub-Dir-1')

#Renomeando Pasta
#os.rename('test.txt', 'demo.txt')

#Pegando Informações
#mod_timeprint(os.stat('demo.txt').st_mtime)
#print(datetime.fromtimestamp(mod_time))


#print(os.getcwd())
#print(os.listdir())
""" 
for dirpath, dirnames, filenames in os.walk('/Users/anaca/Desktop'):
    print('Current Path:', dirname)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print() """


os.chdir('/Users/anaca/Desktop')
#print(os.environ.get('HOME'))

file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)

print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))
print(os.path.isfile('/tmp/test.txt'))
print(os.path.splitext('/tmp/test.txt'))
print(dir(os.path))

