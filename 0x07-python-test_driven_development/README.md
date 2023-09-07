# Project: Python Test-Driven Development

## Background Context

This project is focused on learning Test-Driven Development (TDD) principles in Python. It includes several tasks designed to help you practice writing code with proper documentation and testing.

### Important Notice on Intranet Checks for Python Projects

Starting from today:

- Based on the requirements of each task, you should always write the documentation (module(s) + function(s)) and tests first, before you actually code anything.
- The intranet checks for Python projects won't be released before their first deadline, to encourage you to focus more on TDD and think about all possible cases.
- We strongly encourage you to work together on test cases to avoid missing any edge cases (but not in the implementation of them).
- Always think about all possible edge cases and do not trust the user.

## Resources

Read or watch:

- [doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html) (until "26.2.3.7. Warnings" included)
- [doctest – Testing through documentation](https://docs.python.org/3/library/doctest.html#what-are-doctests)
- [Unit Tests in Python](https://docs.python.org/3/library/unittest.html)
- [Unittest module](https://docs.python.org/3/library/unittest.html)
- [Interactive and Non-interactive tests](https://docs.python.org/3/library/doctest.html#what-are-doctests)

## Learning Objectives

By the end of this project, you should be able to explain to anyone, without the help of Google:

### General

- Why Python programming is awesome.
- What an interactive test is.
- Why tests are important.
- How to write Docstrings to create tests.
- How to write documentation for each module and function.
- What are the basic option flags to create tests.
- How to find edge cases.

## Copyright - Plagiarism

You are tasked to come up with solutions for the tasks below yourself to meet the above learning objectives. You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work. You are not allowed to publish any content of this project. Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs.
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/python3`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- Your code should use the `pycodestyle` (version 2.8.*).
- All your files must be executable.
- The length of your files will be tested using `wc`.

### Python Test Cases

- Allowed editors: vi, vim, emacs.
- All your files should end with a new line.
- All your test files should be inside a folder `tests`.
- All your test files should be text files (extension: `.txt`).
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`.
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
- All your functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`).
- A documentation is not a simple word, it's a real sentence explaining what's the purpose of the module, class, or method (the length of it will be verified).
- We strongly encourage you to work together on test cases to avoid missing any edge case – The Checker is checking for tests!

## Tasks

### 0. Integers Addition

Write a function that adds 2 integers.

- Prototype: `def add_integer(a, b=98):`
- `a` and `b` must be integers or floats, otherwise, raise a `TypeError` exception with the message `a must be an integer or b must be an integer`.
- `a` and `b` must be first casted to integers if they are float.
- Returns an integer: the addition of `a` and `b`.
- You are not allowed to import any module.

### 1. Divide a Matrix

Write a function that divides all elements of a matrix.

- Prototype: `def matrix_divided(matrix, div):`
- `matrix` must be a list of lists of integers or floats, otherwise, raise a `TypeError` exception with the message `matrix must be a matrix (list of lists) of integers/floats`.
- Each row of the matrix must be of the same size, otherwise, raise a `TypeError` exception with the message `Each row of the matrix must have the same size`.
- `div` must be a number (integer or float), otherwise, raise a `TypeError` exception with the message `div must be a number`.
- `div` can't be equal to 0, otherwise, raise a `ZeroDivisionError` exception with the message `division by zero`.
- All elements of the matrix should be divided by `div`, rounded to 2 decimal places.
- Returns a new matrix.
- You are not allowed to import any module.

### 2. Say My Name

Write a function that prints "My name is `<first_name> <last_name>`".

- Prototype: `def say_my_name(first_name, last_name=""):`
- `first_name` and `last_name` must be strings, otherwise, raise a `TypeError` exception with the message `first_name must be a string or last_name must be a string`.
- You are not allowed to import any module.

### 3. Print Square

Write a function that prints a square with the character `#`.

- Prototype: `def print_square(size):`
- `size` is the size length of the square.
- `size` must be an integer, otherwise, raise a `TypeError` exception with the message `size must be an integer`.
- If `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`.
- If `size` is a float and is less than 0, raise a `TypeError` exception with the message `size must be an integer`.
- You are not allowed to import any module.

### 4. Text Indentation

Write a function that prints a text with 2 new lines after each of these characters: `.`, `?`, and `:`.

- Prototype: `def text_indentation(text):`
- `text` must be a string, otherwise, raise a `TypeError` exception with the message `text must be a string`.
- There should be no space at the beginning or at the end of each printed line.
- You are not allowed to import any module.

### 5. Max Integer - Unittest

Write unittests for the function `def max_integer(list=[]):`.

- Your test file should be inside a folder `tests`.
- Use the `unittest` module.
- Your test file should be Python files (extension: `.py`).
- Your test file should be executed by using this command: `python3 -m unittest tests.6-max_integer_test`.
- All tests you make must be passable by the function below.

### 6. Matrix Multiplication

Write a function that multiplies 2 matrices.

- Prototype: `def matrix_mul(m_a, m_b):`
- `m_a` and `m_b` must be validated with specific requirements.
- If `m_a` and `m_b` can't be multiplied, raise a `ValueError` exception with the message `m_a and m_b can't be multiplied`.
- You are not allowed to import any module.

### 7. Lazy Matrix Multiplication

Write a function that multiplies 2 matrices by using the module NumPy.

- Prototype: `def lazy_matrix_mul(m_a, m_b):`
- Test cases should be the same as 100-matrix_mul but with new exception type/message.
- To install NumPy: `pip3 install numpy==1.15.0`.

### 8. CPython #3: Python Strings

Create a function that prints Python strings.

- Prototype: `void print_python_string(PyObject *p);`
- Format: see example.
- If `p` is not a valid string, print an error message.

## Author

KHALID


