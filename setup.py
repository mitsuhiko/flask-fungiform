"""
Flask-Fungiform
---------------

Adds fungiform support to Flask.

Links
`````

* `documentation <http://packages.python.org/Flask-Fungiform>`_
* `development version
  <http://github.com/mitsuhiko/flask-fungiform/zipball/master#egg=Flask-Fungiform-dev>`_

"""
from setuptools import setup


setup(
    name='Flask-Fungiform',
    version='0.8',
    url='http://github.com/mitsuhiko/flask-fungiform',
    license='BSD',
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    description='Adds fungiform support to Flask',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'fungiform'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
