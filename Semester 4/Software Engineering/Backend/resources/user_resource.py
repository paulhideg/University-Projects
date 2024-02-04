from flask_restful import Resource, reqparse
from controller.user import user_controller
from repository.database_model import DestinationSchema

session_parser = reqparse.RequestParser()
session_parser.add_argument("session_id",type = str)

class UserResourceList(Resource):

    def post(self):
        session = session_parser.parse_args()["session_id"]
        l_json = DestinationSchema(many=True).dump(user_controller.get_bucket_list(session))
        return {"destination": l_json}


destination_parser = reqparse.RequestParser()
destination_parser.add_argument("session_id", type = str)
destination_parser.add_argument("title", type = str)
destination_parser.add_argument("description", type = str)
destination_parser.add_argument("image", type = str)
destination_parser.add_argument("geolocation", type = str)
destination_parser.add_argument("start_date", type = str)
destination_parser.add_argument("end_date", type = str)

class UserResourceAdd(Resource):

    def put(self):
        destination_dict = destination_parser.parse_args()
        id =  user_controller.add_destination(destination_dict["session_id"],destination_dict)
        return {"id": id}

