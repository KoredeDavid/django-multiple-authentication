.. _usage:

Usage & Illustrations
=======================

We will go through some illustrations but before we start let's creating a user that we can use to test our authentication

.. code-block:: console

    python manage.py createsuperuser --username=test --email=test@email.com --password=whatthef*ck

This page will show how to use the package with:
    * :ref:`Web App <web_app>`
    * :ref:`REST API <rest_api>`
    * :ref:`Django Admin <django_admin>`


.. _web_app:

Web App
---------

We are going to use django's in-built authentication app which is already pre-installed for this illustration
To use the ``auth`` app we need to add it to our project-level urls.py file.
Make sure to add include on the second line. I've chosen to include the auth app at accounts/ but you can use any url pattern you want.


.. code-block:: python
    # sampleproject/urls.py
    from django.contrib import admin
    from django.urls import path, include # new

    urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  # new
    ]

.. admonition:: Remember

    You can also use your own custom authentication App.

We should specify where to redirect the user upon a successful login.
In other words, once a user has logged in, where should they be sent on the site?
We use the LOGIN_REDIRECT_URL setting to specify this route.
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

Here's a GIF showing a user logging in with his ``email``, ``username`` and ``id``.

.. figure:: assets/gifs/webapp.gif

    GIF caption

.. _rest_api:

REST API
-------------

.. _django_admin:

Django Admin
-------------