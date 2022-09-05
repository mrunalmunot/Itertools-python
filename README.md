# Itertools-python
Itertool module - ONLY FOR LEARNING

Python - Itertools

Import the itertools module. Define a function called `performiterator`, which takes 1 parameter.

• The first parameter is tuplevalues, which is a tuple. tuplevalues will always contain 4 tuples.

The function definition code stub is given in the editor. Generate the code based on the following conditions:

• Declare an empty main list.

• Declare another list. Use the cycle module in itertools to cycle through the first tuple and append the values to the list.

• Convert the list into a tuple and append it to the main list.

• Use the repeat module in itertools to repeat the first value from the second tuple.

• Create a tuple with the values and append it to the main list.

• Use the accumulate module in itertools to get the product after each iteration from the third tuple. → Create the tuple with the values and append it to the main list.

• Use the chain module in itertools to chain all the values of the tuple.

• Create a tuple with the values and append it to the main list.

• Use the filterfalse module in itertools to extract the odd numbers from the chained tuple.

• Create a tuple with the values and append it to the main list.

Convert the main list into a tuple and return it.

Input Format for Custom Testing

• In the first line, the length of each tuple is given.

• The next line contains the 'length' number of values

to be added to the first tuple. • The next line contains the 'length' number of values

to be added to the second tuple.

• The next line contains the 'length' number of values to be added to the third tuple.

• The next line contains the 'length' number of values to be added to the fourth tuple.


# Test Case:
Input

4

1

10

5

2

8

48

14

63

59

47

49

22

19

60

1

40

Output

((1, 10, 5, 2), (8, 8, 8, 8), (59, 106, 155, 177), (1, 10, 5, 2, 8, 48, 14, 63, 59, 47, 49, 22, 19, 60, 1, 40), (1, 5, 63, 59, 47, 49, 19, 1))
