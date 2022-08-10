from pydantic import BaseModel, Field
from datetime import datetime


class ArticleSchema(BaseModel):
    category_id: int = Field(ge=1, default=None)
    title: str = Field(max_length=45)
    body: str = Field(max_length=1024)
    # date_created: datetime = Field(default=datetime.utcnow())
    # author_id: int
    user_id: int = Field(ge=1, default=None)


class ArticleInDBSchema(ArticleSchema):
    id: int = Field(ge=1)