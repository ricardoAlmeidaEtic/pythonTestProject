class Retangulo(object):
    def __init__(self,comprimento,largura) -> None:
        self.comprimento = comprimento
        self.largura = largura

    def calcArea(self) -> int:
        return (self.comprimento * self.largura)

    def calcPerimetro(self) -> int:
        return((self.comprimento*2)+(self.largura*2))    