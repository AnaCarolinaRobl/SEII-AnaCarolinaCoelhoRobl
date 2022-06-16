import socket   #importa a biblioteca socket
import sys      #importa a biblioteca sys

TCP_IP = "127.0.0.1"    #indica qual o host TCP
FILE_PORT = 5005        #define a port de nome do arquivo
DATA_PORT = 5006        #define a port de dados do arquivo
buf = 1024              #define a quantidade de bytes a serem enviados

file_name = sys.argv[1] #especifica o arquivo


try:                    #tenta executar o código
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #starta o socket
    sock.connect((TCP_IP, FILE_PORT))    #ira fazer a conexão do socket no host e na porta nome que foi definido no incio
    sock.send(file_name)                 #faz o envio do nome do arquivo definido para o servidor 
    sock.close()                         #fecha o socket

    print ("Sending %s ..." % file_name) #mostra que esta enviando

    f = open(file_name, "rb")            #abre um arquivo no para de leitura e em binário
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #starta o socket (da mesma forma feita anteriormente)
    sock.connect((TCP_IP, DATA_PORT))    #ira fazer a conexão do socket no host e na porta dados que foi definido no incio
    data = f.read()                      #vai ler o arquivo que foi aberto
    sock.send(data)                      #envia o arquivo lido para o servidor

finally:                #se inicia após a execução do código
    sock.close()        #vai mandar a socket fechar
    f.close()           #fecha o arquivo

