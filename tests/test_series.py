from math_series import __version__

from math_series.series import fibonacci

from math_series.series import lucas


def test_version():
    assert __version__ == '0.1.0'


def test_one():
    actual = fibonacci(9)
    expected = 21
    assert actual == expected

def test_two():
    actual = fibonacci(0)
    expected = "error"
    assert actual == expected



def test_three():
    actual = fibonacci(10)
    expected = 34
    assert actual == expected


def test_four():
    actual = lucas(5)
    expected = 11
    assert actual == expected


def test_five():
    actual = lucas(16)
    expected = 2207
    assert actual == expected


def test_six():
    actual = lucas(11)
    expected = 199
    assert actual == expected