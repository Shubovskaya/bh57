from pydantic import BaseModel, Field


class ArticleSchema(BaseModel):
    category_id: int = Field(ge=1, default=None)
    title: str = Field(max_length=24)
    body: str = Field(max_length=50)
    date_created: int = Field(default=None)
    author_id: int = Field(default=None)


class ArticleInDBSchema(ArticleSchema):
    id: int = Field(ge=1)