📘 Python - Import & Modules
🧑‍💻 Author

By: Guillaume
Project Duration: Oct 13, 2025 → Oct 17, 2025
Weight: 1

🎯 Learning Objectives

At the end of this project, you should be able to explain to anyone, without using Google:

General

Why Python programming is awesome

How to import functions from another file

How to use imported functions

How to create a module

How to use the built-in function dir()

How to prevent code from executing when imported using

if __name__ == "__main__":


How to use command line arguments with your Python programs

⚙️ Requirements
General

Allowed editors: vi, vim, emacs

Files will be compiled/interpreted on Ubuntu 20.04 LTS using Python 3.8.5

All files must end with a new line

The first line of every file should be:

#!/usr/bin/python3


All files must be executable

Code must follow pycodestyle (version 2.7.*)

A README.md file at the root of your project folder is mandatory

The length of files will be tested using wc

📂 Project Structure
alu-higher_level_programming/
└── python-import_modules/
    ├── 0-add.py
    ├── 1-calculation.py
    ├── 2-args.py
    ├── 3-infinite_add.py
    ├── 4-hidden_discovery.py
    ├── 5-variable_load.py
    ├── add_0.py
    ├── calculator_1.py
    ├── variable_load_5.py
    └── README.md

🧩 Tasks Overview
0. Import a simple function from a simple file

Import the function add(a, b) from add_0.py and print 1 + 2 = 3.

✅ Example:

1 + 2 = 3

1. My first toolbox!

Import functions from calculator_1.py and perform addition, subtraction, multiplication, and division.

✅ Example:

10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2

2. How to make a script dynamic!

Print the number of command-line arguments and list them.

✅ Example:

$ ./2-args.py Hello World
2 arguments:
1: Hello
2: World

3. Infinite addition

Add all command-line integer arguments and print the total.

✅ Example:

$ ./3-infinite_add.py 10 20 -5
25

4. Who are you?

Print all names defined by hidden_4.pyc, excluding those starting with __.

✅ Example:

my_secret_santa
print_hidden
print_school

5. Everything can be imported

Import variable a from variable_load_5.py and print its value.

✅ Example:

98

🧠 Key Concepts Covered

import and module usage

Using sys.argv for command-line arguments

Filtering names with dir()

Conditional main execution (if __name__ == "__main__":)

Modular and reusable Python code

🧾 Example Command
chmod +x 0-add.py
./0-add.py

🏁 End of Project

You are now able to:

Reuse and import functions/modules

Write clean, organized, and modular Python programs

Understand how Python manages module execution
