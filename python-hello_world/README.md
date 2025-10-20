# Python Hello World Project

## Description
This project introduces the basics of Python programming:
- Running Python scripts and inline code
- Printing text, integers, floats, and strings
- String manipulation and slicing
- Using f-strings

All exercises follow **PEP 8 style** and use Python 3.

---

## Exercises and How to Solve Them

### 0. Run Python file
**Mandatory**  
**Objective:** Run a Python script using a Shell script.  
- The Python file name is stored in the environment variable `$PYFILE`.  
- Use `python3 "$PYFILE"` to execute it.

**Solution (0-run):**
```bash
#!/bin/bash
python3 "$PYFILE"
1. Run inline
Mandatory
Objective: Run Python code stored in an environment variable $PYCODE.

Use python3 -c "$PYCODE" to execute the code string.

Solution (1-run_inline):

bash
Copy code
#!/bin/bash
python3 -c "$PYCODE"
2. Hello, print
Mandatory
Objective: Print a specific string.

Use the print() function.

Include quotes as required.

Solution (2-print.py):

python
Copy code
#!/usr/bin/python3
print('"Programming is like building a multilingual puzzle')
3. Print integer
Mandatory
Objective: Print an integer variable followed by text using f-strings.

Variable number holds the integer.

Do not cast the number to a string.

File must be 3 lines long.

Solution (3-print_number.py):

python
Copy code
#!/usr/bin/python3
number = 98
print(f"{number} Battery street")
4. Print float
Mandatory
Objective: Print a float with 2 digits of precision.

Variable number holds the float.

Format using f-strings: {number:.2f}.

Do not cast the number to a string.

Solution (4-print_float.py):

python
Copy code
#!/usr/bin/python3
number = 3.14159
print(f"Float: {number:.2f}")
5. Print string
Mandatory
Objective: Print a string 3 times and its first 9 characters.

Use string multiplication: str * 3.

Use slicing: str[:9].

No loops or conditionals. Max 5 lines.

Solution (5-print_string.py):

python
Copy code
#!/usr/bin/python3
str = "Holberton School"
print(str * 3)
print(str[:9])
6. Play with strings
Mandatory
Objective: Print Welcome to Holberton School! using variables.

Concatenate variables: str1 + str2.

No loops, conditionals, or extra variables.

File must be 5 lines.

Solution (6-concat.py):

python
Copy code
#!/usr/bin/python3
str1 = "Welcome to "
str2 = "Holberton School!"
print(str1 + str2)
7. Copy - Cut - Paste
Mandatory
Objective: Slice a string variable into parts.

word_first_3 → first 3 letters: word[:3]

word_last_2 → last 2 letters: word[-2:]

middle_word → everything except first and last: word[1:-1]

File must be 8 lines, no loops/conditionals.

Solution (7-edges.py):

python
Copy code
#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
8. Create a new sentence
Mandatory
Objective: Print object-oriented programming with Python using only existing variables.

Do not create new variables or use string literals.

File must be 5 lines, no loops/conditionals.

Solution (8-concat_edges.py):

python
Copy code
#!/usr/bin/python3
str1 = "object-oriented"
str2 = " programming with Python"
print(str1 + str2)
9. Easter Egg
Mandatory
Objective: Print “The Zen of Python” by Tim Peters.

Use import this.

Keep file ≤ 98 characters.

Solution (9-easter_egg.py):

python
Copy code
#!/usr/bin/python3
import this
Notes
All Python files must start with:

bash
Copy code
#!/usr/bin/python3
Make scripts executable:

bash
Copy code
chmod +x filename.py
Follow PEP 8 style using pycodestyle.

Python 3.8+ is required.
