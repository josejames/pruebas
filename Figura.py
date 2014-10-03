class Figura():

	def rectangulo(self, lado, lado2):
		return lado*lado2

	def cuadrado(self, lado):
		return lado**2

	def triangulo(self, base, altura):
		return (base*altura)/2

	def circulo(self,radio):
		return 3.1416 * (radio**2)

	def poligono(self,per,apot):
		return (per*apot)/2
