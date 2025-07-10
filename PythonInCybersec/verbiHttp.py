import http.client

host = input("Inserire host/IP del sistema target: ")
# testiamo testphp.vulnweb.com 
# /index.php
# http://192.168.50.101/dav/
port = input("Inserire la porta del sistema target (default: 80): ")

if(port == ""): port = 80

try:
    # questo si collega al servizio http a una determinata porta
    # esiste HTTPSConnection che si collega HTTPS
    connection = http.client.HTTPConnection(host, port)
    # Chiediamo il metodo OPTIONS su link /
    connection.request("OPTIONS", "/dav/")
    # Quindi avviamo la connessione
    response = connection.getresponse()
    # quando risponde python salvera' tutto l'oggetto in repsonse
    # che quindi contiene lo stato della connessione
    # ma anche l'header e pure l'eventuale contenuto
    if response.status == 200:
        # dopo aver testato quello che stiamo cercando
        # print("Gli headers sono:\n", response.headers)
        print(f"I verbi attivi sono: {response.getheader('Allow')}")
    else:
        print("Non posso trovare i metodi perche' ho ricevuto il codice: ", response.status)
    connection.close()
except ConnectionRefusedError:
    print("Connessione Fallita")