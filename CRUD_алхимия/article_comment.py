from sqlalchemy import select, update, delete, or_, and_
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models import create_session, ArticleComment
from schemas import ArticleCommentInDBSchema, ArticleCommentSchema


class CRUDArticleComment(object):

    @staticmethod
    @create_session
    def add(article_comments: ArticleCommentSchema, session: Session = None) -> ArticleCommentInDBSchema | None:
        article_comments = ArticleComment(**article_comments.dict())
        session.add(article_comments)
        try:
            session.commit()
        except IntegrityError:
            pass
        else:
            session.refresh(article_comments)
            return ArticleCommentInDBSchema(**article_comments.__dict__)