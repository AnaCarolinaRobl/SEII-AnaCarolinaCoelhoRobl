import socket   #importa a biblioteca socket
import select   #importa a biblioteca select

UDP_IP = "127.0.0.1"                #define qual o host UDP
IN_PORT = 5005                      #define qual a porta UDP
timeout = 3                         #define a variavel de tempo de 3s 


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     #starta o socket em pacotes UDP
sock.bind((UDP_IP, IN_PORT))                                #define o socket como um servidor

while True:                                                 #inicia um loop
    data, addr = sock.recvfrom(1024)                        #recebe os dados do client em pacotes UDP
    if data:                                                #se receber data
        print ("File name:", data)                          #mostrar o nome do arquivo
        file_name = data.strip()                            #e para efeito visual faz a remoção dos espaços do começo e do final do nome do arquivo

    f = open(file_name, 'wb')                               #abre/cria um arquivo no para de escrita e em binário

    while True:                                             #inicia o loop dentro do loop primário
        ready = select.select([sock], [], [], timeout)
        if ready[0]:                                       
            data, addr = sock.recvfrom(1024)               #recebe os dados do client em pacotes UDP
            f.write(data)                                  #escreve no arquivo que foi aberto a variavel data escrita pelo client
        else:                                              #Caso a condição anterior não seja satisfetia entra nessa
            print ("%s Finish!" % file_name)               #mostra que terminou
            f.close()                                      #fecha o arquivo
            break                                          #quebra o loop (sai dele)