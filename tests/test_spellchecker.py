import asyncio
from os import path

import aiofiles

from async_faspell.main import SpellChecker
import tests

PATH_TO_DB = path.abspath(path.join(path.dirname(tests.__file__), 'db'))

async def test_spell_checker():
    async with aiofiles.open(PATH_TO_DB, 'r') as db:
        sp = SpellChecker(await db.read())
        assert await sp.correct('متغاضی') == ['متقاضی']


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_spell_checker())
