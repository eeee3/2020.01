
class Persona:
    def __init__(self,nombre):
        self.nombre = nombre
    def __str__(self):
        return self.nombre

nombres = ["Héctor","Mario","Marta"]
personas = []

for n in nombres:
    p = Persona(n)
    personas.append(p)


import pickle
f = open('personas.pck','wb')
pickle.dump(personas, f)
f.close()


f = open('personas.pck','rb')
personas = pickle.load(f)
f.close()
 
for p in personas:
    print(p)