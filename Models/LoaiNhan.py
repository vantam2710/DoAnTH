from sqlalchemy import DDL, CheckConstraint
from .Database import db

class LoaiNhan(db.Model):
    __tablename__ = 'LoaiNhan' 
    idLoaiNhan = db.Column(db.varchar(100), primary_key=True)
    LoaiNhan = db.Column(db.String(100), nullable=False)

    def __init__(self, LoaiNhan):
        self.LoaiNhan = LoaiNhan

