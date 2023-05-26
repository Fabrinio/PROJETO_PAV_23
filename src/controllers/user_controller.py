from flask_restful import Resource, abort, fields, marshal_with, reqparse, request
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from ..repository.user_repository import get_user, get_users, add_user, update_user, delete_user, select_user

response_fields ={
    "user_id": fields.Integer,
    "name": fields.String,
    "age": fields.Integer,
    "gender": fields.String,
    "height": fields.Float,
    "weight": fields.Float,
}

request_parser = reqparse.RequestParser(bundle_errors=True)
request_parser.add_argument("name", type=str, help="", required=True)
request_parser.add_argument("age", type=int, help="", required=True)
request_parser.add_argument("gender", type=str, help="", required=True)
request_parser.add_argument("height", type=float, help="", required=True)
request_parser.add_argument("weight", type=float, help="", required=True)

class UserItem(Resource):
    @marshal_with(response_fields)
    def get(self, user_id):
        try:
            user = get_user(user_id)
            if not user:
                abort(404, message="Resource not found")
            return user, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    def delete(self, user_id):
        try:
            delete_user(user_id)
            return "Usuário delatado com sucesso.", 204
        except UnmappedInstanceError:
            abort(404, message = "Resource not found")
        except:
            abort(500, message = "Internal Server Error")
    
    @marshal_with(response_fields)
    def put(self, user_id):
        try:
            args = request_parser.parse_args(strict=True)
            user = update_user(**args, user_id=user_id)
            return user, 200
        except(OperationalError, IntegrityError):
            abort(500, message = "Internal Server Error")

class UserList(Resource):
    @marshal_with(response_fields)
    def get(self):
        try:
            if 'name' in request.args:
                name = request.args['name']
                users = select_user(name)
                return users, 200
            else:
                users = get_users()
                return users, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @marshal_with(response_fields)
    def post(self):
        try:
            args = request_parser.parse_args(strict=True)
            user = add_user(**args)
            return user, 201
        except (OperationalError, IntegrityError):
            abort(500, message = "Internal Server Error")
