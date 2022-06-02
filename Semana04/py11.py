

""" f = open("test.txt", "w")
f = open("test.txt", "a")
f = open("test.txt", "r+") """

#Mexendo com o arquivo 

f = open("test.txt", "r")

print(f.name)
print(f.mode)
f.close()

#Outra forma de leitura 
with open("test.txt", "r") as f:
	#pass

#Fazendo a leitura de arquivos pequenos
	f_contents = f.read()
	print(f_contents)

#Leitura de arquivos grandes 
	f_contents = f.readlines()
	print(f_contents)

#Printando as duas primeiras linhas com uma linha de diferença
	f_contents = f.readline()
	print(f_contents)
	f_contents = f.readline()
	print(f_contents)

#Printando as duas primeiras linhas sem uma linha de diferença
	f_contents = f.readline()
	print(f_contents, end = '')
	f_contents = f.readline()
	print(f_contents, end = '')

#Printando o conteudo de forma prática 
	for line in f:
		print(line, end = '')

#Printando uma quantidade especifica de argumentos 
	f_contents = f.read(100)
	print(f_contents, end = '')

#Lendo até o final do arquivo
size_to_read = 100
f_contents = f.read(size_to_read)
while len(f_contents) > 0:
	print(f_contents)
	f_contents = f.read(size_to_read)

	
	size_to_read = 10
	f_contents = f.read(size_to_read)
	print(f_contents, end = '')

	f.seek(0)

	f_contents = f.read(size_to_read)
	print(f_contents, end = '')
	print(f.tell())




#Escrevendo no arquivo

with open("test2.txt", "w") as f:
	#pass
	f.write("Test")
	f.seek(0)
	#f.write("Test")
	f.write("R")

#Copiando arquivos
with open("test.txt", "r") as rf:
	with open("test_copy.txt", "w") as wf:
		for line in rf:
			wf.write(line)

#Copiando Imagens linha por linha
with open("test.jpg", "rb") as rf:
	with open("test_copy.jpg", "wb") as wf:
		for line in rf:
			wf.write(line)

##Copiando Imagens usando chunk
""" with open("test.jpg", "rb") as rf:
	with open("test_copy2.jpg", "wb") as wf:
		chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size) """