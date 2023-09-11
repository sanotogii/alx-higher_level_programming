Test for 1-my_list.py
-------------------------------------------

Case 0: Import
>>> MyList = __import__('1-my_list').MyList
>>>

-------------------------------------------

Case 1: Common Case

>>> my_list = MyList()
>>> my_list.append(7)
>>> my_list.append(12)
>>> my_list.append(4)
>>> my_list.append(9)
>>> my_list.append(6)
>>> print(my_list)
[7, 12, 4, 9, 6]
>>> my_list.print_sorted()
[4, 6, 7, 9, 12]
>>> print(my_list)
[7, 12, 4, 9, 6]
>>>

-------------------------------------------

Case 2: Not Defined Object

>>> MyList = __import__('1-my_list').MyList
>>> my_list2.print_sorted()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'my_list2' is not defined
>>>

-------------------------------------------

Case 3: Passed a List

>>> a = [7, 2, 11]
>>> my_list = MyList(a)
>>> my_list.print_sorted()
[2, 7, 11]
>>>

-------------------------------------------

Case 4: Empty List

>>> a = []
>>> my_list = MyList(a)
>>> my_list.print_sorted()
[]
>>>

-------------------------------------------

Case 5: Unique Number

>>> my_list = MyList()
>>> my_list.append(5)
>>> my_list.print_sorted()
[5]
>>> print(my_list)
[5]
>>>

-------------------------------------------

Case 6: Same Number

>>> my_list2 = MyList()
>>> my_list2.append(3)
>>> my_list2.append(3)
>>> my_list2.append(3)
>>> my_list2.append(3)
>>> my_list2.print_sorted()
[3, 3, 3, 3]
>>>

-------------------------------------------

Case 7: Parent Object
>>> my_list = [7, 8, 9]
>>> my_list.print_sorted()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'print_sorted'
>>>

-------------------------------------------

Case 8: Negative Numbers

>>> MyList = __import__('1-my_list').MyList
>>> my_list = MyList()
>>> my_list.append(15)
>>> my_list.append(7)
>>> my_list.append(-3)
>>> my_list.append(42)
>>> my_list.append(-8)
>>> my_list.print_sorted()
[-8, -3, 7, 15, 42]
>>>

