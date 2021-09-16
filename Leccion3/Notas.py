nota = int(input('Proporciona la nota con un valor entre 0 y 10: '))
mensaje = None
if 9 <= nota <= 10:
    mensaje = 'Nota A'
elif  8 <= nota < 9:
    mensaje = 'Nota B'
elif  7 <= nota < 8:
    mensaje = 'Nota C'
elif  6 <= nota < 7:
    mensaje = 'Nota D'
elif  0 <= nota < 6:
    mensaje = 'Nota F'
else:
    mensaje = 'Valor desconocido'
print(f'Tu nota es: {nota}, {mensaje}')