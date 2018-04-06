class Rectangulo():
    base=0
    altura=0
    def __init__(self,x,y):
        self.base=x
        self.altura=y
    def superficie(self):
        return (self.base*self.altura)

x=Rectangulo(int(input('ingrese base: ')),int(input('ingrese altura: ')))

print(x.superficie())
