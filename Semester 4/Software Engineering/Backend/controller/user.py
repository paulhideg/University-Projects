from controller.credential import credential_controller
from repository.database_model import BucketList, Destination, SessionID
from repository.database_model import db

class UserController:
    def get_bucket_list(self, user_id: str):
        session_id: SessionID = credential_controller.check_session_id(user_id)

        if session_id == None:
            return None
        if session_id.role != "user":
            return None
        
        statement = db.select(BucketList).where(BucketList.user_id == session_id.person_id)
        result = db.session.execute(statement).all()

        l_dest = []
        l = []
        for r in result:
            l.append(r[0])
            statement = db.select(Destination).where(Destination.id == r[0].destination_id)
            result = db.session.execute(statement).first()
            l_dest.append(result[0])

        return l_dest

    def add_destination(self,user_id, destination_dict):
        session_id: SessionID = credential_controller.check_session_id(user_id)

        if session_id == None:
            return None
        if session_id.role != "user":
            return None

        destin = Destination(title = destination_dict["title"], 
                             description = destination_dict["description"], \
                             image = destination_dict["image"], \
                             geolocation = destination_dict["geolocation"], \
                             start_date =  destination_dict["start_date"], \
                             end_date = destination_dict["end_date"])
        db.session.add(destin)
        db.session.commit()

        bucket_list_item = BucketList(user_id = session_id.person_id, destination_id = destin.id)

        db.session.add(bucket_list_item)
        db.session.commit()
        return destin.id


user_controller = UserController()
