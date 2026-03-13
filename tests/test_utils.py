import sys
import os
import pytest

sys.path.append(os.path.abspath("src"))

from app.utils import add, clean_text


def test_add():
    assert add(1, 2) == 3


def test_add_negative():
    assert add(-1, 1) == 0


def test_clean_text_basic():
    assert clean_text(" Hello ") == "hello"


@pytest.mark.parametrize(
    "text, expected",
    [
        (" Hi ", "hi"),
        ("WORLD", "world"),
        ("  PyThOn  ", "python"),
    ],
)
def test_clean_text_parametrize(text, expected):
    assert clean_text(text) == expected
