import sqlite3

class User:
    def __init__(self, login, password) -> None:
        self.login = login
        self.password = password

    def add(self, cur, db) -> None:
        cur.execute(f"""INSERT INTO users VALUES
                        ('{self.login}', '{self.password}')""")
        db.commit()

class VerifyUser:
    def login(login, cur, db, ) -> bool:
        users = cur.execute("SELECT login, password FROM users ORDER BY login")
        users = [user for user in users]
        logins = [user[0] for user in users]

        if login in logins:
            return True
        else:
            return False

    def password(user, cur, db) -> bool:
        users = cur.execute("SELECT login, password FROM users ORDER BY login")

        users = [user for user in users]
        login = user.login

        for _user in users:
            if _user[0] == login:
                password = _user[1]
        if user.password == password:
            return True
        else:
            return False

class RegisterUser:
    def get_password(self) -> str:
        while True:
            password = input('Придумайте пароль:')
            password_confurm = input('Подтвержите пароль:')

            if password == password_confurm:
                break
            print('Попробуйте снова!')
        return password

    def get_login(cur, db) -> str:
        while True:
            login = input('Придумайте логин')
            if not VerifyUser.login(login, cur, db):
                break
            print('Такой логин уже сущестует!\nПопробуйте снова')
        return login



db = sqlite3.connect('users.db')
cur = db.cursor()

try:
    cur.execute('CREATE TABLE users(login, password)')
except:
    pass


match input('Вход - 1, Регистрация - 2\n'):
    case '1':
        user = User(input(),input())

        if VerifyUser.login(user.login, cur, db):
            if VerifyUser.password(user, cur, db):
                print('LOGGED IN')
            else:
                print('INCORRECT PASSWORD')
        else:
            print('Пользователя не существует!')

    case '2':
        login = RegisterUser.get_login(cur, db)
        password = RegisterUser.get_password()
        new_user = User(login, password)
        new_user.add(cur, db)

users = cur.execute("SELECT login, password FROM users ORDER BY login")
print('Список пользователей:')
print([user for user in users])

