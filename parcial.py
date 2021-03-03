# Punto1
llantas = int(input('Digite la cantidad de llantas '))
if llantas < 5:
    precio = llantas * 300
    print(f'El total a pagar es de: ${precio}')
elif llantas >= 5 and llantas <= 10:
    precio = llantas * 250
    print(f'El total a pagar es de: ${precio}')
else:
    precio = llantas * 200
    print(f'El total a pagar es de: ${precio}')
# Punto2
tvs = float(input('Digite la cantidad de televisores a comprar '))
precio = float(input('Digite el precio de los televisores '))
cedula = int(input('Digite el numero de la cedula '))
c = str(cedula)[-2:]
print(f'Los ultimos digitos de su cedula son: {c}')
total = tvs * precio
if c == "01":
    desc = total * 0.10
    res = total - desc
    print(f'El total a pagar es de : ${res}')
elif c == "25":
    desc = total * 0.20
    res = total - desc
    print(f'El total a pagar es de : ${res}')
elif c == "44":
    desc = total * 0.35
    res = total - desc
    print(f'El total a pagar es de : ${res}')
elif c == "57":
    desc = total * 0.50
    res = total - desc
    print(f'El total a pagar es de : ${res}')
else:
    print('No tiene descuento, el total es : ${total}')

# Punto3
precio = float(input('Digite el precio de los colchones '))
cantidad = int(input('Digite la cantidad de colchones a comprar '))
total = precio * cantidad
print(f'El monto es de: ${total}')
if cantidad < 3:
    print(f'El total a pagar es: ${total}')
elif cantidad >= 3 and cantidad < 6:
    desc = total * 0.20
    res = total - desc
    print(f'El total a pagar con descuento del 20% es: ${res} ')
elif cantidad >= 6 and cantidad < 8:
    desc = total * 0.25
    res = total - desc
    print(f'El total a pagar con descuento del 25% es: ${res} ')
else:
    desc = total * 0.30
    res = total - desc
    print(f'El total a pagar con descuento del 30% es: ${res} ')

# Punto4
estudiantes = float(input('Digite la cantidad de estudiantes '))
if estudiantes < 20:
    porc = estudiantes * 0.50
    print(f'Se tomara {porc} estudiantes')
elif estudiantes >= 20 and estudiantes <= 30:
    porc = estudiantes * 0.60
    print(f'Se tomara {porc} estudiantes')
else:
    porc = estudiantes * 0.70
    print(f'Se tomara {porc} estudiantes')

