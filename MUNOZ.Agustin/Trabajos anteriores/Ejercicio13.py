ahorro=float(input("Ingrese sus ahorros iniciales: "))
ahorro1=ahorro+(ahorro*0.04)
ahorro2=ahorro1+(ahorro1*0.04)
ahorro3=ahorro2+(ahorro2*0.04)
print("Ahorros tras el primer año: " + str(round(ahorro1,2)))
print("Ahorros tras el segundo año: " + str(round(ahorro2,2)))
print("Ahorros tras el tercer año: " + str(round(ahorro3,2)))
