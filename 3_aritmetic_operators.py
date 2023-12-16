#Aritmetic operators

sum = 2 + 2
print( 'sum:', sum)

subtraction = 4 - 2
print( 'subtraction:', subtraction)

multiplication = 3 * 2
print( 'multiplication:', multiplication)

division = 10 / 2
print( 'division:', division)

int_division = 10 // 3
print( 'int_division:', int_division)

exponentiation = 2 ** 5
print( 'exponentiation:', exponentiation)

module = 10 % 3
print('module:', module)

module2 = 10 % 5
print('module2:', module2)


#CONCATENATION  
my_name = 'André' + ' ' + 'Pinto';
print(my_name)

#REPETITION
three_As = 3 * 'A'; 
print(three_As)


#Operators precedence
exp_1 = 1 + 1 ** 5 + 5
#First the exponentiation, and then the sums
print(exp_1)

exp_2 = (1 + 1) ** 5 + int(5 * 4 / 2)
#First the parenthesis, then the exponentiation, then multiplication, then division and lastly sum. The 'int' is there to have no decimal cases due to division.
print(exp_2)