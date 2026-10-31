# Lab 6 – Code and Branch Coverage Analysis

Repo Link-https://github.com/aditi123-hub/L6_L7_26_loan_eligibility/tree/main/Lab%206

## Aim
To perform code coverage and branch coverage analysis on a Loan Eligibility application using Python, Pytest, and Coverage.py.

## Objectives
- Understand code coverage and branch coverage.
- Write test cases to test different functions and conditions.
- Identify untested statements and branches.
- Achieve at least 90% code coverage and branch coverage.

## Project Structure

```text
Lab 6/
├── loan_eligibility.py
├── test_loan_eligibility.py
├── CodeCoverageTest_loan_eligibility.py
├── BranchCoverageTest_loan_eligibility.py
├── CodeCoverage_Screenshot.jpeg
├── BranchCoverage_Screenshot.jpeg
└── README.md
```

## Technologies Used
- Python 3.9.6
- Pytest
- Coverage.py

## Installation

Install the required packages:

```bash
pip install pytest coverage
```

## Part 1: Code Coverage Analysis

Run the code coverage tests:

```bash
python3 -m coverage erase
python3 -m coverage run --source=loan_eligibility -m pytest CodeCoverageTest_loan_eligibility.py
python3 -m coverage report -m
```

**Result:**
- Total test cases: 20
- Tests passed: 20
- Code coverage achieved: 100%

## Part 2: Branch Coverage Analysis

Run the branch coverage tests:

```bash
python3 -m coverage erase
python3 -m coverage run --branch --source=loan_eligibility -m pytest BranchCoverageTest_loan_eligibility.py
python3 -m coverage report -m
```

**Result:**
- Total test cases: 27
- Tests passed: 27
- Statement coverage: 100%
- Branch coverage: 100%

## Conclusion

Successfully performed code coverage and branch coverage analysis on the Loan Eligibility application. Test cases were written to cover different functions, conditions, and decision branches.

Achieved **100% code coverage and 100% branch coverage**, exceeding the required minimum of 90%.
