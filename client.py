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
   try:
        dati = input("Inserisci i dati da inviare (0 per terminare la connessione): ") #richiesta di un input 
    except EOFError:
        print("\nOkay. Exit")
        break
    if not dati:
        print("Non puoi inviare una stringa vuota!") #controllo
        continue
    if dati == '0':
        print("Chiudo la connessione con il server!") #chiusura del server
        break
    
    dati = dati.encode()

    sock_service.send(dati)

    dati = sock_service.recv(2048)
sock_service.close()
