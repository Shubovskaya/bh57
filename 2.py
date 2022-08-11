from aiohttp import ClientSession
from schemas import ArticleInDBSchema


class NewArticle(object):

    @staticmethod
    async def get_article():
        async with ClientSession() as session:
            response = await session.get(
                url="https://d474-80-93-191-82.eu.ngrok.io//api/1/article/get"
                # json={
                #     "title": "Alesya",
                #     "body": "description",
                #     "category_id": 1,
                #     "user_id": articles.author_id
                # }
            )
            print(await response.json())

import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(NewArticle.get_article())