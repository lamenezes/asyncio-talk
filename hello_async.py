import asyncio


async def hello():
    print('hello world')


async def hello2():
    await asyncio.sleep(2)
    print('hello world 2')


loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(hello2(), hello())
)
