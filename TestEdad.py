# -*- coding: utf8 -*-

import unittest

from Edad import Edad

class TestEdad(unittest.TestCase):

	def setUp(self):
		self.edad = Edad()

	def test_edad_menor_0(self):
		self.assertEqual(self.edad.checkEdad(-1),'No existes')

	def test_edad_menor_13(self):
		self.assertEqual(self.edad.checkEdad(12),'Eres un niño')

	def test_edad_menor_18(self):
		self.assertEqual(self.edad.checkEdad(17),'Eres joven')

	def test_edad_menor_65(self):
		self.assertEqual(self.edad.checkEdad(64),'Eres un adulto')

	def test_edad_menor_120(self):
		self.assertEqual(self.edad.checkEdad(110),'Eres un adulto mayor')
		
	def test_edad_mayor(self):
		self.assertEqual(self.edad.checkEdad(130), 'Eres Ammun-Ra')


if __name__ == '__main__':
	unittest.main()

