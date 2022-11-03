import pytest
from app.digit_match import digit_match

def test_digit_match_large_inputs():
    apples = 1072503891
    oranges = 62530841

    assert digit_match(apples, oranges) == 4


def test_digit_match_no_matches():
    apples = 0
    oranges = 62530841

    assert digit_match(apples, oranges) == 0


def test_digit_match_clustered_matches():
    apples = 841
    oranges = 62530841

    assert digit_match(apples, oranges) == 3


def test_digit_match_single_digits():
    apples = 0
    oranges = 0

    assert digit_match(apples, oranges) == 1


def test_digit_match_small_inputs():
    apples = 10
    oranges = 20

    assert digit_match(apples, oranges) == 1
