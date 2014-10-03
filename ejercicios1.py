# -*- coding: utf8 -*-
"""
un vendedor recibe una comision de 10%

>>> comision(1000, 1000, 1000, 1000)
'1300.0, 300.0'

>>> comision(0, 0, 50, 100)
'15.0, 15.0'

>>> descuento(100)
85.0

>>> descuento(1000)
850.0

>>> calificacion(10,8,9)
9.0

>>> calificacion(6,8,10)
8.0

>>> peso(65)
'gramos: 65000.0 libras: 143.299 toneladas: 0.065'

>>> peso(78)
'gramos: 78000.0 libras: 171.9588 toneladas: 0.078'

>>> peso(1000)
'gramos: 1000000.0 libras: 2204.6 toneladas: 1.0'

>>> cardex(10,9,8)
'aprobado con 9.0'

>>> cardex(6,5,4)
'reprobado con 5.0'

>>> cardex(10,10,10)
'aprobado con 10.0'

>>> descuento2(9000.0)
'30 de descuento'

>>> descuento2(5000)
'20 de descuento'

>>> descuento2(2000)
'10 de descuento'

>>> cardex2(5,5,5)
'NA'

>>> cardex2(8,7,8)
'S'

>>> cardex2(8,9,8)
'B'

>>> vejez(44)
'joven'

>>> vejez(46)
'vieja'

>>> vejez(0)
'joven'

>>> altura(1.65)
'eres chaparro'

>>> altura(1.75)
'eres alto'

>>> altura(0)
'eres chaparro'

>>> check('abc')
'contrasena fallida'

>>> check('avas')
'contrasena fallida'

>>> check('solrac')
'contrasena valida'


"""


def check(p):
    if p == 'solrac':
        return 'contrasena valida'
    else:
        return 'contrasena fallida'


def altura(a):
    if a <= 1.65:
        return 'eres chaparro'
    else:
        return 'eres alto'


def vejez(edad):
    if edad < 45:
        return 'joven'
    else:
        return 'vieja'


def cardex2(a, b, c):
    promedio = (a + b + c) / 3.0
    if promedio < 6.0:
        return 'NA'
    elif promedio <= 8.0:
        return 'S'
    elif promedio <= 9.0:
        return 'B'
    else:
        return 'E'


def descuento2(m):
    if m > 5000:
        return '30 de descuento'
    elif m > 3000:
        return '20 de descuento'
    elif m > 1000:
        return '10 de descuento'
    else:
        return '0 de descuento'


def comision(base, v1, v2, v3):
    com = (v1 + v2 + v3) / 10.0
    total = base + com
    return "" + str(total) + ", " + str(com)


def descuento(n):
    return n * 0.85


def calificacion(e1, e2, e3):
    return (e1 + e2 + e3) / 3.0


def peso(kilos):
    g = kilos * 1000.0
    l = kilos * 2.2046
    t = kilos / 1000.0
    return 'gramos: {0} libras: {1} toneladas: {2}'.format(g, l, t)


def cardex(c1, c2, c3):
    promedio = (c1 + c2 + c3) / 3.0
    if promedio < 6.0:
        return 'reprobado con {0}'.format(promedio)
    else:
        return 'aprobado con {0}'.format(promedio)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
