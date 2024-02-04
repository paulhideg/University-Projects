from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from repository.database_model import *
from resources.login_resource import LoginResource
from resources.public_list_resource import PublicListResourceAdd, PublicListResourceGetAll
from resources.test_recource import TestResource
from resources.user_resource import UserResourceAdd, UserResourceList

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
CORS(app)

api = Api(app)

db.init_app(app)
with app.app_context():
    db.create_all()

# register TestResource
# this is for learning purpuses only
api.add_resource(TestResource, "/test/<int:id>")

api.add_resource(LoginResource, "/login/")
api.add_resource(PublicListResourceGetAll, "/public_list/")
api.add_resource(PublicListResourceAdd, "/public_list/add/")
api.add_resource(UserResourceList,"/user/list/")
api.add_resource(UserResourceAdd,"/user/add/")


# with app.app_context():
#     dest = PublicList(destination_id=1)
#     dest2 = PublicList(destination_id=2)

#     db.session.add(dest)
#     db.session.add(dest2)
#     db.session.commit()
#     pass

if __name__ == "__main__":
    app.run(debug=True)

