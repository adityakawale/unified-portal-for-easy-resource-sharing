import socket

print("Creating the client socket....")
cs = socket.socket()
print("[Client socket created]")

host = socket.gethostbyname(socket.gethostname())
port = 12345

cs.connect((host,port))
print("connected to the server")

while True:
    cli_answer = input("Client : ")
    if cli_answer == "quit":
        break
    else:
        cli_answer = cli_answer.encode()
        cs.send(cli_answer)

cs.close()
