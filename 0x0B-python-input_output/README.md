# Python Input/Output Project

This project contains a series of Python tasks related to input and output operations. Each task is described below along with the requirements and expected behavior.

## Table of Contents

1. [Read File](#1-read-file)
2. [Write to a File](#2-write-to-a-file)
3. [Append to a File](#3-append-to-a-file)
4. [To JSON String](#4-to-json-string)
5. [From JSON String to Object](#5-from-json-string-to-object)
6. [Save Object to a File](#6-save-object-to-a-file)
7. [Create Object from a JSON File](#7-create-object-from-a-json-file)
8. [Class to JSON](#8-class-to-json)
9. [Student to JSON](#9-student-to-json)
10. [Student to JSON with Filter](#10-student-to-json-with-filter)
11. [Student to Disk and Reload](#11-student-to-disk-and-reload)
12. [Pascal's Triangle](#12-pascals-triangle)
13. [Search and Update](#13-search-and-update)
14. [Log Parsing](#14-log-parsing)

## 1. Read File

- **Task:** Write a function that reads a text file (UTF8) and prints it to stdout.
- **Prototype:** `def read_file(filename=""):`
- Must use the `with` statement.
- Don't need to manage file permission or file doesn't exist exceptions.
- Not allowed to import any module.
- No test cases needed.
- **File:** `0-read_file.py`

## 2. Write to a File

- **Task:** Write a function that writes a string to a text file (UTF8) and returns the number of characters written.
- **Prototype:** `def write_file(filename="", text=""):`
- Must use the `with` statement.
- Don't need to manage file permission exceptions.
- Function should create the file if it doesn't exist.
- Function should overwrite the content of the file if it already exists.
- Not allowed to import any module.
- No test cases needed.
- **File:** `1-write_file.py`

## 3. Append to a File

- **Task:** Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added.
- **Prototype:** `def append_write(filename="", text=""):`
- If the file doesn’t exist, it should be created.
- Must use the `with` statement.
- Don't need to manage file permission or file doesn't exist exceptions.
- Not allowed to import any module.
- No test cases needed.
- **File:** `2-append_write.py`

## 4. To JSON String

- **Task:** Write a function that returns the JSON representation of an object (string).
- **Prototype:** `def to_json_string(my_obj):`
- Don’t need to manage exceptions if the object can’t be serialized.
- No test cases needed.
- **File:** `3-to_json_string.py`

## 5. From JSON String to Object

- **Task:** Write a function that returns an object (Python data structure) represented by a JSON string.
- **Prototype:** `def from_json_string(my_str):`
- Don’t need to manage exceptions if the JSON string doesn’t represent an object.
- No test cases needed.
- **File:** `4-from_json_string.py`

## 6. Save Object to a File

- **Task:** Write a function that writes an Object to a text file, using a JSON representation.
- **Prototype:** `def save_to_json_file(my_obj, filename):`
- Must use the `with` statement.
- Don’t need to manage exceptions if the object can’t be serialized.
- Don’t need to manage file permission exceptions.
- No test cases needed.
- **File:** `5-save_to_json_file.py`

## 7. Create Object from a JSON File

- **Task:** Write a function that creates an Object from a “JSON file.”
- **Prototype:** `def load_from_json_file(filename):`
- Must use the `with` statement.
- Don’t need to manage exceptions if the JSON string doesn’t represent an object.
- Don’t need to manage file permissions / exceptions.
- No test cases needed.
- **File:** `6-load_from_json_file.py`

## 8. Class to JSON

- **Task:** Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer, and boolean) for JSON serialization of an object.
- **Prototype:** `def class_to_json(obj):`
- `obj` is an instance of a Class.
- All attributes of the `obj` Class are serializable: list, dictionary, string, integer, and boolean.
- Not allowed to import any module.
- No test cases needed.
- **File:** `8-class_to_json.py`

## 9. Student to JSON

- **Task:** Write a class `Student` that defines a student by:
  - Public instance attributes: `first_name`, `last_name`, `age`.
  - Instantiation with `first_name`, `last_name`, and `age`: `def __init__(self, first_name, last_name, age):`
  - Public method `def to_json(self):` that retrieves a dictionary representation of a `Student` instance.
  - You are not allowed to import any module.
- No test cases needed.
- **File:** `9-student.py`

## 10. Student to JSON with Filter

- **Task:** Extend the `Student` class from Task 9 with the following:
  - Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance.
  - If `attrs` is a list of strings, only attribute names contained in this list must be retrieved.
  - Otherwise, all attributes must be retrieved.
  - You are not allowed to import any module.
- No test cases needed.
- **File:** `10-student.py`

## 11. Student to Disk and Reload

- **Task:** Extend the `Student` class from Task 10 with the following:
  - Public method `def reload_from_json(self, json):` that replaces all attributes of the `Student` instance.
  - You can assume `json` will always be a dictionary.
  - A dictionary key will be the public attribute name.
  - A dictionary value will be the value of the public attribute.
  - You are not allowed to import any module.
- No test cases needed.
- **File:** `11-student.py`

## 12. Pascal's Triangle

- **Task:** Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing Pascal’s triangle of `n`:
  - Returns an empty list if `n` <= 0.
  - You can assume `n` will always be an integer.
  - You are not allowed to import any module.
- No test cases needed.
- **File:** `12-pascal_triangle.py`

## 13. Search and Update

- **Task:** Write a function that inserts a line of text to a file, after each line containing a specific string.
- **Prototype:** `def append_after(filename="", search_string="", new_string=""):`
- You must use the `with` statement.
- Don’t need to manage file permission or file doesn’t exist exceptions.
- Not allowed to import any module.
- No test cases needed.
- **File:** `13-append_after.py`

## 14. Log Parsing

- **Task:** Write a script that reads and parses logs.
- **Prototype:** `python parse_logs.py`
- You must use the `with` statement.
- Don’t need to manage file permission or file doesn’t exist exceptions.
- Not allowed to import any module.
- No test cases needed.
- **File:** `100-parser.py`
- **Logs:** `log_sample.log`

