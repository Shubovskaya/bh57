from aiohttp import ClientSession
from schemas import ArticleInDBSchema
from CRUD_алхимия import CRUDArticle

class NewArticle(object):

    @staticmethod
    async def put_article():
        article = CRUDArticle.get_all()
        for i in range[:len(article)]:
            async with ClientSession() as session:
                response = await session.put(
                    url="https://d474-80-93-191-82.eu.ngrok.io//api/1/article/add"
                    json={
                        "title": "Alesya",
                        "body": "description",
                        "category_id": 1,
                        "user_id": articles.author_id
                        }
                )
                print(await response.json())

import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(NewArticle.put_article())