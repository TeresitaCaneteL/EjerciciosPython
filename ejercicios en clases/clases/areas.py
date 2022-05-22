class Poligono:
    """
    Define un polígono según su base y su altura.
    """
    def __init__(self, b, h):
        self.b = b
        self.h = h

class Rectangulo(Poligono):

    def area(self):
        return self.b * self.h

class Triangulo(Poligono):

    def area(self):
        return (self.b * self.h) / 2
base=int(input('ingrese base: '))
altura=int(input('ingrese altura: '))
rectangulo = Rectangulo(base, altura)
triangulo = Triangulo(base, altura)

print("Área del rectángulo: ", rectangulo.area())
print("Área del triángulo:", triangulo.area())