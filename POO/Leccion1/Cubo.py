class Cubo:
    def __init__(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.altura * self.profundidad

ancho = int(input('Proporciona el ancho: '))
altura = int(input('Proporciona el alto: '))
profundidad = int(input('Proporciona al profundidad: '))

cubo = Cubo(ancho, altura, profundidad)
print(f'Volumen cubo: {cubo.calcular_volumen()}')
