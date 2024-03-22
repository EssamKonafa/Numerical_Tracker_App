# import sqlite3

# def create_database():
#     connection = sqlite3.connect('app.db')
#     theCursor = connection.cursor()

#     theCursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')

#     connection.commit()
#     connection.close()

#     if __name__ == '__main__':
#         create_database()