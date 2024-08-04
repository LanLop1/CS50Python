import pytest
from plates import is_valid

    
def test_largo():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("he4234") == True
    assert is_valid("H") == False
    assert is_valid("+`") == False

def test_inicio0():
    assert is_valid("he0234") == False
    assert is_valid("he3234") == True
    assert is_valid("HE3234") == True
    assert is_valid("+`") == False

def test_alphaAfterNumber():
    assert is_valid("he34ar") == False
    assert is_valid("he3234") == True
    assert is_valid("22") == False
    assert is_valid(" 2") == False
    assert is_valid('ABC123') == True
    assert is_valid("$1") == False
    assert is_valid("1$") == False
    assert is_valid("12$") == False
    assert is_valid("  AB") == False
    assert is_valid("!?AB2*") == False
    assert is_valid("*:") == False
    assert is_valid("B>") == False
    assert is_valid(".´`+") == False
    assert is_valid("23arc") == False
    assert is_valid('ABC.12') == False


def test_allAlpha():
    assert is_valid("hello") == True
    assert is_valid("+`") == False
    assert is_valid("hello, world") == False
