from helpers import check_users_exictance
from helpers import get_user
from auth import login


username = input('Enter uor user name :')
password = input('Enter your password :')

if check_users_exictance(username):
    user = get_user(username)
    logged_in = login(user, password)
    if logged_in:
        user['logged_in'] = True
        print(user)
    else:
        print('Invalid password')
else:
    print('Invalid username')