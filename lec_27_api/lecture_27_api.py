from flask import Flask
from flask import request
from lecture_27_db import check_user

app = Flask('example-project')


@app.route('/')
def index():
    return 'Hello guys!'


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        template = """
        <form method='POST'>
        <input type='text' name='login' placeholder='Login...'>
        <input type='password' name='password' placeholder='Password...'>
        <input type='submit' value='Sign In'>
        </form>
        """
        return template

    elif request.method == 'POST':
        params = request.form
        user_login = params.get("login")
        password = params.get("password")
        user = check_user(user_login, password)
        print(user)
        if user:
            return f'Congrats! You logged with login "{user_login}" and password "{password}"'
        else:
            return f'Your login or password are wrong!'


if __name__ == '__main__':
    app.run()
