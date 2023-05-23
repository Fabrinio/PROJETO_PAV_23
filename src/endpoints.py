from .controllers.user_controller import UserItem, UserList
from .controllers.exercise_controller import ExerciseItem, ExerciseList
from .controllers.user_exercise_controller import User_ExerciseItem, User_ExerciseList

def initialize_endpoints(api):
    api.add_resource(UserItem, "/user/<int:user_id>")
    api.add_resource(UserList, "/user")

    api.add_resource(ExerciseItem, "/exercise/<int:exercise_id>")
    api.add_resource(ExerciseList, "exercise")

    api.add_resource(User_ExerciseItem, "/user_exercise/<int:user_exercises_id>")
    api.add_resource(User_ExerciseList, "user_exercise")