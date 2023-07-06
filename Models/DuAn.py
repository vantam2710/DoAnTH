from .Database import db

class DuAn(db.Model):
    idDuAn = db.Column(db.Integer, primary_key=True, autoincrement=True)
    TenDA = db.Column(db.String(1000), nullable=False)
    idLoaiNhan = db.Column(db.String(100), nullable=False)
    idQuanLi = db.Column(db.Integer, nullable=False)
    
    def __init__(self, TenDA, idLoaiNhan, idQuanLi):
        self.TenDA = TenDA
        self.idLoaiNhan = idLoaiNhan
        self.idQuanLi = idQuanLi