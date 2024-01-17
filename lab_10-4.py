"""

Create a Python file named lab_10-3.py
*** You must write a comment for every chunk of code you write from now on along with your author tag***

Write a program that contains a function called double_stuff. The function should take a list as its only parameter.
When a list is passed as an argument to the function, the function should double each value in the list, regardless of its type
Write test cases to confirm that your function works when passed a list that:
Contains only integers
Contains integer and float values
Contains a combination of integer, string, and float values

_____________________________________________________________________________________________________________

Create a Python file named lab_10-4.py

Write a program that contains a function called indexed_names. 
The function should take a list of names as its only parameter.
When a list is passed as an argument to the function,
the function should return a new list where each value is replaced by the index, 
followed by a color, space, and the original value
i.e. passing through ["John", "Jane", "Bob"] 
would return ["0: John", "1: Jane", "2: Bob"]
Write 2 test cases to confirm that your function works when passed a list that:



"""

# Author: Andrew Tkacs

def indexed_names(name_list):
    """
    Replaces each value in the given list with index, color, space, and original value.

    Parameters:
    - name_list (list): The input list of names to be processed.

    Returns:
    - list: The new list with modified values.
    """
    return [f"{index}: {name}" for index, name in enumerate(name_list)]

# Test Case 1: List of names
names_1 = ["John", "Jane", "Bob"]
result_names_1 = indexed_names(names_1)
print(f"Original List: {names_1}")
print(f"Indexed Names: {result_names_1}")
print()

# Test Case 2: Another list of names
names_2 = ["Alice", "Charlie", "David"]
result_names_2 = indexed_names(names_2)
print(f"Original List: {names_2}")
print(f"Indexed Names: {result_names_2}")
