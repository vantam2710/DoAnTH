from .Database import db

class VanBan(db.Model):
    __tablename__ = 'VanBan'
    idVanBan = db.Column(db.Integer, primary_key=True, autoincrement=True)
    VanBan = db.Column(db.String(1000), nullable=False)
    idNgonNgu = db.Column(db.Integer)
    idDuLieu = db.Column(db.Integer, nullable=False)
    idVanBan2_CauHoi = db.Column(db.Integer)

    def __init__(self, VanBan, idNgonNgu, idDuLieu, idVanBan2_CauHoi):
        self.VanBan = VanBan
        self.idNgonNgu = idNgonNgu
        self.idDuLieu = idDuLieu
        self.idVanBan2_CauHoi = idVanBan2_CauHoi