#Bob
import random

def pedirSecretoBob() -> int:
    print("Bob, generando clave secreta")
    b = random.randint(1,100)
    print(f"Bob tu clave secreta es (b): {b}")
    return b

def clavePublicaBob(p: int, g: int, b: int) -> int:  
    print("Bob esta haciendo los calculos")
    x = g^b
    print(f"g^b = {x}")
    B = pow(g, b, p)  # B = g^b mod p
    print(f"g^b mod p = {B}")
    print(f"Bob, tu clave pública es: {B}")
    print(" ")
    return B

def claveCompartidaBob(A: int, b: int, p: int) -> int:
    print("Bob esta haciendo los calculos")
    x = A^b
    print(f"A^b = {x}")
    clave_compartida = pow(A, b, p)  # (B^a) mod p
    print(f"A^b mod p = {clave_compartida}")
    print(f"Bob, tu clave compartida es: {clave_compartida}")
    print(" ")
    return clave_compartida


