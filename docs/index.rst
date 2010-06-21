Flask-Fungiform
================

.. module:: flaskext.fungiform

Flask-Fungiform makes integrating `Fungiform`_ into your `Flask`_
application easy.

.. _Fungiform: http://github.com/mitsuhiko/fungiform
.. _Flask: http://flask.pocoo.org/


Installation
------------

Install the extension with one of the following commands::

    $ easy_install Flask-Fungiform

or alternatively if you have pip installed::

    $ pip install Flask-Fungiform


Usage
----------

Forms are created as subclasses of :class:`Form`. 
Here's a complete example of a user registration form:

.. code-block:: python

	from flask import Flask, Markup
	from flaskext.fungiform import Form, TextField,  widgets


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

To output such a form as HTML you first need to pass an instance of it
as a context variable when rendering a template:

>>> form = RegisterForm()
>>> return render_template('register.html', form=form.as_widget())

A Jinja2 template that outputs the form as HTML 
would look something like this:

.. code-block:: jinja

	{% extends "layout.html" %}
	{% block body %}
	  <h2>Register Example</h2>
	  {% call form() %}
	    <dl>
	      {{ form.username.as_dd() }}
	      {{ form.password.as_dd() }}
	      {{ form.password_repeat.as_dd() }}
	    </dl>
	    <p class=actions>
	      <input type=submit value=Register>
	  {% endcall %}
	  {% if validated_data %}
	    <h2>Data Valid</h2>
	    <pre>{{ validated_data|pprint }}</pre>
	  {% endif %}
	{% endblock %}

The above code will generate the opening and closing *form* tags along
with a csrf protection token for the form as a hidden input and
all the defined form fields as inputs inside *dd* elements.
The resulting HTML will be the following:

.. code-block:: html

  
	  <h2>Register Example</h2>
	  <form action="" method="post"><div style="display: none"><input type="hidden" name="_csrf_token" value="192b8007b4220f84796d"></div>
	    <dl>
	      <dt><label for="f_username">Username</label></dt><dd><input type="text" id="f_username" value="" name="username"></dd>
	      <dt><label for="f_password">Password</label></dt><dd><input type="password" id="f_password" value="" name="password"></dd>
	      <dt><label for="f_password_repeat">Password <small>(repeat)</small></label></dt><dd><input type="password" id="f_password_repeat" value="" name="password_repeat"></dd>

	    </dl>
	    <p class=actions>
	      <input type=submit value=Register>
	  </form>
  


A form instance automatically discovers user submitted data from 
GET, POST and PUT request parameters. A complete example of a function
that displays a form and validates the data upon submission
follows:

.. code-block:: python

	@app.route('/register', methods=['GET', 'POST'])
	def register():
	    form = RegisterForm()
	    validated_data = None
	    if request.method == 'POST' and form.validate():
	        validated_data = form.data
	    return render_template('register.html', form=form.as_widget(),
	                           validated_data=validated_data)

For a full example application see the `examples`_ folder for the project.

.. _examples:
   http://github.com/mitsuhiko/flask-fungiform/tree/master/examples/
