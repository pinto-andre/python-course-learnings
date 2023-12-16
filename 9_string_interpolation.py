#String interpolation
	
name = 'André'
price = 1000.56943
variable = '%s, the price is €%.2f' % ( name, price )

print( variable )

#Hexadecimal example
print( 'The hexadecimal of %d is %05x' % (1569, 9651) )
#Here we use ‘%d’ because we are addressing an integer and the hexadecimal is set by ‘%05x’, where 05 represents the number of cases in which hexadecimal will appear and x triggers the hexadecimal.


#Formatting strings with f-strings
variable = 'ABC'
print(f'{variable}')
#the > symbol adds space on the right of variables
print(f'{variable:>10}')
#the < symbol adds space on the left of variables
print(f'{variable:<10}')
#the ^ symbol tries to add space evenly on both sides of variables
print(f'{variable:^10}')
#Here we are shortening the number of decimal cases and asking python to show '+' for positive numbers and '-' for negative numbers.
print(f'{1000.487364123746:+.1f}')
#If we used '-', oython would only show the sign for negative numbers
print(f'{1000.487364123746:-.1f}')
#Hexadecimals with f-strings are also possible
print(f'The hexadecimal of 1569 is {1500:08x}')


#String slicing

variable = 'Hello world!'
print(variable[4]) # --> 'o'
print(variable[-6 ]) # --> 'w'

variable2 = 'Hello world!'
print(variable2[6:11]) # --> 'world'
print(variable2[6:11:2]) # --> 'wrd'

#if you leave the first field blank it will start from the beginning of the string
print(variable2[:5]) # --> 'Hello'

#if you want to write a variable upside down you can use the step value with a negative number
print(variable2[::-1]) # --> '!dlrow olleH'
print(variable2[-1:-13:-1]) # --> '!dlrow olleH'


#len function
print(len(variable2)) # --> 12
print(len(variable2[6:11])) # --> 5