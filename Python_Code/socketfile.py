import socket
def debugMsg(msg):
  # Use this function if you need any debug messages
  with open("/tmp/userdebug.log", "a") as myfile:
    myfile.write(msg + "\n")

    
file = open("/tmp/aliensignallog.txt", "w")


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('localhost',10000))
socket.listen(10)
       

while True:
  connection, address = socket.accept()
  data = connection.recv(1024)
  if len(data) > 0:
    print("Received: "+data)
    connection.close()
    break
    
file = open("/tmp/aliensignallog.txt", "w")
file.write(data)
file.close()
