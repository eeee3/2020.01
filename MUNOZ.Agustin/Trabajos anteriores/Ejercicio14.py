numpan=int(input("Ingrese la cantidad de pan no-fresco vendido en el día: "))
pan1=3.49
pan2=round(3.49-(3.49*0.6),2)
prec1=pan1*numpan
prec2=pan2*numpan
desc=prec1-prec2
print("El precio habitual sería de "+str(round(prec1,2)))
print("El descuento es de "+str(round(desc,2)))
print("El precio final es de "+str(round(prec2,2)))