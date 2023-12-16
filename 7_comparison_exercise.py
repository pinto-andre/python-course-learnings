#EXERCISE

""" 
Using comparison operators, solve the following:
You have two variables "value1" and "value2" for which the values are attributed by a user's input. 
You need to print to the console the following setences:
case 1 - value1 is bigger than value2;
case 2 - value2 is bigger than value1;
case 3 - value1 is equal to value2.
"""

value1 = input("Choose the first value: ")
value2 = input("Choose the second value: ")

if value1 > value2 :
    print(f'{value1=} is bigger than {value2=}')
elif value1 < value2 :
    print(f'{value2=} is bigger than {value1=}')
else:
    print(f'{value1=} is equal to {value2=}')