from .Database import db

class NgonNgu(db.Model):
    __tablename__ = 'NgonNgu'
    idNgonNgu = db.Column(db.Integer, primary_key=True, autoincrement=True)
    NgonNgu = db.Column(db.String(30), nullable=False)

    def __init__(self, NgonNgu):
        self.NgonNgu = NgonNgu