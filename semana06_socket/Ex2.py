import socket      #importa a biblioteca socket

TCP_IP = "127.0.0.1"    #indica qual o host
FILE_PORT = 5005        #define a port de nome do arquivo
DATA_PORT = 5006        #define a port de dados do arquivoo
timeout = 3             #definiu uma variavel, mas não utilizou
buf = 1024              #define a quantidade de bytes a serem enviados


sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #starta o socket f
sock_f.bind((TCP_IP, FILE_PORT))        #define o socket como servidor e inicializa com o host e a porta de nome
sock_f.listen(1)                        #faz a tentativa de conexão com o de máximo 1 client

sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #starta o socket d
sock_d.bind((TCP_IP, DATA_PORT))         #define o socket como servidor e inicializa com o host e a porta de dados
sock_d.listen(1)                         #faz a tentativa de conexão com o de máximo 1 client


while True:                             #inicia o loop
    conn, addr = sock_f.accept()        #faz a conexão com o client
    data = conn.recv(buf)               #recebe o nome do arquivo com o numero de bytes definido em buf
    if data:                            #cria a condição de caso receber algo
        print ("File name:", data)      #mostrar o nome do arquivo
        file_name = data.strip()        #e para efeito visual faz a remoção dos espaços do começo e do final do nome do arquivo

    f = open(file_name, 'wb')           #abre/cria um arquivo no para de escrita e em binário

    conn, addr = sock_d.accept()        #faz a conexão com o client
    while True:                         #inicia o loop dentro do loop primário
        data = conn.recv(buf)           #escreve em data a quantidade buf de dados do client
        if not data:                    #se não receber data
            break                       #quebra o loop (sai dele)
        f.write(data)                   #escreve no arquivo que foi aberto a variavel data escrita pelo client

    print("%s Finish!" % file_name)     #mostra que terminou
    f.close()                           #fecha o arquivo