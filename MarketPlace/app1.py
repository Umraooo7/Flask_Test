from asyncio import tasks
import asyncio
import aiohttp
from timer import timer

URL='https://httpbin.org/uuid'

async def fetch(session, url):
    with session.get(url) as response:
        json_respone = await response.json()

        print(json_respone['uuid'])

async def main():
    with aiohttp.ClientSession() as session:
        tasks = [fetch(session, URL) for _ in range(100)]
        await asyncio.gather(*tasks)

@timer(1, 1)
def func():
    asyncio.run(main())