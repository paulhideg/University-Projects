from repository.database_model import *
import time
from hashlib import  sha512

WEEK_IN_SECONDS = 7*24*60*60

class CredentialController:

    def user_login(self, username: str, password: str):
        """
             returns the session id or None if the user
             could not be logged in
        """
        return self.__login(username,password,User,"user")


    def admin_login(self, username: str, password: str):
        """
             returns the session id or None if the user
             could not be logged in
        """
        return self.__login(username,password,Admin,"admin")

    def __login(self,username,password,type,role):
        statement = db.select(type).where(type.username == username,type.password==password)
        result = db.session.execute(statement).all()

        if len(result) == 0:
            return None

        session_id = self.generate_session_id(username)

        user  = result[0][0]

        # Check if a session already exists
        statement = db.select(SessionID).where(SessionID.person_id == user.id)
        result = db.session.execute(statement).all()

        if len(result) == 0:
            # Need to generate a new one
            timestamp = time.time()
            session_in_db = SessionID(session_id = session_id, 
                                      person_id = user.id, 
                                      role = role,
                                      timestamp = timestamp)
            db.session.add(session_in_db)
            db.session.commit()

        else:
            # Updates the model 
            session:SessionID = result[0][0]
            session.session_id = session_id

            # Commits the update to the database
            db.session.commit()

        return session_id

    def generate_session_id(self, username: str)-> str:
        to_be_hashed = username + str(time.time())
        session_id = sha512(to_be_hashed.encode('UTF-8'))
        return session_id.hexdigest()

    def check_session_id(self, session_id: str):
        """
            parameter:
                session_id - the session id generated when somebody logs in

            returns SessionID - check database_model.py
            returns None - if the session_id is invalid
                                    
        """

        statement = db.select(SessionID).where(SessionID.session_id == session_id)
        result = db.session.execute(statement).all()

        if len(result) == 0:
            return None
        
        session: SessionID = result[0][0]

        current_time = time.time()
        session_time = session.timestamp

        """
        if current_time - session_time > WEEK_IN_SECONDS:
            db.session.delete(SessionID).where(SessionID.id == session.id)
            db.session.commit()
            return None
        """

        return session



credential_controller = CredentialController()
