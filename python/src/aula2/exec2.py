import unittest
import math

class CirculoTest(unittest.TestCase):
    def setUp(self) -> None:
        self.circle = Circulo(raio = 6)

    def test_calculate_area(self):

        area = self.circle.calcArea()

        self.assertEqual(round(area,1),113.1)

    def test_calculate_perimeter(self):
        perimeter = self.circle.calcPerimetro()

        assert round(perimeter,3) == 37.699

class Circulo(object):

    def __init__(self,raio) -> None:
        self.raio = raio
        self.diametro = raio*2

    def calcArea(self):
        return math.pi*(self.raio * self.raio)

    def calcPerimetro(self):
        return self.diametro*math.pi

if __name__ == "__main__":
    unittest.main()
        
#criar um objeto que represente um retangulo