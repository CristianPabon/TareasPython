import socket
import threading

us = input("Nombre de usuario: ")

host = '186.84.22.129'
port = 36636

clientes = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientes.connect((host, port))

def recibir_msn():
  while True:
    try:
      msm = clientes.rcv(1024).decode('utf-8')

      if msm == "@usuario":
        clientes.send(us.encode('utf-8'))
      else:
        print(msm)
    except:
      print("Ha ocurrido un error")
      clientes.close
      break
def escribir_msn():
  while True:
    msm = f"{us}: {input('')}"
    clientes.send(message.encode('utf-8'))

receive_thread = threading.Thread(target = recibir_msn)
receive_thread.start()

write_thread = threading.Thread(target = escribir_msn)
write_thread.start()