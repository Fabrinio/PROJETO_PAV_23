from flask_restful import Resource, abort, fields, marshal_with, reqparse, request
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from ..repository.exercise_repository import get_exercise, get_exercises, add_exercise, update_exercise, delete_exercise, select_exercise

response_fields ={
    "exercise_id": fields.Integer,
    "name": fields.String,
    "description": fields.String,
    "dificulty": fields.Integer,
    "muscular_groups": fields.String
}

request_parser = reqparse.RequestParser(bundle_errors=True)
request_parser.add_argument("name", type=str, help="", required=True)
request_parser.add_argument("description", type=str, help="", required=True)
request_parser.add_argument("dificulty", type=int, help="", required=True)
request_parser.add_argument("muscular_groups", type=str, help="", required=True)

class ExerciseItem(Resource):
    @marshal_with(response_fields)
    def get(self, exercise_id):
        try: 
            exercise = get_exercise(exercise_id)
            if not exercise:
                abort(404, message="Resource not found")
            return exercise, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    def delete(self, exercise_id):
        try:
            delete_exercise(exercise_id)
            return "Exercício delatado com sucesso.", 204
        except UnmappedInstanceError:
            abort(404, message="Resource not found")
        except:
            abort(500, message="Internal Server Error")

    @marshal_with(response_fields)
    def put(self, exercise_id):
        try:
            args = request_parser.parse_args(strict=True)
            exercise = update_exercise(**args, exercise_id=exercise_id)
            return exercise, 200
        except(OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")

class ExerciseList(Resource):
    @marshal_with(response_fields)
    def get(self):
        try:
            if request.args:
                select_exercise(request.args.get('[name]'))
            else:
                return get_exercises(), 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @marshal_with(response_fields)
    def post(self):
        try:
            args = request_parser.parse_args(strict=True)
            exercise = add_exercise(**args)
            return exercise, 201
        except(OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")


