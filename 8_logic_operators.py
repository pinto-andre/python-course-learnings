#Logical operators


#and operator (all expressions need to be true)
entry_command = input("To enter or leave write [E] or [L], respectively: ")
password = input("Your password is needed to enter: ")

allowed_password = 123456

if entry_command == "E" and int(password) == allowed_password :
	print("You're in!!")
elif entry_command == "E" and int(password) != allowed_password :
	print("Wrong password, failed to enter :(")
elif entry_command == "L" and int(password) == allowed_password :
	print("You're out!!")
elif entry_command == "L" and int(password) != allowed_password :
	print("Wrong password, failed to leave :(")
else:
	print("Looks like something went wrong, please try again")
	

#or operator (only one of the expressions needs to be true)
	#Example
entry_command = input("To enter or leave write [E] or [L], respectively: ")
password = input("Your password is needed to enter: ")

allowed_password = 123456

if (entry_command == "E" or entry_command == "e") and int(password) == allowed_password :
	print("You're in!!")
elif (entry_command == "E" or entry_command == "e") and int(password) != allowed_password :
	print("Wrong password, failed to enter :(")
elif (entry_command == "L" or entry_command == "l") and int(password) == allowed_password :
	print("You're out!!")
elif (entry_command == "L" or entry_command == "l") and int(password) != allowed_password :
	print("Wrong password, failed to leave :(")
else:
	print("Looks like something went wrong, please try again")
	 

#not operator example (To invert meanings)
password = input("Your password: ")
allowed_password = 123456

if not password : #IF password is an empty string (empty string is falsy)
	print( "Please enter your password" )
elif int(password) != 123456 :
	print( "Wrong password!" )

print(not True) #---> False
print(not False) #---> True


#in operator (used to check if "a" is in "b")
name = "Hideki"

print( "e" in name)

if ('e' in name) :
	print("Your name has an 'e' inside it")


#not in operator (used to check if "a" isn't in "b")
name2 = "Yuuki"

print( "e" not in name2)

if ('e' not in name2) :
	print("Your name2 doesn't have an 'e' inside it")