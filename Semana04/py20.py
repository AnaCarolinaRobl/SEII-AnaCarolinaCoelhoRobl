#f = open('test.txt')

try:
    #pass
    f = open('test.txt')
    #if f.name == 'test.txt':
        #raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    #print('Não Existe')
    print("Error")
else:
    #pass
    print(f.read())
    f.close()
finally:
    #pass
    print("Executing Finally...")

print('End of program')