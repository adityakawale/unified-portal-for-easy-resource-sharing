import socket

print("Creating the client socket....")
cs = socket.socket()
print("[Client socket created]")

host = socket.gethostbyname(socket.gethostname())
port = 12345

cs.connect((host,port))
print("connected to the server")


ser_resp = cs.recv(1024)
ser_resp = ser_resp.decode("utf-8")
print("Server says : ",ser_resp)

cli_answer = input("Type client message : ")
cli_answer = cli_answer.encode()
cs.send(cli_answer)

cs.close()
