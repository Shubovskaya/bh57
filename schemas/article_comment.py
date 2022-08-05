from pydantic import BaseModel, Field
from datetime import datetime


class ArticleComment(BaseModel):
    user_id: int = Field(ge=1, default=None)
    article_id: int = Field(ge=1, default=None)
    comment: str = Field(max_length=140)
    date_created: datetime = Field(default=datetime.utcnow())


class ArticleCommentInDBSchema(ArticleCommentSchema):
    id: int = Field(ge=1)