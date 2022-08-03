from sqlalchemy import select, update, delete, or_, and_
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models import create_session, Category, Article


class CRUDCategory(object):

    @staticmethod
    @create_session
    def add(name: str, parent_id: int, session: Session = None) -> Category | None:
        category = Category(name=name, parent_id=parent_id)
        session.add(category)
        try:
            session.commit()
        except IntegrityError:
            pass
        else:
            session.refresh(category)
            return category

    @staticmethod
    @create_session
    def get(category_id: int, session: Session = None) -> Category | None:
        category = session.execute(
            select(Category)
            .where(Category.id == category_id)
        )
        category = category.first()
        if category:
            return category[0]

    @staticmethod
    @create_session
    def get_all(parent_id: int = None, session: Session = None) -> Category | list:
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
        return [category[0] for category in categories]

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
            category_id: int,
            name: str = None,
            parent_id: int = None,
            session: Session = None
    ) -> bool:
        session.execute(
            update(Category)
            .where(Category.id == category_id)
            .values(
                name=name if name else Category.name,
                parent_id=parent_id if parent_id else Category.parent_id
            )
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

