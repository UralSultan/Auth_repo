from data import USERS


def check_users_exictance(username):
    for u in USERS:
        if u['username'] == username:
            return True
    return False


def get_user(username: str) -> dict:
    for user in USERS:
        if user['username'] == username:
            return user

