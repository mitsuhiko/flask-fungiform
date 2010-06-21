Flask-Fungiform
================

.. module:: flaskext.fungiform

Flask-Fungiform adds support for `Fungiform`_ to your `Flask`_
application.  

.. _Fungiform: http://github.com/mitsuhiko/fungiform
.. _Flask: http://flask.pocoo.org/
.. _example sourcecode:
   http://github.com/mitsuhiko/flask-fungiform/tree/master/examples/

Installation
------------

Install the extension with one of the following commands::

    $ easy_install Flask-Fungiform

or alternatively if you have pip installed::

    $ pip install Flask-Fungiform


How to Use
----------

The forms you create are subclasses of :class:`Form`. 
Here's a complete example of a user registration form:

.. code-block:: python

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

To display such a form in HTML you first need to pass it as a context variable
when rendering the template:

>>> form = RegisterForm()
>>> return render_template('register.html', form=form.as_widget())

A Jinja2 template that renders the form as HTML would look something like this:

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


A form instance automatically discovers user submitted data from
request parameters. A complete example of a function
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



