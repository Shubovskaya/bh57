from CRUD_алхимия import CRUDCategory, CRUDArticle, CRUDUser
from schemas import ArticleSchema, UserSchema, ArticleCommentSchema
from datetime import datetime


# CRUDCategory.add(name="Стейки", parent_id=1)
# CRUDCategory.add(name="Роллы", parent_id=2)
# for category in CRUDCategory.get_all():
#     print(category.name)
#     print(category.__dict__)

# category = CRUDCategory.get(category_id=1)
# print(category)
# category.name = "не вкусно"
# CRUDCategory.update(category=category)
# print(CRUDCategory.get(category_id=1))

# CRUDArticle.add(article=ArticleSchema(category_id=1, title="Студенты", body="Расписание", author_id=1))

# CRUDUser.add(user=UserSchema(user_name="Иван", hashed_password="Иванов", is_blocked=True, email="ivan@mail.ru"))
# CRUDUser.add(user=UserSchema(user_name="Sergey", hashed_password="Petrov", is_blocked=True, email="sergey@mail.ru"))

import asyncio

async def main():
    res = await CRUDUser.get_all()

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())