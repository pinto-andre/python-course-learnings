#STRING FORMATING

#Method f-string
name = 'André Pinto'
height = 1.66
weight = 70
bfi = weight / ( height**2)

answer =  f'{name} is {height}m, weights {weight}kg and his bfi is {bfi:.2f}' #Here the '.2f' is going to make the bfi to show only with 2 decimal cases

print( answer )


#Method format

a = 'A'
b = 'B'
c = 1.1
string = 'a={name1} b={name2} c={name3:.2f}'
format = string.format(name1=a, name2=b, name3=c)

print( format )

name = 'John'
age = 23
string = '{1} is {0} years old'
print(string.format(name, age))


#Collecting user given information

name = input("What's your name? ")
print( name )

#Since it always gathers strings we may need to convert what we are collecting:

number_1 = input('Choose a number: ')
number_2 = input('Choose a number: ')

#Converting collected strings to number types
int_number_1 = int(number_1)
int_number_2 = int(number_2)

#If any of the variables ins't a number, it will throw an error
print(f'The numbers total sum is {int_number_1 + int_number_2}') 