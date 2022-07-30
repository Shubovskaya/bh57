from datetime import datetime

from sqlalchemy import Column, SmallInteger, VARCHAR, TIMESTAMP, Boolean, Integer, ForeignKey, Text
from sqlalchemy .orm import declarative_base

Base = declarative_base()

class User(Base):
    tablename: str = "users"

    id = Column(Integer, primary_key=True)
    user_name = Column(VARCHAR(24), unique=True, nullable=False)
    hashed_password = Column(Text, nullable=False)
    is_blocked = Column(Boolean, default=False)

class Category(Base):
    tablename: str = "categories"

    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(24), nullable=False)
    parent_id = Column(SmallInteger, ForeignKey("categories.id", ondelete="CASCADE"))

class Article(Base):
    tablename: str = "articles"

    id = Column(SmallInteger, primary_key=True)
    category_id = Column(
        SmallInteger,
        ForeignKey("categories.id", ondelete="CASCADE"),
        nullable=False
    )
    title = Column(VARCHAR(50), nullable=False)
    body = Column(VARCHAR(1024), nullable=False)
    date_created = Column(TIMESTAMP, default=datetime.utcnow())

class UserArticle(Base):
    tablename: str = "user_articles"
    id = Column(SmallInteger, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="NO ACTION"), nullable=False)
    article_id = Column(Integer, ForeignKey("articles.id", ondelete="CASCADE"), nullable=False)