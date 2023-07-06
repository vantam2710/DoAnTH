from .Database import db
class DuLieu(db.Model):
    __tablename__ = 'DuLieu'
    idDuLieu = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idDuAn = db.Column(db.Integer, primary_key=True)

    def __init__(self, idDuAn):
        self.idDuAn = idDuAn