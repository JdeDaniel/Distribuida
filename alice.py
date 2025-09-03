#Alice
import random

def pedirSecretoAlice() -> int:
    print("Alice, generando clave secreta")
    a  = random.randint(1,100)
    print(f"Alice, tu clave secreta es (a): {a}")
    return a

def clavePublicaAlice(p: int, g: int, a: int) -> int:
    print("Alice esta haciendo los calculos")
    x = g^a
    print(f"g^a = {x}") 
    A = pow(g, a, p)  # B = g^b mod p
    print(f"g^a mod p = {A}")
    print(f"Alice, tu clave pública es: {A}")
    print(" ")
    return A

def claveCompartidaAlice(B: int, a: int, p: int) -> int:
    print("Alice esta haciendo los calculos")
    x = B^a
    print(f"B^a = {x}")
    clave_compartida = pow(B, a, p)  # (B^a) mod p
    print(f"B^a mod p = {clave_compartida}")
    print(f"Alice, tu clave compartida es: {clave_compartida}")
    print(" ")
    return clave_compartida


