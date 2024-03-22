from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app=Flask(__name__)
CORS(app)

def create_database():
    connection = sqlite3.connect('app.db')
    theCursor = connection.cursor()

    theCursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')

    connection.commit()
    connection.close()

create_database()

@app.route('/signup', methods=['POST'])
def signup():
    userData = request.get_json()
    username= userData.get('username')
    password= userData.get('password')

    if not username or not password:
        return jsonify({'success': False, 'message':'username and password are required'})
    
    connection = sqlite3.connect('app.db')
    theCursor = connection.cursor()

    try:
        theCursor.execute('INSERT INTO users (username,password) VALUES (?,?)',(username,password))
        connection.commit()
        connection.close()
        return jsonify({'success':True, 'message':'user registered successfully'})
    except sqlite3.IntegrityError:
        connection.close()
        return jsonify({'success':False, 'message':'user already exist'})
    
@app.route('/login', methods=['POST'])
def login():
    userData= request.get_json()
    username= userData.get('username')
    password= userData.get('password')

    connection= sqlite3.connect('app.db')
    theCursor=connection.cursor()

    theCursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username,password))
    user=theCursor.fetchone()
    connection.close()

    if user:
        return jsonify({'susses':True,'message':'login successfully'})
    else:
        return jsonify({'success':False,'message':'invalid username or password'})

if __name__ == "__main__":
    app.run(debug=True)