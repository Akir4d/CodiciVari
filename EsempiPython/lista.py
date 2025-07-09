lista = [1, "ciao", 3.14, [1, 2, 3]]
print(lista[0])  # Stampa: 1
print(lista[1])  # Stampa: ciao
print(lista[2])  # Stampa: 3.14
print(lista[3])  # Stampa: [1, 2, 3]
print(lista[3][0])  # Stampa: 1 (accesso al primo elemento della lista interna)

lista.pop()
print(lista)
## lista.remove(elemento da rimuovere)
lista.remove("ciao")
print(lista)

## lista.append() Mette un elemento alla fine
lista.append([1,2,3,6])
print(lista)

## lista.insert(elemento dopo quale inserire, elemento nuovo)
lista.insert(2,"ciao")
print(lista)

## se preferite rimuovere un elemento per posizione
del lista[2]
print(lista)

## se ovviamente vogliamo sovrascivere un elemento della lista
lista[0] = "Franco"
print(lista)