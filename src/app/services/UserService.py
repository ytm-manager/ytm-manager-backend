from src.app.db import db
from src.app.models.UserModel import UserModel


class UserService:
    def __init__(self):
        pass

    def create_user(self, email, password):
        if self.get_user(email) is None:
            user = UserModel(email=email, password=password)
            db.session.add(user)
            db.session.commit()
        else:
            raise ValueError

    def get_user(self, email):
        user_model = UserModel.query.filter_by(email=email).first()
        print(user_model)
        return user_model
    

