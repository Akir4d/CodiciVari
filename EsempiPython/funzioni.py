def saluta(nome):
    # potevo scrivere saluto = "Ciao " + nome + "!"
    # man voglio provare una esemplificazione figa!
    saluto=f"Ciao {nome}!"
    return saluto

nome = input("Ciao come ti chiami? ")
messaggio = saluta(nome)
print(messaggio)