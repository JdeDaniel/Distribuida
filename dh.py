from sympy import isprime

print("Algoritmo Diffie-Hellman")

def establecerParametros():

    while True:
        try:
            p = int(input("Ingrese el valor de p: "))
            if isprime(p):
                break
            else:
                print("Ingrese un numero primo.")
        except ValueError:
            print("Error. Ingrese un numero entero primo.")

    print(" ")

    while True:
        try:
            g = int(input("Ingrese el valor de g: "))
            if 1 < g < p :
                break
            else:
                print("Ingrese un numero entero mayor a 1 y menor a p.")
        except ValueError:
            print("Error. Ingrese un numero entero.")

    print(" ")
    print(f"Parámetros públicos establecidos: p = {p}, g = {g}")

