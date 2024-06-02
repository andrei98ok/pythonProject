import pytest
from room_number import porch_and_floor


def test_porch_and_floor():
    assert porch_and_floor(1) == (1, 1)
    assert porch_and_floor(15) == (1, 4)
    assert porch_and_floor(21) == (2, 1)
    assert porch_and_floor(45) == (3, 2)

