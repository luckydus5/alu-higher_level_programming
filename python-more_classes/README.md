📘 Python - More Classes and Objects

This project continues exploring Object-Oriented Programming (OOP) in Python, focusing on classes, instances, and special methods (__str__, __repr__, etc.).
All tasks revolve around building and improving a Rectangle class step by step.

🧩 Project Information

Repository: alu-higher_level_programming

Directory: python-more_classes

Language: Python 3

Style: Follows PEP8 guidelines

Modules Imported: 🚫 None allowed

📂 Files and Descriptions
File	Description
0-rectangle.py	Defines an empty class Rectangle.
1-rectangle.py	Defines a rectangle with private width and height attributes, including property getters and setters for validation.
2-rectangle.py	Adds public methods area() and perimeter() to compute rectangle area and perimeter.
3-rectangle.py	Adds __str__() to print the rectangle using the character #.
4-rectangle.py	Adds __repr__() to return a string that can recreate the rectangle using eval().
5-rectangle.py	Adds __del__() to print a message "Bye rectangle..." when an instance is deleted.
6-rectangle.py	Adds class attribute number_of_instances to count active rectangle instances.
7-rectangle.py	Adds class attribute print_symbol to change the symbol used for string representation.
8-rectangle.py	Adds static method bigger_or_equal(rect_1, rect_2) to compare rectangles by area.
9-rectangle.py	Adds class method square(cls, size=0) to create a square (same width and height).
🧠 Concepts Covered

Classes and instances in Python

Private vs. public attributes

Getters and setters using @property

Instance and class attributes

Special methods:

__init__ → object initialization

__str__ → informal string representation

__repr__ → official string representation

__del__ → object deletion

Static methods and class methods

Using eval() to recreate objects from their representation

⚙️ Example Usage
0-rectangle.py
$ ./0-main.py
<class '0-rectangle.Rectangle'>
{}

1-rectangle.py
$ ./1-main.py
{'_Rectangle__height': 4, '_Rectangle__width': 2}
{'_Rectangle__height': 3, '_Rectangle__width': 10}

2-rectangle.py
$ ./2-main.py
Area: 8 - Perimeter: 12
--
Area: 30 - Perimeter: 26

3-rectangle.py
$ ./3-main.py
##
##
##
##
<3-rectangle.Rectangle object at 0x...>

4-rectangle.py
$ ./4-main.py
##
##
##
##
Rectangle(2, 4)

5-rectangle.py
$ ./5-main.py
Area: 8 - Perimeter: 12
Bye rectangle...

6-rectangle.py
$ ./6-main.py
2 instances of Rectangle
Bye rectangle...
1 instances of Rectangle
Bye rectangle...
0 instances of Rectangle

7-rectangle.py
$ ./7-main.py
########
########
########
########
--
&&&&&&&&
&&&&&&&&
&&&&&&&&
&&&&&&&&
--

8-rectangle.py
$ ./8-main.py
my_rectangle_1 is bigger or equal to my_rectangle_2
my_rectangle_2 is bigger than my_rectangle_1
Bye rectangle...
Bye rectangle...

9-rectangle.py
$ ./9-main.py
Area: 25 - Perimeter: 20
#####
#####
#####
#####
#####
Bye rectangle...

🧾 Requirements

All files should start with #!/usr/bin/python3

Code must be PEP8 compliant

Each file must contain a docstring

No imports allowed

Each class should be tested with the provided main.py scripts

👨‍💻 Author

Olivier Dusabamahoro
📧 ALU Rwanda Student
💻 GitHub Repository: alu-higher_level_programming
