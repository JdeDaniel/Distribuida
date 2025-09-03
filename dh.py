from sympy import isprime
import alice
import bob
import random

def establecerParametros():

    while True:
        try:
            p = random.randint(5,20)
            if isprime(p):
                break
            else:
                print("Espere a que el numero primo se genere.")
        except ValueError:
            print("Error.")

    print(" ")

    while True:
        try:
            g = random.randint(1,p)
            if 1 < g < p :
                break
            else:
                print("Espere a que se genere g.")
        except ValueError:
            print("Error.")

    print(" ")
    print(f"Parámetros públicos establecidos: p = {p}, g = {g}")
    print(" ")
    return p,g


def clavesCorrectas() -> bool:
    p,g = establecerParametros()

    a = alice.pedirSecretoAlice()
    b = bob.pedirSecretoBob()
    print(" ")

    A = alice.clavePublicaAlice(p,g,a)
    B = bob.clavePublicaBob(p,g,b)
    print(" ")

    claveCompartidaAlice = alice.claveCompartidaAlice(B,a,p)
    claveCompartidaBob = bob.claveCompartidaBob(A,b,p)
    
    if claveCompartidaAlice == claveCompartidaBob:
        print("Éxito, las claves son iguales")
        return True
    else: 
        print("Fracaso, las claves son diferentes")
        return False





