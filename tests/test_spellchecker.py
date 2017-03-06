import asyncio

from async_faspell.main import SpellChecker


async def test_spell_checker():
    with open('db', 'r') as db:
        sp = SpellChecker(db.read())
        await sp.correct('متغاضی') == ['متقاضی']


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_spell_checker())
