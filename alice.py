#Alice

def pedirSecretoAlice() -> int:
    print("Alice, ingresa tu clave secreta")
    a = int(input("a: "))
    return a

def clavePublicaAlice(p: int, g: int, a: int) -> int:   
    A = pow(g, a, p)  # B = g^b mod p
    print(f"Alice, tu clave pública es: {A}")
    return A

def claveCompartidaAlice(B: int, a: int, p: int) -> int:
    clave_compartida = pow(B, a, p)  # (B^a) mod p
    print(f"Alicia, tu clave compartida es: {clave_compartida}")
    return clave_compartida


