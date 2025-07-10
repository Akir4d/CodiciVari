import socket as so

# chiediamo all'utente informazioni
target = input("Inserisci l'indirizzo da scansire: ")
portrange = input("Inserisci un range di porte (es 5-200): ")

# portrange si aspetta un input che si 5-1024 
# di portrange prendo la prima porta usando split per generare 
# una list [porta_basso, porta_alta] e quindi prendere la porta bassa
lowport = int(portrange.split('-')[0])
# stessa cosa ma con la porta alta
highport = int(portrange.split('-')[1])

print(f"Scansisco host {target} dalla porta {lowport} alla porta {highport}")
porte_chiuse = []
# ora porta per porta le controlliamo tutte
for port in range(lowport, highport + 1): # [2,4,5,6,7...1024]
    # apriamo una connessione
    s = so.socket(so.AF_INET, so.SOCK_STREAM)
    # usiamo connect_ex che apre e chiude la connessione e restutisce solo lo stato
    status = s.connect_ex((target, port))
    # le connessione e' riuscita dara' 0
    if(status == 0):
        print(f"*** La porta {port} e' aperta ***")
    else:
        porte_chiuse.append(port)
        #print(f"La porta {port} e' chiusa!")
    s.close()
#print("porte chiuse", porte_chiuse)


