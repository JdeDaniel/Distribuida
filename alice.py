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

print("Alice, ingresa tu clave secreta")
a = int(input("a: "))


# 3. Cálculo de claves públicas
A = pow(g, a, p)  # A = g^a mod p

print(f"Alice, tu clave pública es: {A}")

# 4. Intercambio de claves públicas (A y B viajan por el canal inseguro)
B=5 #Valor que Bob manda y Alice recibe 

# 5. Cálculo de la clave compartida
clave_alice = pow(B, a, p)  # (B^a) mod p

#Bob calcula su clave_bob y se la comparte a Alice
clave_bob=5

print(f"Clave compartida calculada por Alice: {clave_alice}")


# 6. Verificación
if clave_alice == clave_bob:
    print(f"\n Éxito. Clave secreta compartida: {clave_alice}")
else:
    print("\n Error: las claves no coinciden")
