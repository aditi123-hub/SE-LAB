# Lab 5: Static Code Analysis — Reflection

## 1. What is static code analysis, and why is it useful?

Static code analysis examines source code without executing its normal functionality. It helps identify potential bugs, security vulnerabilities, and coding-style problems early. In this lab, Pylint, Bandit, and Flake8 helped identify different categories of issues in the dairy collection program.

## 2. What did Pylint, Bandit, and Flake8 detect?

Pylint detected code-quality problems such as missing docstrings, inconsistent function naming, an unused import, and an ambiguous variable name. Bandit detected potentially unsafe SQL construction, weak MD5 hashing, and shell command execution. Flake8 identified formatting violations, long lines, an ambiguous variable name, and an incorrect comparison with None.

## 3. What changes did you make, and how did they improve the program?

I added documentation, renamed functions to follow snake_case, removed the unused import, and corrected formatting. I replaced SQL string construction with parameterized queries, replaced MD5 with SHA-256, and removed the shell invocation from the printing function. These changes improved readability and addressed the reported security risks. I also reran the program to check that the dairy collection calculations and output remained correct.

## 4. What did you learn from this lab?

I learned that different static analysis tools identify different types of problems and that using them together gives broader coverage. The initial Pylint score was 2.00/10, while the final score was 10.00/10. Bandit initially reported three security findings and reported no issues after the fixes. Flake8 initially reported seven violations and produced no output after the fixes. I learned that it is important to inspect warnings, make appropriate changes, and rerun the tools to verify the results.
