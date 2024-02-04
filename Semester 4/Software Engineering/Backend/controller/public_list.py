from repository.database_model import Destination, PublicList, db

class PublicListController:
    def get_all(self):
        statement = db.select(PublicList)
        result = db.session.execute(statement).all()
        l_dest = []
        l = []
        for r in result:
            l.append(r[0])
            statement = db.select(Destination).where(Destination.id == r[0].destination_id)
            result = db.session.execute(statement).first()
            l_dest.append(result[0])

        return l_dest

    def add(self,destination_dict):
        destin = Destination(title = destination_dict["title"], 
                             description = destination_dict["description"], \
                             image = destination_dict["image"], \
                             geolocation = destination_dict["geolocation"], \
                             start_date =  "", \
                             end_date = "")
        db.session.add(destin)
        db.session.commit()

        public_list_item = PublicList(destination_id = destin.id)

        db.session.add(public_list_item)
        db.session.commit()
        return destin.id

public_list_controller = PublicListController()
