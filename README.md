# phase-3-week-1-code-challenge
This repository contains solutions and test scripts for three coding challenges. Each challenge has its own set of requirements and corresponding tests.

# Challenge 1: Converting 12-hour Time to 24-hour Time

Converting a 12-hour time like "8:30 am" or "8:30 pm" to 24-hour time (like "0830" or "2030").

- Input: `hour` (1 to 12), `minute` (0 to 59), `period` ("am" or "pm")
- Output: Four-digit string representing time in 24-hour format

To test the solution, run:

```bash
pytest test_challenge1.py

# Challenge 2: Exactly Two Positive Numbers
Determine if exactly two out of three integers are positive.

Input: a, b, c (integers)
Output: True if exactly two of the three integers are positive, False otherwise
To test the solution, run:
pytest test_challenge2.py

# Challenge 3: Highest Value of Consonant Substrings
Find the highest value of consonant substrings in a lowercase string.

Consonants: Any letters except "aeiou" (a = 1, b = 2, ..., z = 26)
Output: Highest value among the consonant substrings
To test the solution, run:
pytest test_challenge3.py

# Running the Tests
Make sure you have Python and pytest installed. If not, you can install pytest using:
pip install pytest

# Yusra Mohamed 