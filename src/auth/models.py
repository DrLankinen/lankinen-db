from src import db
from src.models import Base

class User(Base):

    __tablename__ = "account"

    email = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    databases = db.relationship('Database', backref='account', lazy=True)

    def __init__(self, email, password):
        self.email = email
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True