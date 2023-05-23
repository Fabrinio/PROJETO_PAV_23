import sqlalchemy
from ..models.models import Exercises, db

def get_exercises() -> sqlalchemy.orm.query.Query:
    exercises = db.session.query(Exercises).all()
    return exercises

def get_exercise(exercise_id: int) -> Exercises:
    exercise = db.session.query(Exercises).get(exercise_id)
    return exercise

def delete_exercise(exercise_id: int):
    exercise = db.session.query(Exercises).get(exercise_id)
    db.session.delete(exercise)
    db.session.commit()


def add_exercise(name: str, description: str, dificulty: int, muscular_groups: str, exercise_id: int) -> Exercises:
    exercise = db.session.query(Exercises).get(exercise_id)

    exercise.name = name
    exercise.description = description
    exercise.dificulty = dificulty
    exercise.muscular_groups = muscular_groups

    db.session.commit()
    
def update_exercise(name: str, description: str, dificulty: int, muscular_groups: str, exercise_id: int) -> Exercises:
    exercise = db.session.query(Exercises).get(exercise_id)

    exercise.name = name
    exercise.description = description
    exercise.dificulty = dificulty
    exercise.muscular_groups = muscular_groups
   

    db.session.commit()
    
    return exercise

def  select_exercise(name: str) -> sqlalchemy.orm.query.Query:
    print(name)
    exercise = db.session.query(Exercises).filter_by(name=name).all()
    return exercise
