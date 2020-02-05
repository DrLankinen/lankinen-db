from src import db
from src.models import Base

class Table(Base):
    name = db.Column(db.String(144), nullable=False)
    columns = db.Column(db.String(144), nullable=False)

    def __init__(self, name, columns):
        self.name = name
        self.columns = columns