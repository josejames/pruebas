# -*- coding: utf8 -*-
"""
	Segun la edad muestra un mensaje

>>> ciclo_de_vida(0)
'No existes'

>>> ciclo_de_vida(12)
'Eres niño'

>>> ciclo_de_vida(17)
'Eres adolescente'

>>> ciclo_de_vida(19)
'Eres adulto'

>>> ciclo_de_vida(67)
'Eres adulto mayor'

>>> ciclo_de_vida(123)
'Eres Munn-Ra'
"""
def ciclo_de_vida(edad):
	if edad<=0:
		return 'No existes'
	elif edad < 13:
		print "'Eres niño'"
	elif edad < 18:
		return 'Eres adolescente'
	elif edad < 65:
		return 'Eres adulto'
	elif edad < 120:
		return 'Eres adulto mayor'
	else:
		return 'Eres Munn-Ra'
