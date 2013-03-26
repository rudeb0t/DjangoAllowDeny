=================
Django Allow/Deny
=================

This package contains a Django middleware that implements a very simple IP
address-based access control similar to the method provided by Apache's
mod_access module. The motivation for this middleware is to provide this
capability to Django's built-in web server or `Tornadio2Go`_.

Installation
============

The quickest way to install is via `pip`_ from within a `virtualenv`_.::

    pip install https://github.com/rudeb0t/DjangoAllowDeny/master.zip#egg=django-allowdeny

Alternatively, you can opt to use an "editable" installation::

    pip install -e https://github.com/rudeb0t/DjangoAllowDeny.git#egg=django-allowdeny

Usage
=====

Add ``django_allowdeny`` to your ``INSTALLED_APPS``. Then add
``django_allowdeny.middleware.AllowDenyMiddleware`` as the first item your
``MIDDLEWARE_CLASSES`` list.

Django Settings
===============

The middleware is configured by default to allow all connections even if you
have already installed it.  To enable access control add the
``ALLOW_DENY_SETTINGS`` dictionary to your Django settings file. This
dictionary accepts the following keys:

* ``ORDER`` - a list containing the strings 'allow' or 'deny' or both.

* ``ALLOW`` - a list of IP addresses to allow access based on ``ORDER``.

* ``DENY`` - a list of IP addresses to deny access based on ``ORDER``.

Allow/Deny Behavior
===================

Depending on ``ORDER`` you will get different behaviors for when an IP address
matches the one found in ``ALLOW`` and ``DENY`` lists. Typical use cases for
``ORDER``:

* ['allow', 'deny'] - If IP address is found in ``ALLOW``, allow access. If IP
  address is found in ``DENY`` but not in ``ALLOW``, deny access. Otherwise,
  allow access.

* ['deny', 'allow'] - If IP address is found in ``ALLOW`` but not in ``DENY``,
  allow access. If IP address is found in ``DENY``, deny access. Otherwise,
  allow access.

ALLOW/DENY Values
=================

``ALLOW`` and ``DENY`` can contain a list of IP addresses in dotted quad
notation. You can also use the special keyword 'all'.

Currently Unimplemented
=======================

This middleware is not intended to replace more robust access controls found in dedicated web servers such as Apache, Nginx and Cherokee.
As such, there is currently no support for the following:

* IP address ranges and subnets.

* IPV6 addresses.

There are no plans to add support for these at a later date.

.. _Tornadio2Go: https://github.com/rudeb0t/tornadio2go
.. _pip: http://pypi.python.org/pypi/pip
.. _virtualenv: http://pypi.python.org/pypi/virtualenv
