from pydantic import BaseModel, Field
from datetime import datetime


class ArticleSchema(BaseModel):
    category_id: int = Field(ge=1, default=None)
    title: str = Field(max_length=24)
    body: str = Field(max_length=50)
    date_created: datetime
    author_id: int


class ArticleInDBSchema(ArticleSchema):
    id: int = Field(ge=1)