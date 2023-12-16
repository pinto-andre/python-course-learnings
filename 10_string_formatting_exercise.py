"""
Exercise
Ask the user to write his/her name
Ask the user to write his/her age

If the user writes both of them you need to show the following sentences:
1) 'Your name is ...'
2) 'Your inverted name is ...'
3) 'Your name contains(or not) spaces'
4) 'The first letter of your name is ...'
5) 'The last letter of your name is ...'

If the user doesn't fill any of the fields show:
6) 'Sorry, looks like you left the required fields empty :('
"""

username = input('Write your name: ')
age = input("What is your age? ")

if username and age :
    print(f'Your name is {username} and you are {age} years old')
    print(f'Your inverted name is {username[::-1]}')
    if ' ' in username :
        print('Your name contains spaces')
    else:
        print("Your name doesn't contain spaces")
    print(f'The first letter of your name is {username[0]}')
    print(f'The last letter of your name is {username[len(username)-1]}')
elif not username or not age :
    print('Sorry, looks like you left the required fields empty :(')