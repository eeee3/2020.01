class dog:
    def __init__(self, name="", age=0, raza=""):
        self.name=name
        self.age=age
        self.raza=raza
    def __str__(self):
        return self.name + " " + str(self.age) + " " + self.raza
    
    def input(self):
        self.name=input("Ingrese el nombre: ")
        self.age=int(input("Ingresa la edad del perro: "))
        self.raza=input("Ingrese la raza del perro: ")

if __name__=="__main__":
    perro1=dog()
    perro2=dog("coso")
    
    print(perro1)
    print(perro2)
