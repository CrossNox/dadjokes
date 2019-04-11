Dadjokes
========

`icanhazdadjoke <https://icanhazdadjoke.com/>`__ API wrapper, to
programatically cheer your code up.

Installation
============

.. code:: bash

    pip install dadjokes

Usage
=====

Example
-------

.. code:: python

    from dadjoke import Dadjokes
    dadjoke = Dadjoke()
    print(dadjoke.joke)

The previous snippet will print a random joke.

``Dadjoke`` objects can be built from an id as well. You can get those
calling the ``.id`` property of a ``Dadjoke``. If you are using this in
a **Slack** app, you might find the ``.as_slack`` property useful.

You can use the iterable ``DadjokeSearch`` iterable class to search
jokes by term, with an optional limit.

cli
~~~

Please check available options with:

.. code:: bash

    dadjokes -h
