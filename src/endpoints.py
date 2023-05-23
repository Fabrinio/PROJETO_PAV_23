from .controllers.user_controller import UserItem, UserList

def initialize_endpoints(api):
    api.add_resource(UserItem, "/user/<int:user_id>")
    api.add_resource(UserList, "/user")