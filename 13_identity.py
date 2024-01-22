"""
Flag - Marks a spot in the code
None - Doesn't have a value
"is" and "is not" - can be used to get truthfulness regarding type, value and identity
id = gets the identity of an element in the memory. If a variables value is equal to another variable, then it's id is going to be the same in order to increase efficiency
"""

v1 = 'a'
v2 = 'a'
v3 = 'A'

print(id(v1))
print(id(v2))
print(id(v3))


condition = True;
passed_on_if = None;

if condition :
    passed_on_if = True;
    print('Do something');

else:
    print('Do not act');

print(passed_on_if, passed_on_if is None);
print(passed_on_if, passed_on_if is not None);
