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

@pytest.mark.parametrize("arg1, arg2, res", [
    (4, 5, 9),
    (0, 0, 0),
    (-1, 1, 0),
    (2.5, 3.5, 6.0),
])
def test_sum_pos_muns(arg1, arg2, res, calculator):
    assert calculator.sum(arg1, arg2)  == res

@pytest.mark.skipif(condition="sys.version_info < (3, 13)", reason="Требуется Python 3.12")
def test_div_by_zero(calculator):
    with pytest.raises(ArithmeticError, match="На ноль делить нельзя"):
        calculator.div(10,0)


@pytest.mark.skip(reason="тест отключен")
def test_mul_pos_muns(calculator):
    print("ddffdf")
    assert calculator.sum(2,2)  == 4

@pytest.mark.user_marker
def test_sub_pos_muns(calculator):
    assert calculator.sub(4,2)  == 2