from aiohttp import ClientSession


class NewArticle(object):

    @staticmethod
    async def put_article():
        async with ClientSession() as session:
            response = await session.get(
                url="https://d474-80-93-191-82.eu.ngrok.io/api/1/article/add",
                # json={
                #     "title": "Alesya",
                #     "body": "string",
                #     "category_id": 1,
                #     "user_id": 1
                # }
            )
            print(await response.json())

import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(NewArticle.put_article())