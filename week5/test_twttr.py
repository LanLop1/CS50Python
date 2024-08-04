import pytest
from twttr import shorten


def test_Capital():
    assert shorten("PATETO") == "PTT"
    assert shorten("PUPIL") == "PPL"


def test_lower_case():
    assert shorten("pateto") == "ptt"
    assert shorten("pupil") == "ppl"


def test_blank():
    assert shorten("") == ""