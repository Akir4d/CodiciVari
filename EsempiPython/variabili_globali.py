variabile_globale = 30
def modifica_globale():
    global variabile_globale
    variabile_globale = 40
    # print(f"ho processato: {variabile_globale}")

print(variabile_globale)  # Stampa: 30
modifica_globale()
print(variabile_globale)  # Stampa: 40
