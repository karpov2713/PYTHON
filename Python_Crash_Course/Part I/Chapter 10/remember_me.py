"""
СОХРАНЕНИЕ И ЧТЕНИЕ ДАННЫХ, СГЕНЕРИРОВАННЫХ ПОЛЬЗОВАТЕЛЕМ
"""
import json
"""
Программа загружает имя пользователя, если оно было сохранено ранее.
В противном случае она запрашивает имя пользователя и сохраняет его.
"""
"""
filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when come back, {username}!")
else:
    print(f"Welcome back, {username}!")
"""

"""
РЕФАКТОРИНГ
"""
"""
def greet_user():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when come back, {username}!")
    else:
        print(f"Welcome back, {username}!")

greet_user()
"""

def get_stored_username():
    """ПОЛУЧАЕТ ХРАНИМАЕ ИМЯ ПОЛЬЗОВАТЕЛЯ, ЕСЛИ ОНО СУЩЕСТВУЕТ"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)


def greet_user():
    """ПРИВЕТСТВУЕТ ПОЛЬЗОВАТЕЛЯ ПО ИМЕНИ"""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()
