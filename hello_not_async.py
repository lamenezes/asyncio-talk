import asyncio
import time


async def hello():
    print('hello world')


async def hello2():
    time.sleep(2)
    print('hello world 2')


loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(hello2(), hello())  # not really async
)
