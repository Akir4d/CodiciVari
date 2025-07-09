
x = "Hello, World"

print(x.split(sep=",")) # stampa ['Hello', ' World']
print(x.upper()) # stampa HELLO, WORLD

y = "this is Python"

print(x + " " +y) # stampa Hello, World this is Pyhon


vett=x.split(sep=",")
print(vett[0]+vett[1].strip()) # stampa HelloWorld