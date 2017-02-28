sqlalchemy-media
================

Documentation
-------------
faspell is an async library for providing suggestion for Persian spellchecking.

Usage
-----------

Here is a simple example to see how to use this library:

.. code-block:: python

  from faspell.spell_checker import SpellChecker
  # Hint: database is supposed to be a text file containing persian words separated by \n. e.g. سلام\nسیب\nدرخت
  sp = SpellChecker(database=path_to_db)
  sp.correct(word='متغاضی')

Produces
-----------
    ['متقاضی']



