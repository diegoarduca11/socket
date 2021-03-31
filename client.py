#!/usr/bin/env python3

import socket     #importo la libreria socket

SERVER_ADDRESS = '127.0.0.1'   
SERVER_PORT = 22224

sock_service = socket.socket()  #socket di servizio

sock_service.connect((SERVER_ADDRESS, SERVER_PORT))  #la socket service riceve i dati che invia il cliente.L'accettazione è su 2 porte differenti

print("Client connesso a  " + str((SERVER_ADDRESS, SERVER_PORT)))
protocollo = ["SYN", "SYN ACK","ACK with Data","ACK for Data"]
step=0
dati = str(step)
while True:
   dati = dati.endcode()
   sock_service.send(dati)
   print("Invio: "+ str(step)+ " - " + protocollo[step])
   dati = sock_service.recv(2048)
   if not dati:
      print("Server non risponde. Exit")
      break
   dati=dati.decode()
   if dati == '3':
      print("ricevuto: "+dati+ " - " +protocollo[int(dati)])
      print("Termino connessione")
      break
   else:
      step = int(dati)
      print("ricevuto: "+str(step)+ " - " +protocollo[step])
       dati:str
      dati = str(step)
sock_service.close()
