import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.56.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello Carol!")
input()
send("Falta 1 input para a desconexão do client!")
input()
send("Desconectando!")

send(DISCONNECT_MESSAGE)

"""

O programa client se conecta ao server, após a abertura do mesmo, 
após isso ele envia a mensagem porgramada para envio após a
conexão e depois responde aos dois inputs e se desconecta. E desta forma 
poder ser feita com a quantidade de clientes desejadas.

"""