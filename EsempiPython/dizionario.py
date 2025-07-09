dizionario = {
    "nome": "Alice",
    "età": 30,
    "città": "Roma"
}

print(dizionario["nome"])  # Stampa: Alice
print(dizionario["età"])   # Stampa: 30
print(dizionario["città"]) # Stampa: Roma

dizionario["età"] = 31

print(dizionario) # stampa {'nome': 'Alice', 'età': 31, 'città': 'Roma'}

dizionario["email"] = "alice@darkai.com"

print(dizionario) # stampa {'nome': 'Alice', 'età': 31, 'città': 'Roma', 'email': 'alice@darkai.com'}

# Utilizzo di pop() per rimuovere un elemento
dizionario.pop("città")

print(dizionario)

# Utilizzo di del per rimuovere un elemento
del dizionario["email"]
print(dizionario)  # Stampa: {'nome': 'Alice', 'età': 31}

print(dizionario.keys()) # stampa dict_keys(['nome', 'età'])
print(dizionario.values()) # stampa dict_values(['Alice', 31])
print(dizionario.items()) # questo metodo che vedremo dopo serve per iterare con for il dizionario
