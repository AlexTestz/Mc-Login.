import os
from dotenv import load_dotenv

from flask import Flask
from flask import render_template, redirect, request, Response, session
from flask_mysqldb import MySQL , MySQLdb



app = Flask(__name__,template_folder="template")

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'login'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql=MySQL(app)

#Login
@app.route('/')
def home():
    return render_template('Login.html')
#Init Session
@app.route('/Session')
def init_session():
    return render_template('Session.html')



#Function Login
@app.route('/access-login', methods= ["GET","POST"])
def login():

    if request.method == 'POST' and 'txtCorreo' in request.form and 'txtPassword':
        _correo = request.form['txtCorreo']
        _password = request.form['txtPassword']

        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM usuarios WHERE correo = %s AND password = %s',(_correo,_password,))
        account = cur.fetchone()

        if account:
            session['logeado'] = True
            session['id'] = account ['id']

            return render_template('Session.html') #Se logea al inicio
        else: 
             return render_template('Login.html', messaje="Correo o contraseña incorrectos")

if __name__=='__main__':     
    app.secret_key = 'alex'
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)

