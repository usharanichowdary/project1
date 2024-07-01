from flask import Flask, render_template, request, redirect, url_for
import pymysql


app = Flask(__name__)


db = pymysql.connect(
    host='localhost',
    user='root',  
    password='',  
    db='flask_app'  
)

@app.route('/')
def index():
    return 'Welcome to Flask MySQL app'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email=request.form['email']
        password = request.form['password']
        cursor = db.cursor()
        cursor.execute('INSERT INTO users (username,email,password) VALUES (%s, %s, %s)', (username,email, password))
        db.commit()
        cursor.close()
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        user = cursor.fetchone()
        cursor.close()
        if user:
            return 'Login successful'
        else:
            return 'Invalid credentials'
    return render_template('login.html')

if __name__ == '__main__':  
    app.run(debug=True)
