
import pytest
from loan_eligibility import credit_band, is_eligible, interest_rate


# ---------------- CREDIT BAND TESTS ----------------

def test_invalid_score_below_300():
    with pytest.raises(ValueError):
        credit_band(299)


def test_invalid_score_above_900():
    with pytest.raises(ValueError):
        credit_band(901)


def test_excellent_band():
    assert credit_band(750) == "excellent"


def test_good_band():
    assert credit_band(650) == "good"


def test_fair_band():
    assert credit_band(550) == "fair"


def test_poor_band():
    assert credit_band(300) == "poor"


# ---------------- LOAN ELIGIBILITY TESTS ----------------

def test_unknown_employment():
    with pytest.raises(ValueError):
        is_eligible(30, 50000, "unemployed", 800)


def test_age_below_minimum():
    assert is_eligible(20, 50000, "salaried", 800) is False


def test_age_above_maximum():
    assert is_eligible(61, 50000, "salaried", 800) is False


def test_salaried_income_below_minimum():
    assert is_eligible(30, 20000, "salaried", 800) is False


def test_self_employed_income_below_minimum():
    assert is_eligible(30, 30000, "self_employed", 800) is False


def test_poor_credit_score():
    assert is_eligible(30, 50000, "salaried", 500) is False


def test_self_employed_eligible():
    assert is_eligible(30, 50000, "self_employed", 800) is True


# ---------------- INTEREST RATE TESTS ----------------

def test_excellent_interest_rate():
    assert interest_rate(800, "salaried", False) == 8


def test_good_interest_rate():
    assert interest_rate(700, "salaried", False) == 10


def test_fair_interest_rate():
    assert interest_rate(600, "salaried", False) == 13


def test_poor_interest_rate():
    assert interest_rate(500, "salaried", False) == 13


def test_self_employed_interest_rate():
    assert interest_rate(800, "self_employed", False) == 9


def test_interest_rate_with_collateral():
    assert interest_rate(800, "salaried", True) == 6


def test_interest_rate_with_self_employment_and_collateral():
    assert interest_rate(800, "self_employed", True) == 7
