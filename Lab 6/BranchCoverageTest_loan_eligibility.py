
import pytest
from loan_eligibility import credit_band, is_eligible, interest_rate


# ---------------- CREDIT BAND BRANCH TESTS ----------------

def test_score_below_300():
    with pytest.raises(ValueError):
        credit_band(299)


def test_score_above_900():
    with pytest.raises(ValueError):
        credit_band(901)


def test_score_at_lower_valid_boundary():
    assert credit_band(300) == "poor"


def test_score_at_upper_valid_boundary():
    assert credit_band(900) == "excellent"


def test_excellent_branch():
    assert credit_band(750) == "excellent"


def test_good_branch():
    assert credit_band(650) == "good"


def test_fair_branch():
    assert credit_band(550) == "fair"


def test_poor_branch():
    assert credit_band(500) == "poor"


# ---------------- ELIGIBILITY BRANCH TESTS ----------------

def test_unknown_employment_branch():
    with pytest.raises(ValueError):
        is_eligible(30, 50000, "unemployed", 800)


def test_age_below_21():
    assert is_eligible(20, 50000, "salaried", 800) is False


def test_age_above_60():
    assert is_eligible(61, 50000, "salaried", 800) is False


def test_valid_age_boundary_21():
    assert is_eligible(21, 50000, "salaried", 800) is True


def test_valid_age_boundary_60():
    assert is_eligible(60, 50000, "salaried", 800) is True


def test_salaried_income_below_minimum():
    assert is_eligible(30, 20000, "salaried", 800) is False


def test_salaried_income_at_minimum():
    assert is_eligible(30, 25000, "salaried", 800) is True


def test_self_employed_income_below_minimum():
    assert is_eligible(30, 30000, "self_employed", 800) is False


def test_self_employed_income_at_minimum():
    assert is_eligible(30, 40000, "self_employed", 800) is True


def test_poor_credit_rejected():
    assert is_eligible(30, 50000, "salaried", 500) is False


def test_non_poor_credit_accepted():
    assert is_eligible(30, 50000, "salaried", 550) is True


# ---------------- INTEREST RATE BRANCH TESTS ----------------

def test_excellent_rate():
    assert interest_rate(800, "salaried", False) == 8


def test_good_rate():
    assert interest_rate(700, "salaried", False) == 10


def test_other_rate():
    assert interest_rate(600, "salaried", False) == 13


def test_self_employed_rate_adjustment():
    assert interest_rate(800, "self_employed", False) == 9


def test_salaried_rate_without_adjustment():
    assert interest_rate(800, "salaried", False) == 8


def test_collateral_reduces_rate():
    assert interest_rate(800, "salaried", True) == 6


def test_no_collateral_adjustment():
    assert interest_rate(800, "salaried", False) == 8


def test_self_employed_with_collateral():
    assert interest_rate(800, "self_employed", True) == 7
