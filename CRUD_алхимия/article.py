from sqlalchemy import select, update, delete

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from models import create_async_session, Category, Article
from schemas import ArticleInDBSchema, ArticleSchema


class CRUDArticle(object):

    @staticmethod
    @create_async_session
    async def add(article: ArticleSchema, session: AsyncSession = None) -> ArticleInDBSchema | None:
        article = Article(**article.dict())
        session.add(article)

        try:
            await session.commit()
        except IntegrityError:
            pass
        else:
            await session.refresh(article)
            return ArticleInDBSchema(**article.__dict__)

    @staticmethod
    @create_async_session
    async def get(article_id: int, session: AsyncSession = None) -> ArticleInDBSchema | None:
        article = await session.execute(
            select(Article)
            .where(Article.id == article_id)
        )
        article = article.first()
        if article:
            return ArticleInDBSchema(**article[0].__dict__)

    @staticmethod
    @create_async_session
    async def get_all(category_id: int = None, session: AsyncSession = None) -> ArticleInDBSchema | list:
        if category_id:
            articles = await session.execute(
                select(Article)
                .where(Article.category_id == category_id)
                .order_by(Article.id)
            )
        else:
            articles = await session.execute(
                select(Article)
                .order_by(Article.id)
            )
        return [ArticleInDBSchema(**article[0].__dict__) for article in articles]

    @staticmethod
    @create_async_session
    async def delete(article_id: int, session: AsyncSession = None) -> None:
        await session.execute(
            delete(Article)
            .where(Article.id == article_id)
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def update(
            article: ArticleInDBSchema,
            session: AsyncSession = None
    ) -> bool:
        await session.execute(
            update(Article)
            .where(Article.id == article.id)
            .values(**article.dict())
        )

        try:
            await session.commit()
        except IntegrityError:
            return False
        else:
            return True

    @staticmethod
    @create_async_session
    async def get_articles(category_id: int, session: AsyncSession = None) -> list[tuple[Category, Article]]:
        response = await session.execute(
            select(Category, Article)
            .join(Article, Category.id == Article.category_id)
            .where(Category.id == category_id)
        )
        return response.all()
