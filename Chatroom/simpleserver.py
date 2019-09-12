import socket

def create_socket():
    print("Creating the server socket....")
    ss = socket.socket()  # socket for server gets created
    print("[Socket for the server created]")

    host = socket.gethostbyname(socket.gethostname())
    port = 12345
    print("Binding the socket to the server....")
    ss.bind((host,port))
    print("[Binded successfully]")
    ss.listen(5)

    print("Waiting for the clients.....")
    conn,address = ss.accept()

    msg = "Thankyou for connnecting to me"
    msg = msg.encode()
    conn.send(msg)

    cli_resp = conn.recv(1024)
    cli_resp = cli_resp.decode("utf-8")
    print("Client says : " , cli_resp)
    conn.close()



create_socket()
