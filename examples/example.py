from flask import Flask, Markup, render_template, redirect, url_for, request
from flaskext.fungiform import Form, TextField, ValidationError, widgets


app = Flask(__name__)
app.secret_key = 'development key'


class RegisterForm(Form):
    username = TextField('Username', required=True)
    password = TextField('Password', widget=widgets.PasswordInput,
                         required=True)
    password_repeat = TextField(Markup('Password <small>(repeat)</small>'))

    def context_validate(self, data):
        if data['password'] != data['password_repeat']:
            raise ValidationError('The two passwords do not match')


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        app.logger.debug('Form data: %s', form.data)
        return 'Registered!'
    return render_template('register.html', form=form.as_widget())


if __name__ == '__main__':
    app.run(debug=True)
