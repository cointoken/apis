import asyncio
import time
import requests


async def say_after(delay,what):
	await asyncio.sleep(delay)
	print(what)


async def get_baidu():
	c = requests.get('http://www.baidu.com')
	print(c.content)


async def get_bing():
	c = requests.get('http://bing.com')
	print(c.content)


async def main():
    task1 = asyncio.create_task(get_baidu())
    task2 = asyncio.create_task(get_bing())
    print('started at',time.strftime('%X'))
    await task1
    await task2
    print('finished at',time.strftime('%X'))

asyncio.run(main())
