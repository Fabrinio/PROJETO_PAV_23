from flask_restful import Resource, abort, fields, marshal_with, reqparse, request
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from ..repository.user_exercise_repository import get_user_exercise, get_user_exercises, add_user_exercise, update_user_exercise, delete_user_exercise

response_fields={
    "user_exercises_id": fields.Integer,
    "id_user": fields.Integer,
    "id_exercise": fields.Integer,
    "date": fields.String,
    "duration": fields.Float,
    "weight": fields.Float,
    "repetitions": fields.Integer
}

request_parser = reqparse.RequestParser(bundle_errors=True)
request_parser.add_argument("id_user", type=int, help="", required=True)
request_parser.add_argument("id_exercise", type=int, help="", required=True)
request_parser.add_argument("date", type=str, help="", required=True)
request_parser.add_argument("duration", type=float, help="", required=True)
request_parser.add_argument("weight", type=float, help="", required=True)
request_parser.add_argument("repetitions", type=int, help="", required=True)

class User_ExerciseItem(Resource):
    @marshal_with(response_fields)
    def get(self, user_exercises_id):
        try:
            user_exercise = get_user_exercise(user_exercises_id)
            if not user_exercise:
                abort(404, message="Resource not found")
            return user_exercise, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    def delete(self, user_exercises_id):
        try:
            delete_user_exercise(user_exercises_id)
            return "Deletado com sucesso.", 204
        except UnmappedInstanceError:
            abort(404, message = "Resource not found")
        except:
            abort(500, message = "Internal Server Error")
    
    @marshal_with(response_fields)
    def put(self, user_exercises_id):
        try:
            args = request_parser.parse_args(strict=True)
            # Remova o argumento 'date' do dicionário 'args'
            date = args.pop('date', None)
            user_exercise = update_user_exercise(date_str=date, user_exercises_id=user_exercises_id, **args)
            return user_exercise, 200
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")


class User_ExerciseList(Resource):
    @marshal_with(response_fields)
    def get(self):
        try:
                return get_user_exercises(), 200
        except OperationalError:
            abort(500, message = "Internal Server Error")

    @marshal_with(response_fields)
    def post(self):
        try:
            args = request_parser.parse_args(strict=True)
            user_exercise = add_user_exercise(**args)
            return user_exercise, 201
        except (OperationalError, IntegrityError):
            abort(500, message = "Internal Server Error")
