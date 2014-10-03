# -*- coding: utf8 -*-

class Edad():

	def checkEdad(self,edad):
		if edad < 0:
			return 'No existes'
		elif edad < 13:
			return 'Eres un niño'
		elif edad < 18:
			return 'Eres joven'
		elif edad < 65:
			return 'Eres un adulto'
		elif edad < 120:
			return 'Eres un adulto mayor'
		else:
			return 'Eres Ammun-Ra'
