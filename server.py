#!/usr/bin/env python3
from threading import Thread
import socket
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224   
def ricevi_comandi(sock_service, addr_client):  
    print("\nConnessione ricevuta da " + str(addr_client))
    print("\nAspetto di ricevere i dati ")
    while True:
        dati = sock_service.recv(2048)#riceve i dati dal client
        if not dati:
            print("Fine dati dal client. Reset")
            break
        dati = dati.decode()#decodifica i dati in stringa da byte

        print("Ricevuto: '%s'" % dati)
        if dati=='ko':
            print("Chiudo la connessione con " + str(addr_client))
            break
        operazione, primo, secondo = dati.split(';')#split divide i dati che vengono ricevuti
        #serie di if per compiere l'operazione ricevuta
        if operazione == "piu" :
            risultato = int(primo) + int(secondo)
        if operazione == "meno" :
            risultato = int(primo) - int(secondo)
        if operazione == "per" :
            risultato = int(primo) * int(secondo)
        if operazione == "diviso" :
            risultato = int(primo) / int(secondo)
        dati = "il risultato dell'operazione: " + operazione + " tra "+ str(primo)+ " e "+ str(secondo)+ " è: "+ str(risultato)
        dati = dati.encode()#trasformiamo la soluzione in byte
        sock_service.send(dati)#inviamo i dati al client
    sock_service.close() #chiude il server       

def avvia_server(indirizzo, porta ):
    sock_listen = socket.socket()#crea la socket
    #operazione opzionale che riavvia subito il server
    sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #Associamo indirizzo e porta
    sock_listen.bind((indirizzo, porta))
    sock_listen.listen(5)
    print("Server in ascolto su %s." % str((indirizzo, porta)))
    ricevi_connessioni(sock_listen)
    
def ricevi_connessioni(sock_listen):
    while True:
        sock_service, addr_client = sock_listen.accept()
        print("\nConnessione ricevuta da %s " % str(addr_client))
        print("Creo un thread per servire le richieste")
        try:
            Thread(target=ricevi_comandi, args=(sock_service, addr_client)).start()
        except:
            print("il thread non si avvia")
            sock_listen.close()#chiude la comunicazione
if _name_ == '_main_':
    avvia_server(SERVER_ADDRESS,SERVER_PORT)


