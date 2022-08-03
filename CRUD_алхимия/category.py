from sqlalchemy import select, update, delete, or_, and_
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models import create_session, Category, Article
from schemas import CategoryInDBSchema, CategorySchema


class CRUDCategory(object):

    @staticmethod
    @create_session
    def add(category: CategorySchema, session: Session = None) -> CategoryInDBSchema | None:
        category = Category(**category.dict())
        session.add(category)
        try:
            session.commit()
        except IntegrityError:
            pass
        else:
            session.refresh(category)
            return CategoryInDBSchema(**category.__dict__)

    @staticmethod
    @create_session
    def get(category_id: int, session: Session = None) -> CategoryInDBSchema | None:
        category = session.execute(
            select(Category)
            .where(Category.id == category_id)
        )
        category = category.first()
        if category:
            return CategoryInDBSchema(**category[0].__dict__)

    @staticmethod
    @create_session
    def get_all(parent_id: int = None, session: Session = None) -> CategoryInDBSchema | list:
        if parent_id:
            categories = session.execute(
                select(Category)
                .where(Category.parent_id == parent_id)
                .order_by(Category.id)
            )
        else:
            categories = session.execute(
                select(Category)
                .order_by(Category.id)
            )
        return [CategoryInDBSchema(**category[0].__dict__) for category in categories]

    @staticmethod
    @create_session
    def delete(category_id: int, session: Session = None) -> None:
        session.execute(
            delete(Category)
            .where(Category.id == category_id)
        )
        session.commit()

    @staticmethod
    @create_session
    def update(
            category: CategoryInDBSchema,
            session: Session = None
    ) -> bool:
        session.execute(
            update(Category)
            .where(Category.id == category.id)
            .values(**category.dict())
            )

        try:
            session.commit()
        except IntegrityError:
            return False
        else:
            return True

    @staticmethod
    @create_session
    def get_articles(category_id: int, session: Session = None) -> list[tuple[Category, Article]]:
        response = session.execute(
            select(Category, Article)
            .join(Article, Category.id == Article.category_id)
            .where(Category.id == category_id)
        )
        return response.all()

