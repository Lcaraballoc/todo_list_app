from flask import Flask, request, make_response, redirect, session

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SUPER SECRETO'

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return response


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    user_ip = session.get('user_ip')
    return user_ip

