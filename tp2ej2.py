class Circulo:
    radio=0
    def __init__(self, radio):
        self.radio=radio

    def area(self):
        from math import pi
        return (pi*(int(self.radio)**2))

    def perimetro(self):
        from math import pi
        return(2*pi*(int(self.radio)))

circulo=Circulo(5)
print(circulo.area())
print(circulo.perimetro())
