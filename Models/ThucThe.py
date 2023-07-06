from .Database import db

class ThucThe(db.Model):
    __tablename__ = 'ThucThe'
    idThucThe = db.Column(db.Integer, primary_key=True, autoincrement=True)
    TenThucThe = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, TenThucThe):
        self.TenThucThe = TenThucThe