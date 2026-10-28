# Static Code Analysis — Issue Documentation

| Issue | Type | Line(s) in Original File | Description | Fix Approach |
|---|---|---|---|---|
| Unsafe shell execution (B605) | Security — High | 31 | `os.system()` passed the farmer name to a shell command, creating a command-injection risk. | Replaced the shell command with a direct `print()` call. |
| Weak MD5 hash (B324) | Security — High | 16 | MD5 is unsuitable for security-sensitive hashing. | Replaced MD5 with SHA-256. The result is a digest, not an authentication token by itself. |
| SQL injection risk (B608) | Security — Medium | 11 | SQL values were inserted using string formatting, allowing potentially unsafe query construction. | Used parameterized SQL with placeholders and a tuple of values. |
| Missing module docstring (C0114) | Code quality | 1 | The module did not explain its purpose. | Added a module-level docstring. |
| Missing function docstrings (C0116) | Code quality | 10, 15, 19, 24, 30, 34, 39 | Functions lacked descriptions. | Added descriptive docstrings. |
| Non-snake-case function names (C0103) | Naming/style | 10, 15, 19, 24, 30, 34 | Function names did not follow Python naming conventions. | Renamed functions and updated their calls. |
| Shadowed connection parameter (W0621) | Code quality | 10, 19, 24, 34 | Function parameters named `conn` shadowed the global connection variable. | Renamed the parameters to `connection`. |
| Unused import (F401/W0611) | Style/code quality | 2 | The `json` module was imported but never used. | Removed the unused import. |
| Long lines (C0301/E501) | Style | 7, 11, 20, 25 | Several lines exceeded the configured length limits. | Split long statements across multiple lines. |
| Ambiguous variable name (E741) | Style | 26 | The variable `l` was difficult to distinguish from the number 1. | Renamed it to `top_farmer_row`. |
| Incorrect None comparison (C0121/E711) | Style/code quality | 36 | The code used `fat == None`. | Changed the check to `fat is None`. |
| Old-style string formatting (C0209) | Code quality | 11 | The SQL statement used `.format()` to construct a query. | Replaced string construction with parameterized SQL. |
| Excess blank lines (E303) | Style | 34, 40, 58, 64 | Too many blank lines separated top-level definitions. | Adjusted spacing to follow Python style conventions. |

## Verification

- Original Pylint score: 2.00/10
- Final Pylint score: 10.00/10
- Original Bandit findings: 3 (2 High, 1 Medium)
- Final Bandit findings: 0
- Original Flake8 findings: 7
- Final Flake8 findings: 0
