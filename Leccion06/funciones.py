def mi_funcion(nombre, apellido):
    print('saludos desde mi función')
    print(f'Nombre: {nombre}, Apellido: {apellido}')

mi_funcion('Juan', 'Perez')
mi_funcion('Karla','Lara')


def sumar(a=0, b=0):
    return a + b


resultado = sumar(5, 3)
#print(f'Resultado sumar: {resultado}')
print(f'Resultado sumar: {sumar(5,3)}')
