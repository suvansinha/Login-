username='Wade'
password='DPloveschimichangas!'

username_input = input('Username: ')
password_input = input('Password: ')

if username_input == username and password_input == password:
    print('Access granted')
elif username_input != username and password_input == password:
    print('Access denied')
    print('Username is incorrect')
elif username_input == username and password_input != password:
    print('Access denied')
    print('Password is incorrect')  
else:
    print('Access denied')
    print('You might wanna check the fields...')
    