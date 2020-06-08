inv = float(input("Ingrese la cantidad a invertir: "))
interes = float(input("Ingrese el interés porcentual anual: "))
anos = int(input("Ingrese la cantidad de años: "))
print("Capital final: " + str(round(inv * (interes/100+1)**anos, 2)))