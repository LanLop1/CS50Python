import pytest
import fuel
from fuel import convert, gauge


def test_Capital():
    assert convert("1/3") == 33
    assert convert("2/4") == 50


def test_gauge():
    assert gauge(99) == "F"
    assert gauge(32) == "32%"
    assert gauge(1) == "E"


def test_error():
    assert convert("") == ValueError
    assert convert("7/5") == ValueError
    assert convert("3/0") == ZeroDivisionError