from flask_restful import Resource,reqparse
from controller.credential import credential_controller

"""
    https://flask-restful.readthedocs.io/en/latest/reqparse.html

    Create a parser so we can parse the arguments which were sent to
    the endpoint

    Arguments should have the following form:
    {
        username: string
        password: string
        role: "user" | "admin"
    }
"""
login_parser = reqparse.RequestParser()
login_parser.add_argument("username",type = str)
login_parser.add_argument("password",type = str)
login_parser.add_argument("role",type = str,choices = ("user","admin"))

"""
    resposne:
        status code: 200
        {
            session_id: str -- session_id of the logged in person
        }

        status code: 500
        {
            "msg": str -- if credentials are not found
        }
    
    currently:
        there is 1 user for testing purposes
        username: "user"
        password: "user"

        there is 1 admin for testing purposes
        username: "admin"
        password: "admin"
"""

class LoginResource(Resource):

    def post(self):
        login_dict = login_parser.parse_args()

        username = login_dict["username"]
        password = login_dict["password"]

        session_id = None

        if login_dict["role"] == "user":
            session_id = credential_controller.user_login(username,password)
        elif login_dict["role"] == "admin":
            session_id = credential_controller.admin_login(username,password)

        if session_id == None:
            return {"msg": "Credentials not found"}, 500


        return {"session_id": session_id}
