from CRUD_алхимия import CRUDCategory, CRUDArticle, ArticleSchema
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

CRUDArticle.add(article=ArticleSchema(category_id=1, title="Студенты", body="Расписание", date_created=datetime, author_id=1))

