import socket   #importa a biblioteca socket
import time     #importa a biblioteca time 
import sys      #importa a biblioteca sys

UDP_IP = "127.0.0.1"                #define qual o host UDP
UDP_PORT = 5005                     #define qual a porta UDP
buf = 1024                          #define a quantidade de bytes a serem enviados
file_name = sys.argv[1]             #especifica o arquivo


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #starta o socket em pacotes UDP
sock.sendto(file_name, (UDP_IP, UDP_PORT))              #faz o envio de um nome de arquivo em pacotes UDP
print ("Sending %s ..." % file_name)                    #mostra que esta enviando
f = open(file_name, "r")                                #abre um arquivo no para de leitura
data = f.read(buf)                                      #vai ler o arquivo que foi aberto no tamanho de buf
while(data):                                            #inicia um loop
    if(sock.sendto(data, (UDP_IP, UDP_PORT))):          #cria a condição que ve o envio do conteúdo do arquivo em pacotes UDP
        data = f.read(buf)                              #vai ler o arquivo que foi aberto no tamanho de buf
        time.sleep(0.02)                                #define um tempo de delay

sock.close()                                            #vai mandar a socket fechar
f.close()                                               #fecha o arquivo