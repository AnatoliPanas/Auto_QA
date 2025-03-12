import pytest
from calculator import Calculator

cal = Calculator()

@pytest.fixture
def calculator():
    return Calculator()

# тестируем метод sum

res = cal.sum(4, 6)
assert res == 10, 'результат не совпал'

res1 = cal.sum(-4, -2)
assert res1 == -6, 'результат не совпал'

res2 = cal.avg([1,2,3])
assert res2 == 2, 'результат не совпал'

@pytest.mark.parametrize("a, b, exp", [
    (4, 5, 9),
    (0, 0, 0),
    (-1, 1, 0),
    (2.5, 3.5, 6.0),
])
def test_sum_po_muns(a, b, exp, calculator):
    assert calculator.sum(a,b)  == exp