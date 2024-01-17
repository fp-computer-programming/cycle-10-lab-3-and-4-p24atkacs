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

#Author: Andrew Tkacs

def double_stuff(my_list):
    """
    Doubles each value in the given list, regardless of its type.

    Parameters:
    - my_list (list): The input list to be modified.

    Returns:
    - list: The modified list with doubled values.
    """
    return [item * 2 for item in my_list]

# Test Case 1: List with only integers
int_list = [1, 2, 3, 4, 5]
result_int = double_stuff(int_list)
print(f"Original List: {int_list}")
print(f"Doubled List: {result_int}")
print()

# Test Case 2: List with integers and float values
mixed_list_1 = [1, 2.5, 3, 4.75, 5]
result_mixed_1 = double_stuff(mixed_list_1)
print(f"Original List: {mixed_list_1}")
print(f"Doubled List: {result_mixed_1}")
print()

# Test Case 3: List with a combination of integer, string, and float valuesd
mixed_list_2 = [1, 'hello', 3.14, 4, 'world']
result_mixed_2 = double_stuff(mixed_list_2)
print(f"Original List: {mixed_list_2}")
print(f"Doubled List: {result_mixed_2}")
