Getting Started
=================

.. _requirements:

Requirements
------------

* Python >= 3.6
* Django (3.0, 3.1, 3.2, 4.0, 4.1)

These are the officially supported python and django package versions.  Other versions
will probably work.

.. _installation:

Installation
-------------

Django Multiple Authentication can be installed with pip:

.. code-block:: console

    pip install django
    pip install django-multiple-authentication

Then, your django project must be configured to use the library.  In ``settings.py``, add  ``multiple_auth`` to
your list of ``INSTALLED_APPS``:


.. _configuration:

Project Configuration
------------------------

Startup up a new project like this if you haven't

.. code-block:: console

    django-admin startproject sampleproject

    cd sampleproject

    python manage.py makemigrations

    python manage.py migrate

Add ``multiple_auth`` to your list of ``INSTALLED_APPS`` in your ``settings.py`` :


.. code-block:: python

    # sampleproject/settings.py

    INSTALLED_APPS = [
        ...
        "multiple_auth",
   ]


Now we tell django what ``AUTHENTICATION_BACKENDS`` we want to use for user authentication.
Update your ``settings.py`` with this:

.. code-block:: python

    # sampleproject/settings.py

    AUTHENTICATION_BACKENDS = (
        'multiple_auth.backends.MultipleAuthentication',
    )


Next you add ``MULTIPLE_AUTH`` settings (a dictionary) to your ``settings.py``. Include a key of ``auth_fields`` a value of the list of
field(s) in your User Model you want to accept for your authentication.

You can use one or more fields. For example,
we will be using the ``username`` and ``email`` fields. With this example users will be able to login with ``username`` or ``email``
So update your settings like this:

.. code-block:: python

    # sampleproject/settings.py

    MULTIPLE_AUTH = {
        'auth_fields': ['username', 'email']
    }


.. admonition:: NOTE

    Note that the the ``auth_fields`` is not just limited two fields. You can have one, two or more fields.

One Field:

.. code-block:: python

    # sampleproject/settings.py

    MULTIPLE_AUTH = {
        'auth_fields': ['id']
    }


Two OR More fields

.. code-block:: python

    # sampleproject/settings.py

    MULTIPLE_AUTH = {
        'auth_fields': ['email', 'username', 'phone_number', 'id', ...]
    }
