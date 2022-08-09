from sqlalchemy import select, update, delete, or_, and_
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models import create_session, User
from schemas import UserInDBSchema, UserSchema


class CRUDUser(object):

    @staticmethod
    @create_session
    def add(user: UserSchema, session: Session = None) -> UserInDBSchema | None:
        user = User(**user.dict())
        session.add(user)
        try:
            session.commit()
        except IntegrityError:
            pass
        else:
            session.refresh(user)
            return UserInDBSchema(**user.__dict__)
