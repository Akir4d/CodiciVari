# in python input riceve solo stringhe
# quindi occorre far il cast in intero per evitare ambiguita'
# il cast per l'intero e' int()
x = int(input("inserisci un numero: "))


if x < 10:
    print("il numero inserito e' minore di 10")
elif (x == 10):
    print("il numero inserito  e' uguale a 10")
else:
    print("il numero inserito e' maggiore di 10")



