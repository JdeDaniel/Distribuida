print("Algoritmo Diffie-Hellman")

# 1. Parámetros públicos
# p = 23        # número primo (debe ser muy grande)
#g = 5         # generador

p = int(input("p: "))
g = int(input("g: "))


print(f"Parámetros públicos: p = {p}, g = {g}")

# 2. Claves privadas (secretas)
#a = 6   # Secreto de Alice
#b = 15  # Secreto de Bob

print("Alice, ingresa tu clave secreta")
a = int(input("a: "))

print("Bob, ingresa tu clave secreta")
b = int(input("b: "))


# 3. Cálculo de claves públicas
A = pow(g, a, p)  # A = g^a mod p
B = pow(g, b, p)  # B = g^b mod p

print(f"Clave pública de Alice: {A}")
print(f"Clave pública de Bob: {B}")

# 4. Intercambio de claves públicas (A y B viajan por el canal inseguro)

# 5. Cálculo de la clave compartida
clave_alice = pow(B, a, p)  # (B^a) mod p
clave_bob   = pow(A, b, p)  # (A^b) mod p

print(f"Clave compartida calculada por Alice: {clave_alice}")
print(f"Clave compartida calculada por Bob:   {clave_bob}")

# 6. Verificación
if clave_alice == clave_bob:
    print(f"\n Éxito. Clave secreta compartida: {clave_alice}")
else:
    print("\n Error: las claves no coinciden")
