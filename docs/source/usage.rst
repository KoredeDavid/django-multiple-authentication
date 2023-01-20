.. _usage:

Usage & Illustration
=======================

We will go through an illustration to show how the package works, but before we start let's create a user that we can
use to test our authentication.

.. code-block:: console

    python manage.py createsuperuser --username=test --email=test@email.com

It will bring a prompt to set ``password``. So just set your password and you're done creating a user.

..

    .. This page will show how the package works with:
        * :ref:`Web App <web_app>`
        * :ref:`REST API <rest_api>`



    .. .. _web_app:

    .. Web App
    ---------

We are going to use django's in-built authentication app which is already pre-installed for this illustration.
To use the ``auth`` app we need to add it to our project-level ``urls.py`` file.
I've chosen to import the ``auth`` app ``views``.


.. code-block:: python

    # sampleproject/urls.py
    from django.contrib import admin
    from django.contrib.auth import views # new

    urlpatterns = [
        path("admin/", admin.site.urls),
        path("accounts/login/", views.LoginView.as_view(template_name='admin/login.html'), name="login") # new
    ]


.. admonition:: Remember

    You can also use your own custom login authentication just like this `tutorial <https://www.smashingmagazine.com/2020/02/django-highlights-user-models-authentication/>`_

We should specify where to redirect the user upon a successful login.
In other words, once a user has logged in, where should they be sent on the site?
We use the ``LOGIN_REDIRECT_URL`` setting to specify this route.
At the bottom of the settings.py file add the following to redirect the user to the homepage.

.. code-block:: python

    # sampleproject/settings.py

    LOGIN_REDIRECT_URL = "/"


Let's now tell django to let users login with either ``email`` or ``username`` or user ``id`` in our ``settings.py``!

Update your the ``auth_fields`` setting within ``MULTIPLE_AUTH`` as follows:

.. code-block:: python

    # sampleproject/settings.py

    MULTIPLE_AUTH = {
        'auth_fields': ['username', 'email', 'id']
    }

It's time to test! Start your server with ``python manage.py runserver`` in your console and navigate to our login page at ``http://127.0.0.1:8000/accounts/login/``.
You con now login with either ``email`` or ``username`` or user ``id``. Yipee!!!



..  figure:: assets/gifs/webapp.gif
    :alt: A GIF showing a user logging in with his ``email``, ``username`` and ``id``.
    :align: center
    :scale: 30 %

    Here's a GIF showing a user logging in with his ``email``, ``username`` and ``id``.

.. admonition:: NOTE!

    It also works with **Django Admin** and **REST Apis**




..

    .. .. _rest_api:

    .. REST API
    -------------
    For this illustration let's install **Django REST Framework (DRF)** which is a toolkit built on top of Django that
    is used for building API's.

    .. .. code-block:: console

       .. pip install djangorestframework