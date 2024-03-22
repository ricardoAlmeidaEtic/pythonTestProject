import pytest
from exec3v2 import Retangulo

@pytest.mark.parametrize(
    argnames ="a,b,result",
    argvalues = [
        (10,10,100)
    ]
)
def test_calcArea(a,b,result):
    assert Retangulo(a,b).calcArea() is result