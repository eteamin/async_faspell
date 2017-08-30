async-faspell
================
[![Build Status](https://travis-ci.org/eteamin/async_faspell.svg?branch=master)](https://travis-ci.org/eteamin/async_faspell)

Documentation
-------------
faspell is an async library for providing suggestion for Persian spellchecking.

Usage
-----------
Here is a simple example to see how to use this library:

.. code-block:: python

  import asyncio
  from faspell.spell_checker import SpellChecker

  # Hint: database is supposed to be a text file containing persian words separated by \n. e.g. سلام\nسیب\nدرخت
  async def test_spellchecker():
     with open(path_to_db, 'r') as db:
        sp = SpellChecker(db.read())
        corrected = await sp.correct('متغاضی')
        print(corrected)
        
  loop = asyncio.get_event_loop()
  loop.run_until_complete(test_spellchecker())

Produces
-----------
    ['متقاضی']

Benchmark
------------
Hosted using aiohttp and gunicorn
the following benchmark 'ab -c 1000 -n 1000 url' results in!:

.. code-block:: bash

  Percentage of the requests served within a certain time (ms)
  
    50%     49
    66%     51
    75%     53
    80%     54
    90%     60
    95%     64
    98%     69
    99%     75

