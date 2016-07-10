import asyncio

from helpers import AsyncListOfTupleIteration


my_list = [('a', 2), ('as', 2312, 'sdfsdfs')]

async def iterate():
    async for i, j in AsyncListOfTupleIteration(my_list):
        print(i, j)


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(iterate())
