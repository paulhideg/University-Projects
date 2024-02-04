from flask_restful import Resource

"""
    You need to register TestResource with
    api.add_resource in app.py
"""
class TestResource(Resource):

    def get(self,id: int):
        return {"msg": id}
