def saluta(nome, messaggio="Ciao"):
    print(f"{messaggio} {nome}!")

saluta("Alice", "Ciao") # Ciao Alice!
saluta("Bob", "Buongiorno") # Buongiorno Bob!

saluta(messaggio="Ciao", nome="Franco") # Ciao Franco!
saluta(nome="Ciro") # Ciao Ciro!
saluta("Piera") # Ciao Piera!