
class Pelicula:
    def __init__(self, codigo=0, titulo="", genero="", duracion=0):
        self.codigo= codigo
        self.titulo= titulo
        self.genero= genero
        self.duracion= duracion

    def input(self):

        self.codigo=int(input("Ingrese el código de la película: "))
        self.titulo=input("Ingrese el título de la película: ")
        self.genero=input("Ingrese el género de la película: ")
        self.duracion=int(input("Ingrese la duración de la película: "))

    def __str__(self):

        return "(%d) - %s (%s) (%d mins)" % (self.codigo, self.titulo, self.genero, self.duracion)


class PeliculasRepo:


    def __init__(self):

        self.peliculas = {}

    def add(self,pel):

        self.peliculas[pel.codigo]=pel

    def update(self, pel):

        self.peliculas[pel.codigo]=pel

    def delete(self,pel):

        del self.peliculas[pel.codigo]

    def find_all(self):

        lista_pel=[]
        for pelicula in self.peliculas.values():
            lista_pel.append(pelicula)
        return lista_pel

    def find_by_id(self, id_pel):

        return self.peliculas[id_pel]

    def __str__(self):
        string = ""
        for pelicula in self.find_all():
            string += pelicula.__str__()
        return string

if __name__ == "__main__":

    a = Pelicula()
    a.input()
    b= Pelicula()
    b.input()
    p = PeliculasRepo()
    p.add(a)
    p.add(b)
    print(p.__str__())
    



