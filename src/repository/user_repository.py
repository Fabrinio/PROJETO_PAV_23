import sqlalchemy
from ..models.models import User, db

def get_users() -> sqlalchemy.orm.query.Query:
    users = db.session.query(User).all()
    return users

def get_user(user_id: int) -> User:
    user = db.session.query(User).get(user_id)
    return user

def delete_user(user_id: int):
    user = db.session.query(User).get(user_id)
    db.session.delete(user)
    db.session.commit()


def add_user(name: str, age: int, gender: str, height: float, weight: float, user_user_id: int) -> User:
    user = db.session.query(User).get(user_user_id)

    user.name = name
    user.age = age
    user.gender = gender
    user.height = height
    user.weight = weight

    db.session.commit()
    
def update_user(name: str, age: int, gender: str, height: float, weight: float, user_id: int) -> User:
    user = db.session.query(User).get(user_id)

    user.name = name
    user.age = age
    user.gender = gender
    user.height = height
    user.weight = weight

    db.session.commit()
    
    return user

def  select_user(name: str) -> sqlalchemy.orm.query.Query:
    print(name)
    user = db.session.query(User).filter_by(name=name).all()
    return user

