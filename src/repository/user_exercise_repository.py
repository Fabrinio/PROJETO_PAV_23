import sqlalchemy
from ..models.models import User_Exercises, db
from datetime import datetime

def get_user_exercises() -> sqlalchemy.orm.query.Query:
    user_exercises = db.session.query(User_Exercises).all()
    return user_exercises

def get_user_exercise(user_exercises_id: int) -> User_Exercises:
    user_exercise = db.session.query(User_Exercises).get(user_exercises_id)
    return user_exercise

def delete_user_exercise(user_exercises_id: int):
    user_exercise = db.session.query(User_Exercises).get(user_exercises_id)
    db.session.delete(user_exercise)
    db.session.commit()


def add_user_exercise(id_user: int, id_exercise: int, date_str: str, duration: float, weight:float, repetitions:int, user_exercises_id: int) -> User_Exercises:
    user_exercise = db.session.query(User_Exercises).get(user_exercises_id)

    date = datetime.strptime(date_str, "%Y-%m-%d")

    user_exercise.id_user = id_user
    user_exercise.id_exercise = id_exercise
    user_exercise.date = date
    user_exercise.duration = duration
    user_exercise.weight = weight
    user_exercise.repetitions = repetitions

    db.session.commit()
    
def update_user_exercise(id_user: int, id_exercise: int, date_str: str, duration: float, weight:float, repetitions:int, user_exercises_id: int) -> User_Exercises:
    user_exercise = db.session.query(User_Exercises).get(user_exercises_id)

    date = datetime.strptime(date_str, "%Y-%m-%d")

    user_exercise.id_user = id_user
    user_exercise.id_exercise = id_exercise
    user_exercise.date = date
    user_exercise.duration = duration
    user_exercise.weight = weight
    user_exercise.repetitions = repetitions
   

    db.session.commit()
    
    return user_exercise

