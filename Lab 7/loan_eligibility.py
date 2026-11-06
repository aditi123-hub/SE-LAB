
CATEGORIES = {
    "P": "Individual",
    "C": "Company",
    "H": "HUF",
    "F": "Firm"
}


def parse_income(income):
    try:
        if not isinstance(income, str):
            return None

        income = income.strip().replace(',', '')

        if not income or not income.isdigit():
            return None

        return int(income)

    except (ValueError, AttributeError):
        return None


def monthly_emi(details):
    try:
        if not isinstance(details, str):
            return None

        parts = details.split(',')

        if len(parts) != 3:
            return None

        principal, rate, years = [int(x.strip()) for x in parts]

        if principal <= 0 or rate < 0 or years <= 0:
            return None

        r = rate / 1200
        n = years * 12

        # Handle zero-interest loans separately
        if r == 0:
            return round(principal / n, 2)

        emi = principal * r * (1 + r) ** n / ((1 + r) ** n - 1)

        return round(emi, 2)

    except (ValueError, TypeError, AttributeError, OverflowError):
        return None


def pan_category(pan):
    try:
        if not isinstance(pan, str):
            return None

        pan = pan.strip().upper()

        if len(pan) != 10:
            return None

        category = pan[3]

        return CATEGORIES.get(category)

    except (TypeError, IndexError):
        return None


def main():
    print("==== Running parse_income ====")
    user_input = input("Enter monthly income (e.g. 50,000): ")
    result = parse_income(user_input)
    print("Income:", result)

    print("\n==== Running monthly_emi ====")
    user_input = input("Enter principal,rate,years (e.g. 500000,10,5): ")
    result = monthly_emi(user_input)
    print("Monthly EMI:", result)

    print("\n==== Running pan_category ====")
    user_input = input("Enter a PAN number (e.g. ABCPE1234F): ")
    result = pan_category(user_input)
    print("PAN Category:", result)


if __name__ == "__main__":
    main()
