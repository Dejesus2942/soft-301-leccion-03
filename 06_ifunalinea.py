# pedir dos numeros
# A y B
A = int(input("Ingrese el numero 01: "))
B = int(input("Ingrese el numero 02: "))
M = A if A > B else B
print("El mayor es: " + str(M))

A = int(input("Ingrese el valor de A: "))
R = A % 2
print("Par") if R == 0 else print("Impar")