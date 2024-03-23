from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app=Flask(__name__)
CORS(app)

def create_database():
    connection = sqlite3.connect('database.db')
    theCursor = connection.cursor()

    theCursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    theCursor.execute('CREATE TABLE IF NOT EXISTS numerical_data (id INTEGER PRIMARY KEY, numerical_value INTEGER)')

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
    
    connection = sqlite3.connect('database.db')
    theCursor = connection.cursor()

    # theCursor.execute('SELECT id FROM users WHERE username=?',(username,))
    # exitingUser = theCursor.fetchone()

    # if exitingUser:
    #     connection.close()
    #     return jsonify({'success':False,'message':'username already exist try another one instead'})

    try:
        theCursor.execute('INSERT INTO users (username,password) VALUES (?,?)',(username,password))
        connection.commit()
        connection.close()
        return jsonify({'success':True, 'message':'user registered successfully'})
    except sqlite3.IntegrityError:
        connection.close()
        return jsonify({'success':False, 'message':'Error occurred while registering user'})

@app.route('/signin', methods=['POST'])
def signin():
    userData= request.get_json()
    username= userData.get('username')
    password= userData.get('password')

    connection= sqlite3.connect('database.db')
    theCursor=connection.cursor()

    theCursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username,password))
    user=theCursor.fetchone()
    connection.close()

    if user:
        return jsonify({'success':True,'message':'signin successfully'})
    else:
        return jsonify({'success':False,'message':'invalid username or password'})
    
@app.route('/saveNumValue', methods=['POST'])
def saveNumValue():
    data = request.get_json()
    numerical_value = data.get('numerical_value')

    connection = sqlite3.connect('database.db')
    theCursor = connection.cursor()

    theCursor.execute('INSERT INTO numerical_data (numerical_value) VALUES (?)', (numerical_value,))
    connection.commit()
    connection.close()

    return jsonify({'success':True,'message':'num saved successfully'})

@app.route('/getNumValues', methods=['GET'])
def getNumValues():
    connection = sqlite3.connect('database.db')
    theCursor = connection.cursor()

    theCursor.execute('SELECT numerical_value FROM numerical_data ORDER BY id DESC LIMIT 1')
    result = theCursor.fetchone()

    connection.close()

    if result:
        return jsonify({'success':True,'numerical_value':result[0]})
    else:
        return jsonify({'success': False, 'message': 'No numerical value found'})
    
if __name__ == "__main__":
    app.run(debug=True)