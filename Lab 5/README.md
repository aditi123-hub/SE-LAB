# Lab 5: Static Code Analysis — Dairy Milk Collection Ledger
Forked Repo Link-https://github.com/aditi123-hub/L5_26_dairy_collection
## Objective
To perform static code analysis on a Python program using Pylint, Bandit, and Flake8, identify code quality and security issues, and fix the reported issues.

## Tools Used
- **Pylint** — checks code quality, style, naming conventions, and documentation.
- **Bandit** — identifies potential security vulnerabilities in Python code.
- **Flake8** — checks Python code for style violations and formatting issues.

## Project Structure

```text
Lab 5/
├── dairy_collection.py
├── pylint_before.txt
├── pylint_final.txt
├── bandit_before.txt
├── bandit_final.txt
├── flake8_before.txt
├── flake8_final.txt
├── issues.md
├── reflection.md
└── README.md
```

## Procedure

1. Ran Pylint, Bandit, and Flake8 on the original Python program.
2. Saved the initial reports in the corresponding `*_before.txt` files.
3. Identified code quality, security, and formatting issues.
4. Modified the Python program to address the identified issues.
5. Ran all three tools again and saved the final reports.
6. Documented the issues and reflections in `issues.md` and `reflection.md`.

## Changes Made

- Added module and function docstrings.
- Improved function and variable naming conventions.
- Removed unused imports.
- Fixed line-length and formatting violations.
- Replaced SQL string construction with parameterized queries.
- Replaced MD5 hashing with SHA-256.
- Removed shell command execution and used Python's `print()` function instead.
- Corrected comparisons with `None`.

## Results

| Tool | Before | After |
|---|---|---|
| Pylint | 2.00/10 | 10.00/10 |
| Bandit | 3 reported issues | 0 reported issues |
| Flake8 | 7 violations | 0 violations |

## Deliverables

- `dairy_collection.py` — corrected Python source code.
- Before-and-after reports for Pylint, Bandit, and Flake8.
- `issues.md` — issues identified and fixes applied.
- `reflection.md` — reflection on the static analysis process.

## Conclusion

Static code analysis helped identify and resolve code quality, security, and formatting issues. After making the corrections, the program achieved a Pylint score of 10.00/10, with no issues reported by Bandit or Flake8.

