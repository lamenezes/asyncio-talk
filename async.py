import asyncio
import time

import aiohttp


async def getn(url, n=10):
    t0 = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [
            get(url, i, session) for i in range(1, n + 1)
        ]
        # tasks = [<coroutine object 823u9821>, <coroutine object 81239213>, ...]
        await asyncio.gather(*tasks)

    print('total ellpased={:.2f}'.format(time.time() - t0))


async def get(url, i, session):
    t0 = time.time()
    async with session.get(url) as response:
        print(i, response.status, '{:.2f}'.format(time.time() - t0))


loop = asyncio.get_event_loop()
loop.run_until_complete(getn('https://httpbin.org/get'))
