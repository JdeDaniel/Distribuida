from sympy import isprime

print("Algoritmo Diffie-Hellman")

# 1. Parámetros públicos

#Comprobacion de p como numero primo usando isprime

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

#Comprobacion de 1<g<p
while True:
    try:
        g = int(input("Ingrese el valor de g: "))
        if g>1 and g<p:
            break
        else:
            print("Ingrese un numero entero mayor a 1 y menor a p.")
    except ValueError:
        print("Error. Ingrese un numero entero.")

print(" ")

print(f"Parámetros públicos establecidos: p = {p}, g = {g}")

# 2. Claves privadas (secretas)

print("Bob, ingresa tu clave secreta")
b = int(input("b: "))


# 3. Cálculo de claves públicas
B = pow(g, b, p)  # B = g^b mod p

print(f"Bob, tu clave pública es: {B}")

# 4. Intercambio de claves públicas (A y B viajan por el canal inseguro)
A=5 #Valor que Alice manda y Bob recibe 

# 5. Cálculo de la clave compartida
clave_bob   = pow(A, b, p)  # (A^b) mod p

#Alice calcula su clave_alice y se la comparte a Bob
clave_alice=5

print(f"Clave compartida calculada por Bob:   {clave_bob}")

# 6. Verificación
if clave_alice == clave_bob:
    print(f"\n Éxito. Clave secreta compartida: {clave_bob}")
else:
    print("\n Error: las claves no coinciden")
