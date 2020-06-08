def transformar_numero():
    letra1=input("Ingrese una letra: ")
    letra2=input("Ingrese otra letra: ")
    letra3=input("Ingrese la última letra: ")
    num1=int(input("Ingrese un número: "))
    bin1=""
    while num1 // 2!=0:
        bin1=str(num1%2)+bin1
        num1=num1//2
    num2=int(input("Ingrese otro número: "))
    bin2=""
    while num2 // 2!=0:
        bin2=str(num2%2)+bin2
        num2=num2//2
    print("La primer letra es: ",bin(ord(letra1)))
    print("La segunda letra es: ",bin(ord(letra2)))
    print("La tercer letra es: ",bin(ord(letra3)))
    print("El primer numero es: "+str(num1)+bin1)
    print("El segundo numero es: "+str(num2)+bin2)

transformar_numero()

