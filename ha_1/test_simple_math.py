# pytest -v test_simple_math.py
# pytest --markers
# pytest -vm user_marker

import pytest
from simple_math import SimpleMath

@pytest.fixture
def simplemath():
    return SimpleMath()

@pytest.mark.parametrize("a, exp", [
    (2, 4),
    (0, 0),
    (1, 1),
    (-2, 4)
])
def test_square_po_muns(a, exp, simplemath):
    assert simplemath.square(a)  == exp

@pytest.mark.parametrize("a, exp", [
    (2, 8),
    (0, 0),
    (1, 1),
    (-2, -8),
])
def test_cube_po_muns(a, exp, simplemath):
    assert simplemath.cube(a)  == exp