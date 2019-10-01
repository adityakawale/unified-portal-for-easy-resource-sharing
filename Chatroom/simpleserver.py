import socket
import threading
all_connections = []
all_address = []

def create_socket():
    print("Creating the server socket....")
    global ss
    ss = socket.socket()  # socket for server gets created
    print("[Socket for the server created]")

def binding_socket():
    host = socket.gethostbyname(socket.gethostname())
    port = 12345
    print("Binding the socket to the server....")
    ss.bind((host,port))
    print("[Binded successfully]")
    ss.listen(5)

def socket_accept():

    conn,address = ss.accept()
    tnew = threading.Thread(target=chat_room(conn,address[1]))
    tnew.start()


def chat_room(conn,address):

    while True:
        cli_resp = conn.recv(1024)
        cli_resp = cli_resp.decode("utf-8")

        if cli_resp == "quit":
            print("[Client [%s] disconnected]"%(str(address)))
            conn.close()
            break
        else:
            print("Client [%s] says : "%(str(address)), cli_resp)


create_socket()
binding_socket()
while True:
    socket_accept()