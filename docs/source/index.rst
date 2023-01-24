.. Django Multiple Authentication documentation master file, created by sphinx-quickstart on Thu Dec 29 10:11:13 2022. You can adapt this file completely to your liking, but it should at least contain the root `toctree` directive.

Welcome to Django Multiple Authentication's documentation!
==========================================================

.. image:: https://readthedocs.org/projects/django-multiple-authentication/badge/?version=latest
    :target: https://django-multiple-authentication.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Django Multiple Authentication allows you to use either email or username field or any other
field on your user model for your user authentication.

-------------------------------------------------------------------------------

Rationale
----------------

Django's default authentication only accepts username for user authentication.
So the package allows you to use either email or username or any other stuff on your user table for user authentication.
It works with django's in-built authentication function, so
it works as long as django's authentication function is called.

Contents
------------------------

.. toctree::
   :maxdepth: 3

   getting_started
   usage

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
