from flask_restful import Resource, reqparse
from controller.public_list import public_list_controller
from repository.database_model import *


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

class PublicListResourceGetAll(Resource):

    def get(self):
        l_json = DestinationSchema(many=True).dump(public_list_controller.get_all())

        return {"destination": l_json}

destination_parser = reqparse.RequestParser()
destination_parser.add_argument("title", type = str)
destination_parser.add_argument("description", type = str)
destination_parser.add_argument("image", type = str)
destination_parser.add_argument("geolocation", type = str)

class PublicListResourceAdd(Resource):

    """
        title = db.Column(db.String(100))
        description = db.Column(db.String(100))
        image = db.Column(db.String(500)) # link to the image
        geolocation = db.Column(db.String(100))
        start_date = db.Column(db.String(100))
        end_date = db.Column(db.String(100))
    """

    def put(self):
        destination_dict = destination_parser.parse_args()
        id = public_list_controller.add(destination_dict)
        return {"id": id}

