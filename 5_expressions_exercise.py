""" 
EXERCISE
Create the necessary variables and the expression to calculate the body fat index.
The answer should be a string like:
<name> is <height>m, weights <weight>kg and his/her bfi is <bfi>
"""

name = 'André Pinto'
height = 1.66
weight = 70
bfi = weight / ( height**2)

answer = name + ' is ' + str(height) + 'm, weights ' + str(weight) + 'kg and his bfi is ' + str(bfi)
print( answer )