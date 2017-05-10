=============================
django-migrations-graph
=============================

.. image:: https://badge.fury.io/py/django-migrations-graph.svg
    :target: https://badge.fury.io/py/django-migrations-graph

.. image:: https://travis-ci.org/dizballanze/django-migrations-graph.svg?branch=master
    :target: https://travis-ci.org/dizballanze/django-migrations-graph

.. image:: https://codecov.io/gh/dizballanze/django-migrations-graph/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/dizballanze/django-migrations-graph

Django-admin command to display migrations with dependencies.

Documentation
-------------


Quickstart
----------

Install django-migrations-graph::

    pip install django-migrations-graph

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'migraph.apps.MigraphConfig',
        ...
    )

Add django-migrations-graph's URL patterns:

.. code-block:: python

    from migraph import urls as migraph_urls


    urlpatterns = [
        ...
        url(r'^', include(migraph_urls)),
        ...
    ]

Features
--------

* TODO

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
