from sqlalchemy import select, update, delete

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from models import create_async_session, User, Article, Category, ArticleComment
from schemas import UserInDBSchema, UserSchema


class CRUDUser(object):

    @staticmethod
    @create_async_session
    async def add(user: UserSchema, session: AsyncSession = None) -> UserInDBSchema | None:
        user = User(**user.dict())
        session.add(user)
        try:
            await session.commit()
        except IntegrityError:
            pass
        else:
            await session.refresh(user)
            return UserInDBSchema(**user.__dict__)

    @staticmethod
    @create_async_session
    async def get(user_id: int, session: AsyncSession = None) -> UserInDBSchema | None:
        user = await session.execute(
            select(User)
            .where(User.id == user_id)
        )
        user = user.first()
        if user:
            return UserInDBSchema(**user[0].__dict__)

    @staticmethod
    @create_async_session
    async def get_all(role_id: int = None, session: AsyncSession = None) -> UserInDBSchema | list:
        if role_id:
            users = await session.execute(
                select(Article)
                .where(Article.category_id == role_id)
                .order_by(Article.id)
            )
        else:
            users = await session.execute(
                select(Article, Category, ArticleComment)
                # .order_by(Article.id, Category.id, ArticleComment.id)
            )
        return [UserInDBSchema(**user[0].__dict__) for user in users]

    @staticmethod
    @create_async_session
    async def delete(user_id: int, session: AsyncSession = None) -> None:
        await session.execute(
            delete(User)
            .where(User.id == user_id)
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def update(
            user: UserInDBSchema,
            session: AsyncSession = None
    ) -> bool:
        await session.execute(
            update(User)
            .where(User.id == user.id)
            .values(**user.dict())
        )

        try:
            await session.commit()
        except IntegrityError:
            return False
        else:
            return True

    @staticmethod
    @create_async_session
    async def get_result(article_id: int, session: AsyncSession = None) -> list[tuple[Article, ArticleComment]]:
        response = await session.execute(
            select(Article, ArticleComment)
            .join(ArticleComment, Article.id == ArticleComment.article_id)
            .where(Article.id == article_id)
        )
        return response.all()