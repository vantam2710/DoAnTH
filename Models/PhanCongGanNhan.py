from .Database import db
class PhanCongGanNhan(db.Model):
    __tablename__ = 'PhanCongGanNhan'
    idDuAn = db.Column(db.Integer, primary_key=True)
    idNguoiGanNhan = db.Column(db.Integer, primary_key=True)
    TrangThai = db.Column(db.String(30))

    def __init__(self, idDuAn, idNguoiGanNhan,TrangThai):
        self.idDuAn = idDuAn
        self.idNguoiGanNhan = idNguoiGanNhan
        self.TrangThai = TrangThai
        
