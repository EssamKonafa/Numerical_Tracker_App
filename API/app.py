from flask import Flask, request, jsonify

app=Flask(__name__)

@app.route('/')

def home():

    return 'welcom to ur fist flask app'

if __name__ == "__main__":
    app.run(debug=True)