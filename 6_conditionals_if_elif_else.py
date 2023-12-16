#CONDITIONALS
#IF / ELIF / ELSE


#Only one condition
entry = True;

if entry:
	print("You're in!!")

 #Whether it is accomplished or not, we only need to check the truthiness of the variable


#Two conditions: We give orders in case something happens, but if it doesn't then we want something different to occur:

dog_name = 'Leia'

if dog_name == 'Leia':
	print("Who's a pretty girl?")

else:
	print("What's the name?")


#More than two conditions

entry = input( 'Do you which to "enter" or "leave"? ')

if entry == 'enter':
	print('You are inside')

elif entry == 'leave':
	print('You are out')

else:
	print('You did not choose any of the options (enter/leave)')


