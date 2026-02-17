USERS = {
    "admin": "1234"
}


def check_login(login, password):
    return USERS.get(login) == password
