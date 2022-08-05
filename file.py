import asyncio
from time import sleep


# async def foo():
#     for i in range(1, 11):
#         print(i)
#         await asyncio.sleep(1)
#
#
# async def main():
#     loop = asyncio.get_event_loop()
#     tasks = [loop.create_task(foo()) for i in range(10)]
#     for task in tasks:
#         await task
#
#
# if __name__=="__main__":
#     asyncio.run(main())

def foo():
    sleep(1)


async def main():
    await asyncio.to_thread(foo)
    print(1)


if __name__ == "__main__":
    asyncio.run(main())








