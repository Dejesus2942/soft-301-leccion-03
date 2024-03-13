PV = float(input("Ingresar precio de venta: "))
print("Ingrese N para  nacional o E para extrajero")
opcion = input()
if opcion == "N":
    TOTAL = PV + (PV * .08)
else:
    TOTAL = PV + (PV * .18)
print("El total es: " + str(TOTAL))
