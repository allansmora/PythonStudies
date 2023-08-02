'''
beecrowd | 1012
Área
'''

def areaTriangulo(base,altura):
    area = (base*altura)/2
    print(f"TRIANGULO: {area:.3f}")
def areaCirculo(raio):
    area = 3.14159*raio**2
    print(f"CIRCULO: {area:.3f}")
def areaTrapezio(baseMaior, baseMenor,altura):
    area = ((baseMaior+baseMenor)*altura)/2
    print(f"TRAPEZIO: {area:.3f}")
def areaQuadrado(lado):
    area = lado**2
    print(f"QUADRADO: {area:.3f}")
def areaRetangulo(ladoA,ladoB):
    area= ladoA*ladoB
    print(f"RETANGULO: {area:.3f}")
a,b,c = input().split(" ")
a = float(a)
b = float(b)
c = float(c)

areaTriangulo(a,c)
areaCirculo(c)
areaTrapezio(a,b,c)
areaQuadrado(b)
areaRetangulo(a,b)