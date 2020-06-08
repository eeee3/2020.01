def cpu():
    num1=input("Ingrese 5 numeros binarios, ya sean 0 o 1: ")[:5]
    if num1[0]=="0" and num1[1]=="0" and num1[2]=="0":
        if num1[3]=="1" and num1[4]=="1": 
            print("El resultado de ", num1[3], " + ", num1[4], "es: 10")
        if num1[3]=="0" and num1[4]=="0":
            print("El resultado de ", num1[3], " + ", num1[4], "es: 00")
        if num1[3]=="1" and num1[4]=="0":
            print("El resultado de ", num1[3], " + ", num1[4], "es: 01")
        if num1[3]=="0" and num1[4]=="1":
            print("El resultado de ", num1[3], " + ", num1[4], "es: 01")
 

    if num1[0]=="0" and num1[1]=="0" and num1[2]=="1":
        if num1[3]=="1" and num1[4]=="1":
            print("El resultado de ", num1[3], " - ", num1[4], "es: 00") 
        if num1[3]=="0" and num1[4]=="0": 
            print("El resultado de ", num1[3], " + ", num1[4], "es: 00")
        if num1[3]=="0" and num1[4]=="1":
            print("El resultado de ", num1[3], " + ", num1[4], "es: -01")
        if num1[3]=="1" and num1[4]=="0":
            print("El resultado de ", num1[3], " + ", num1[4], "es: 01")


    if num1[0]=="0" and num1[1]=="1" and num1[2]=="0":
        if num1[3]=="1" and num1[4]=="1":
            print("El resultado de ", num1[3], " * ", num1[4], "es : 01")
        if num1[3]=="0" and num1[4]=="0":
            print("El resultado de ", num1[3], " * ", num1[4], "es : 00")
        if num1[3]=="0" and num1[4]=="1":
            print("El resultado de ", num1[3], " * ", num1[4], "es : 00")
        if num1[3]=="1" and num1[4]=="0":
            print("El resultado de ", num1[3], " * ", num1[4], "es : 00")

    if num1[0]=="0" and num1[1]=="1" and num1[2]=="1":
        if num1[3]=="1" and num1[4]=="1":
            print("El resultado de ", num1[3], " / ", num1[4], "es de: 01")
        if num1[3]=="0" and num1[4]=="0":
            print("El resultado de ", num1[3], " / ", num1[4], "es de: 00")
        if num1[3]=="1" and num1[4]=="0":
            print("El resultado de ", num1[3], " / ", num1[4], "es de: 00")
        if num1[3]=="0" and num1[4]=="1":
            print("El resultado de ", num1[3], " / ", num1[4], "es de: 00")

    if num1[0]=="1" and num1[1]=="0" and num1[2]=="0":
        if num1[3]=="1" and num1[4]=="1":
            print("El resultado de ", num1[3], " and ", num1[4], "es de: 01")
        if num1[3]=="0" and num1[4]=="0":
            print("El resultado de ", num1[3], " and ", num1[4], "es de: 00")
        if num1[3]=="1" and num1[4]=="0":
            print("El resultado de ", num1[3], " and ", num1[4], "es de: 00")
        if num1[3]=="0" and num1[4]=="1":
            print("El resultado de ", num1[3], " and ", num1[4], "es de: 00")

    if num1[0]=="1" and num1[1]=="0" and num1[2]=="1":
        if num1[3]=="1" and num1[4]=="1":
            print("El resultado de ", num1[3], " or ", num1[4], "es de: 01")
        if num1[3]=="0" and num1[4]=="0":
            print("El resultado de ", num1[3], " or ", num1[4], "es de: 00")
        if num1[3]=="1" and num1[4]=="0":
            print("El resultado de ", num1[3], " or ", num1[4], "es de: 01")
        if num1[3]=="0" and num1[4]=="1":
            print("El resultado de ", num1[3], " or ", num1[4], "es de: 01")

    if num1[0]=="1" and num1[1]=="1" and num1[2]=="0":
        if num1[3]=="1" and num1[4]=="1":
            print("El resultado de ", num1[3], " not ", num1[4], "es de: 00")
        if num1[3]=="0" and num1[4]=="0":
            print("El resultado de ", num1[3], " not ", num1[4], "es de: 01")
        if num1[3]=="1" and num1[4]=="0":
            print("El resultado de ", num1[3], " not ", num1[4], "es de: 01")
        if num1[3]=="0" and num1[4]=="1":
            print("El resultado de ", num1[3], " not ", num1[4], "es de: 01")
  
cpu()