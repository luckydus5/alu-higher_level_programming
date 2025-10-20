# Python Hello World Project

## Description
This project contains exercises to learn the basics of Python programming.  
It covers running Python scripts, printing, string manipulation, and using f-strings.

---

## Exercises

### 0. Run Python file
**Mandatory**  
Write a Shell script that runs a Python script. The Python file name is stored in the environment variable `$PYFILE`.

**Example:**
```bash
cat main.py
#!/usr/bin/python3
print("Best School")

export PYFILE=main.py
./0-run
# Output:
Best School
Repo:

Directory: python-hello_world

File: 0-run

1. Run inline
Mandatory
Write a Shell script that runs Python code stored in the environment variable $PYCODE.

Example:

bash
Copy code
export PYCODE='print(f"Best School: {88+10}")'
./1-run_inline
# Output:
Best School: 98
Repo:

Directory: python-hello_world

File: 1-run_inline

2. Hello, print
Mandatory
Write a Python script that prints exactly:

css
Copy code
"Programming is like building a multilingual puzzle
File: 2-print.py

3. Print integer
Mandatory
Complete the source code to print the integer stored in variable number, followed by "Battery street", using f-strings.
Do not cast the variable to a string. File must be 3 lines long.

Example:

bash
Copy code
./3-print_number.py
# Output:
98 Battery street
File: 3-print_number.py

4. Print float
Mandatory
Complete the source code to print the float stored in variable number with 2 digits precision using f-strings.
Do not cast the variable to a string.

Example:

bash
Copy code
./4-print_float.py
# Output:
Float: 3.14
File: 4-print_float.py

5. Print string
Mandatory
Print 3 times the value of a string variable str, followed by its first 9 characters.
Do not use loops or conditionals. Maximum 5 lines.

Example:

bash
Copy code
./5-print_string.py
# Output:
Holberton SchoolHolberton SchoolHolberton School
Holberton
File: 5-print_string.py

6. Play with strings
Mandatory
Complete the source code to print:

css
Copy code
Welcome to Holberton School!
Use the variables str1 and str2.
No loops or conditionals. File must be 5 lines long.

Example:

bash
Copy code
./6-concat.py
# Output:
Welcome to Holberton School!
File: 6-concat.py

7. Copy - Cut - Paste
Mandatory
Complete the source code to manipulate variable word:

word_first_3 → first 3 letters

word_last_2 → last 2 letters

middle_word → value of word without first and last letters

No loops or conditionals. File must be 8 lines long.

Example:

bash
Copy code
./7-edges.py
# Output:
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
File: 7-edges.py

8. Create a new sentence
Mandatory
Complete the source code to print:

csharp
Copy code
object-oriented programming with Python
Do not create new variables or use string literals. No loops or conditionals. File must be 5 lines long.

Example:

bash
Copy code
./8-concat_edges.py
# Output:
object-oriented programming with Python
File: 8-concat_edges.py

9. Easter Egg
Mandatory
Write a Python script that prints “The Zen of Python” by Tim Peters.
File must be maximum 98 characters long (wc -m 9-easter_egg.py).

Example:

bash
Copy code
./9-easter_egg.py
# Output:
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
File: 9-easter_egg.py

Notes
All Python files must start with:

bash
Copy code
#!/usr/bin/python3
All scripts must be executable:

bash
Copy code
chmod +x filename.py
Follow PEP 8 style guide using pycodestyle.

Python 3.8+ is required.

yaml
Copy code

---

If you want, I can also make a **super-short version** with just the exercise number, title, and file name — perfect for quick browsing inside `vim`.  

Do you want me to make that too?
