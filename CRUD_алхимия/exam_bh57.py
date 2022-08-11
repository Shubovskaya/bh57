from aiohttp import ClientSession
from schemas import ArticleInDBSchema
from CRUD_алхимия import CRUDArticle

class NewArticle(object):

    @staticmethod
    async def put_article():
        async with ClientSession() as session:
            json = CRUDArticle.get(article_id=3)
            response = await session.get(
                url="https://d474-80-93-191-82.eu.ngrok.io//api/1/article/add",
                json=json
            )
            print(await response.json())

import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(NewArticle.put_article())