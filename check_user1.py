import sqlite3

con = sqlite3.connect('db/users.db')
cur = con.cursor()


def check(user, password):
    result = cur.execute("""SELECT password FROM user
                WHERE login = ?""", (user,)).fetchall()
    if result:
        for i in result:
            if password == str(i[0]):
                return 'Yes'
            else:
                return 'NO'
    else:
        return 'make_new'


def add_user(user, password):
    a = cur.execute("""INSERT INTO users.db
                              (user, password)
                              VALUES
                              ?""", (user, password))
