#class 1

#Below the function shows '2' on the console
print(1 + 1)

""" 
here is just to show how to make multi-line comments
print (123) 
"""


#class 2

#Below we have a print function reading more than one argument
print(12, 34) #standard separator ' '
print(56, 78, sep='-') #hyphen as chosen separator
print(9, 10, 11, sep=' and ') # spaced 'and' as chosen separator


#class 3
#String with single quotes
print('André Pinto') #--> Shows André Pinto

#String with double quotes
print("André Pinto") #--> Shows André Pinto
print("André 'Pinto'") #--> Shows André 'Pinto'

#String with escape char (\)
print("André \"Pinto\"") #--> Shows André "Pinto"


#class 4
#integer number (aka int)
print(1)
print(-10)
print(0)

#float number
print(1.5)
print(-11.1)
print(0.0)


#class 5
#Boolean type
print(10 == 10)
print( False )

#discover with what data type we're dealing
print( type('hello') )
print( type(1) )
print( type(True) )

#type conversion
print( '1', type(int('1')) ) #integer
print( float('1') ) #float
print( 1, type(str(1))  ) #string


#class 7
#Variable naming and declaring
my_name = 'André'
print( my_name ) #--> André

print(my_name + str(27)) #Since we are converting an integer into a string, the plus operator will concatenate two strings
age = 27;
is_not_minor = age >= 18

print( 'name:', my_name, 'age:', age)
print( 'Is not a minor?', is_not_minor)