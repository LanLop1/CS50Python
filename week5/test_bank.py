import pytest
from bank import value


def test_h():
    assert value("h") == 20
    assert value("H") == 20


def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hello world") == 0


def test_random():
    assert value("jadi") == 100
    assert value("pupil") == 100
    assert value("Whats up?") == 100