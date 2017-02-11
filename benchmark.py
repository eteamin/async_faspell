import asyncio
from datetime import datetime

import aiohttp

data = {
    'word': 'hellow'
}
requests = 100
async def benchmark():
    await asyncio.gather(*[request_handler() for i in range(1, requests)])


async def request_handler():
    async with aiohttp.ClientSession() as session:
        async with session.post('http://localhost:8080/apiv1/correct', data=data) as resp:
            await resp.text()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    start = datetime.now()
    loop.run_until_complete(benchmark())
    finish = datetime.now()
    print(finish - start)