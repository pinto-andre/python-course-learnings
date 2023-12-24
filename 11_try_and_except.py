#try and except

number = input("Choose a number and I'll double it: ")
""" number_float = float(number)
print(f'The double of {number_float} is {number_float * 2:.2f}') """

#Is digit checks if the value is a number or not, if it is, returns true, if not returns false

print(number.isdigit()) 

#If you insert a number, the code will run without any exception(error), if not it will run until the first print and then will return the except
try:
    print("STR:", number)
    number_float = float(number)
    print("Float:", number_float)
    print(f'The double of {number_float} is {number_float * 2:.2f}')

except:
    print("That's not a number, please try again")