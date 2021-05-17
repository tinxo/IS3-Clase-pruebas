from app.calculos import suma
import pytest

def test_suma():
    assert suma(2,5) == 7

@pytest.mark.parametrize(
    "valor_a, valor_b, resultado",
    [
        (2,3,5),
        (3,2,5),
        (suma(3,2),5,10),
        (3,suma(2,5),10),
    ]
)
def test_suma_parametrizada(valor_a, valor_b, resultado):
    assert suma(valor_a, valor_b) == resultado