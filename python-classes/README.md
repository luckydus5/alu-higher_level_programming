0x06. Python - Classes and Objects
📘 Description

This project introduces Object-Oriented Programming (OOP) concepts in Python. You will learn how to define classes, create objects, and understand the difference between attributes, methods, and properties. The project covers fundamental principles such as encapsulation, abstraction, and information hiding — the core of OOP design.

🎯 Learning Objectives

By the end of this project, you should be able to explain the following concepts clearly, without the help of Google:

General

Why Python programming is awesome

What is OOP (Object-Oriented Programming)

What does “first-class everything” mean in Python

What is a class

What is an object or instance

Difference between a class and an object/instance

What is an attribute

The purpose and usage of public, protected, and private attributes

What is self and why it’s used

What is a method

What is the special __init__ method and how to use it

Concepts of Data Abstraction, Data Encapsulation, and Information Hiding

What is a property

The difference between an attribute and a property in Python

The Pythonic way to write getters and setters

How to dynamically create new attributes for existing instances of a class

How to bind attributes to objects and classes

What is the __dict__ of a class and/or instance, and what it contains

How Python finds the attributes of an object or class

How to use the built-in getattr() function

📚 Resources

Read or watch the following materials before starting the project:

Object-Oriented Programming (until “Inheritance” excluded)

Object-Oriented Programming in Python 3

Properties vs. Getters and Setters

Learn to Program 9: Object-Oriented Programming (YouTube)

Python Classes and Objects (Official Documentation)

Object-Oriented Programming Concepts

⚠️ Note: Some examples in the resources show how not to write code — read carefully to understand best practices.

⚙️ Requirements
General

Allowed editors: vi, vim, emacs

All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5

All files must end with a new line

The first line of all files must be:

#!/usr/bin/python3


A README.md file at the root of the project folder is mandatory

Your code should follow the pycodestyle (version 2.7.*) style guide

All files must be executable

The length of your files will be tested using wc

Each module, class, and function must contain a proper docstring explaining its purpose

📝 Documentation Rules

Documentation must be a real sentence describing the purpose of the code, not just a word or phrase.

Use the Google Style for docstrings. Example:

def my_function(param1, param2):
    """Calculate and return the sum of two numbers.

    Args:
        param1 (int): The first number.
        param2 (int): The second number.

    Returns:
        int: The sum of both numbers.
    """

🧱 Example Project Structure
0-square.py
1-square.py
2-square.py
3-square.py
4-square.py
5-square.py
6-square.py
README.md

💡 Example

File: 0-square.py

#!/usr/bin/python3
"""Defines an empty class Square."""

class Square:
    """An empty class that defines a square."""
    pass


Usage:

guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

guillaume@ubuntu:~/$ ./0-main.py
<class '0-square.Square'>
{}

🧠 Author

Olivier Dusabamahoro
📧 ALU Student — Foundations Program
💻 Project: Python - Classes and Objects
