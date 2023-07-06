from .Database import db

class CauHoiDongNghia(db.Model):
    __tablename__ = 'CauHoiDongNghia'
    idCauHoiDongNghia = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idNhan = db.Column(db.Integer, nullable=False)
    CauHoi = db.Column(db.String(1000), nullable=False)

    def __init__(self, idNhan, CauHoi):
        self.idNhan = idNhan
        self.CauHoi = CauHoi
