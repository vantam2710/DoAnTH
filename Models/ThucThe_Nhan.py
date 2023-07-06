from .Database import db

class ThucThe_Nhan(db.Model):
    __tablename__ = 'ThucThe_Nhan'
    idThucThe = db.Column(db.Integer, primary_key=True)
    idNhan = db.Column(db.Integer, primary_key=True)

    def __init__(self, idThucThe, idNhan):
        self.idThucThe = idThucThe
        self.idNhan = idNhan