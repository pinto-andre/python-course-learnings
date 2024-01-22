"""

Up until here, we already covered some immutable types: str, int, float and bool.
This means that its values can't change
"""

string = 'André Pinto'

""" string[10] = 'a' - Throws an error because it's immutable """

print(string);

new_string = f'{string[:3]}u{string[4:]}'
print(new_string)

