Usage & Illustration
=======================

.. _usage:

We will go through an illustration to show how the package works, but before we start let's create a user that we can
use to test our authentication.

.. code-block:: console

    python manage.py createsuperuser --username=test --email=test@email.com

It will bring a prompt to set ``password``. So just set your password and you're done creating a user.

We are going to use django's in-built authentication app which is already pre-installed.
To use the ``auth`` app we need to add it to our project-level ``urls.py`` file.
I've chosen to import the ``auth`` app ``views`` and we are going to use its ``LoginView``.


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
You can now login with either ``email`` or ``username`` or user ``id``. Yipee!!!



..  figure:: assets/gifs/webapp.gif
    :alt: A GIF showing a user logging in with his ``email``, ``username`` and ``id``.
    :align: center

    Here's a GIF showing a user logging in with his ``email``, ``username`` and ``id``.

.. admonition:: NOTE

    It also works with **Django Admin** and **REST APIs!!!**

