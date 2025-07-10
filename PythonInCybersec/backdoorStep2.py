import socket as so
import os, subprocess

# socket, ha bisogno di una tupla contenete (ip dove fare il bind, e porta)
SRV_ADDR = "10.0.2.15"
SRV_PORT = 44445

# Creaimo un oggetto che ci faccia gestire la connessione
# AF_INET e' ipv4, mentre SOCK_STREAM e' tcp, curiosita' SOCK_DGRAM e' udp
s = so.socket(so.AF_INET, so.SOCK_STREAM)
# configuriamo questo oggetto in modo che si faccia riservare l'accoppiata ip:port
# bind ha bisogno di una tupla (ip,porta)
s.bind((SRV_ADDR,SRV_PORT))
# Spieghiamo che deve entrare in ascolto
# listen(numero_connessioni_accettate)
s.listen(1)
# Ora attiaviamo la connessione vera ma prima avvisiamo l'utente che stiamo avviando la connessione
print("Server Avviato! Sono in attesa di connessione ...")
# con accept il codice si fermera' fino a che qualcuno non si collega
# accept ha come return una tupla (oggetto_della_connessione, ip_della_macchina_che_si_e'_connessa)
# Esiste un modo piu' efficente in python per fare questo
# tc = s.accept()
# connection = tc[0]
# address = tc[1]
# si chiama destrutturazione dei dati, ovvero se ho una lista o una tupla posso divere i valori
# su piu' variabili con una sintesi davvero intuitiva
connection, address = s.accept()
print(f"Qualcuno si e' connesso dall'indirizzo {address[0]} usando la porta {address[1]}")
# e ora sfruttiamo connection che in pratica sta dialogando col client

while True: 
       # ottengo la directory corrente
       cartella = os.getcwd()
       # Facciamo un prompt simile al terminale linux
       prompt = f"{cartella} $ "
       # lo invio al client
       connection.sendall(prompt.encode())
       # mi metto in ascolto della risposta
       data = connection.recv(1024)
       # ora traformiamo data in un comando comprensibile dal terminale in utf-8 e puliamo da \n con strip 
       comandi = data.decode('utf-8').strip().split(" ")
       # cerchiamo il comando coma cd ls etc
       comando = comandi[0]
       if comando == "cd":
              # la directory e' il secondo argomento
              os.chdir(comandi[1])
       else:
              # possiamo ora inviare il comando al sistema
              risposta = subprocess.run(comandi, capture_output=True, text=True)
       # se il client non sta dialogando o ha interrotto la connessione
       # devo uscire dal ciclo
       if not data: break
       # se invece ha inviato dati diamo feedback al client inviando una risposta
       connection.sendall(risposta.stdout.encode())
       # stampiamo quello che il client ci ha inviato
       print(data.decode('utf-8'))
# alla fine del ciclo dobbiamo chiudere la connessione
connection.close()
