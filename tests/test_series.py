from math_series.series import fibonacci
from math_series.series import lucas
def test_zero():
    actual= fibonacci(0)
    expected = 0
    assert actual== expected


def test_one():
    actual= fibonacci(1)
    expected = 1
    assert actual== expected
    
def test_six():
    actual= fibonacci(6)
    expected = 8
    assert actual== expected

def test_thirteen():
    actual= fibonacci(13)
    expected = 233
    assert actual== expected

def test_zero_lucas():
    actual= lucas(0)
    expected = 2
    assert actual== expected

def test_one_lucas():
    actual= lucas(1)
    expected = 1
    assert actual== expected

def test_four_lucas():
    actual= lucas(4)
    expected = 7
    assert actual== expected

def test_seven_lucas():
    actual= lucas(7)
    expected = 29
    assert actual== expected

