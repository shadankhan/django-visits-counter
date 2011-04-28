``django-visits-counter`` is a django app to count add a visit counter to any
type of object on django projects.

The offial repository for ``django-visits-counter`` is at
http://code.google.com/p/django-visits-counter/.  Please file any tickets
there.

Features
========

* Count the visits for to an object
* Discart visits based on ip, user agent and time

Requirements
============

As far as I am aware, the only requirement for django-visits-counter to work is
a modern version of Django.  I developed the project on Django 1.3.

Installation
============

Download ``django-visits-counter`` using *one* of the following methods:

pip
---

You can download the package from the `CheeseShop
<http://pypi.python.org/pypi/django-visits-counter/>`_ or use::

    pip install django-visits-counter

to download and install ``django-visits-counter``.

easy_install
------------

You can download the package from the `CheeseShop
<http://pypi.python.org/pypi/django-visits-counter/>`_ or use::

    easy_install django-visits-counter

to download and install ``django-visits-counter``.

Checkout from Google Code
-------------------------

Use the following command::

    hg clone https://django-visits-counter.googlecode.com/hg/ django-visits-counter  

Configuration
=============

First of all, you must add this project to your list of ``INSTALLED_APPS`` in
``settings.py``::

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        ...
        'visits-counter',
        ...
    )

Run ``manage.py syncdb``.  This creates a few tables in your database that are
necessary for operation.

You can configure the visits discard interval in ``settings.py`` adding
``MIN_TIME_BETWEEN_VISITS=<minutes>``.

Usage
=====

To add a visit to and object you have to use the visits_counter.utils.add_visit
function in your views::
  from visits_counter.utils. import add_visit
  def view(request,id):
    my_object = MyModel.objects.get(pk=id)
    add_visit(request, my_object)

To show visits you have to load the visits_tags in your template and use the tag ``visits``::
    {% load visits_tags %}

    {% visits my_object as visits %}
    num of visits: {{ visits }}
