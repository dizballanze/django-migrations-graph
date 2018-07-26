=============================
django-migrations-graph
=============================

.. image:: https://badge.fury.io/py/django-migrations-graph.svg
    :target: https://badge.fury.io/py/django-migrations-graph

.. image:: https://travis-ci.org/dizballanze/django-migrations-graph.svg?branch=master
    :target: https://travis-ci.org/dizballanze/django-migrations-graph

.. image:: https://codecov.io/gh/dizballanze/django-migrations-graph/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/dizballanze/django-migrations-graph

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
    :target: https://saythanks.io/to/dizballanze

Django-admin command to display migrations with dependencies.

Documentation
-------------

Requirements
-----------

- Python 2.7, 3.4+
- Django 1.8+

Quickstart
----------

Install django-migrations-graph::

    pip install django-migrations-graph

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'migraph',
        ...
    )

Screenshot
--------

.. image:: screenshot.png

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage

License
-----

MIT
