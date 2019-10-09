import socket
import pymsgbox

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1500))
pymsgbox.alert('Server Started at port : %d' %(1500))
s.listen(20)

while True:
    conn,addr = s.accept()
    pymsgbox.alert(f'Client connected : {addr} ')
    conn.send(1)