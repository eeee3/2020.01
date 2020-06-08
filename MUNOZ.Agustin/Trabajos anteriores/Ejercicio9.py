peso=input("Ingrese su peso: ")
estatura=input("Ingrese su estatura: ")
imc=round(float(peso)/(float(estatura))**2,2)
print("Tu imc es de " + str(imc))