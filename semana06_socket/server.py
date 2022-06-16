import socket 
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()


"""
Server se conecta com cada cliente individualmente e cada cliente, e cada
cliente se liga ao server, assim o server irá comandar cada passagem de informação
onde por exemplo: se o cliente 1 quiser algo do cliente 2, ele dever pedir ao server
e o server pede ao cliente dois. Ou seja, fucnionando como um intermediador de informações.

Ao se rodar este programa estamos iniciando o server
que assim que rodado o client será detectado (quadno conectado) 
e com o decorrer de passagem de informações do client (no código client desenvolvido
esta limitado a 3 inputs) o server irá responder a cada input com a mensagem : Msg received, até que
o client se desconecte.

"""
