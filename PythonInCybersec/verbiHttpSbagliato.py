import http.client

host = input("Inserire host/IP del sistema taget: ")
# testphp.vulnweb.com
port = input("Inserire la porta del sistema target (default: 80): ")

if(port == ""): port = 80

try:
    connection = http.client.HTTPConnection(host, port)
    connection.request("OPTIONS", "/")
    response = connection.getresponse()
    print("I metodi abilitati sono: ", response.status)
    connection.close()
except ConnectionRefusedError:
    print("Connessione Fallita")