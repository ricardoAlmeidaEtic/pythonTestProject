import unittest

class RetanguloTest(unittest.TestCase):
    def setUp(self) -> None:
        self.retangle = Retangulo(comprimento = 5,largura = 7)

    def test_calculate_area(self):

        area = self.retangle.calcArea()

        self.assertEqual(area,35)

    def test_calculate_perimeter(self):
        perimeter = self.retangle.calcPerimetro()

        assert perimeter == 24

class Retangulo(object):
    comprimento = 0
    largura = 0

    def __init__(self,comprimento,largura) -> None:
        self.comprimento = comprimento
        self.largura = largura

    def calcArea(self):
        return (self.comprimento * self.largura)

    def calcPerimetro(self):
        return((self.comprimento*2)+(self.largura*2))
        
    def setValues(self,comprimento,largura):
        if comprimento > 0 and largura > 0:
            self.comprimento = comprimento
            self.largura = largura
        else:
            print("Os valores introduzidos tem de ser maiores que zero.")
            exit()

        



if __name__ == "__main__":
    unittest.main()
        
#criar um objeto que represente um retangulo