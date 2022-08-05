from sqlalchemy import select, update, delete, or_, and_
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models import create_session, Category, Article
from schemas import ArticleInDBSchema, ArticleSchema

class CRUDArticle(object):

    @staticmethod
    @create_session
    def add(article: ArticleSchema, session: Session = None) -> ArticleInDBSchema | None:
        article = Article(**article.dict())
        session.add(article)

        # try:
        #     session.commit()
        # except IntegrityError:
        #     pass
        # else:
        #     session.refresh(article)
        #     return ArticleInDBSchema(**article.__dict__)