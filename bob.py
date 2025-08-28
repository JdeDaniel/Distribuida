#Bob

def pedirSecretoBob() -> int:
    print("Bob, ingresa tu clave secreta")
    b = int(input("b: "))
    return b


def clavePublicaBob(p: int, g: int, b: int) -> int:   
    B = pow(g, b, p)  # B = g^b mod p
    print(f"Bob, tu clave pública es: {B}")
    return B

def claveCompartidaBob(A: int, b: int, p: int) -> int:
    clave_compartida = pow(A, b, p)  # (B^a) mod p
    print(f"Tu clave compartida es: {clave_compartida}")
    return clave_compartida


