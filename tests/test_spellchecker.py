import asyncio
import aiofiles

from async_faspell.main import SpellChecker


async def test_spell_checker():
    async with aiofiles.open('db', 'r') as db:
        sp = SpellChecker(await db.read())
        assert await sp.correct('متغاضی') == ['متقاضی']


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_spell_checker())
