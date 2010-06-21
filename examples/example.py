from flask import Flask, Markup, render_template, redirect, url_for, request
from flaskext.fungiform import Form, TextField, Multiple, \
     Mapping, IntegerField, ChoiceField, ValidationError, widgets


app = Flask(__name__)
app.secret_key = 'development key'


class RegisterForm(Form):
    username = TextField('Username', required=True)
    password = TextField('Password', widget=widgets.PasswordInput,
                         required=True)
    password_repeat = TextField(Markup('Password <small>(repeat)</small>'),
                                widget=widgets.PasswordInput)

    def context_validate(self, data):
        if data['password'] != data['password_repeat']:
            raise ValidationError('The two passwords do not match')


class MappingForm(Form):
    items = Multiple(Mapping(
        product = ChoiceField('Product'),
        count = IntegerField('Number of Items', sentinel=True)
    ), 'Items in Basket')

    def __init__(self, initial=None, action=None, request_info=None):
        Form.__init__(self, initial, action, request_info)
        self.items.field.fields['product'].choices = [
            (0, 'Item 1'),
            (1, 'Item 2')
        ]


@app.route('/')
def index():
    return redirect(url_for('register'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    validated_data = None
    if request.method == 'POST' and form.validate():
        validated_data = form.data
    return render_template('register.html', form=form.as_widget(),
                           validated_data=validated_data)


@app.route('/mapping', methods=['GET', 'POST'])
def mapping():
    form = MappingForm()
    validated_data = None
    if request.method == 'POST' and form.validate():
        validated_data = form.data
    return render_template('mapping.html', form=form.as_widget(),
                           validated_data=validated_data)


if __name__ == '__main__':
    app.run(debug=True)
