from .Database import db

class NguoiDung(db.Model):
    __tablename__ = 'NguoiDung'

    idUser = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(100), nullable=False)
    Password = db.Column(db.String(100), nullable=False)
    Hoten = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phoneNumber = db.Column(db.String(100), nullable=False)
    typeUser = db.Column(db.String(100), nullable=False)
    LevelUser = db.Column(db.String(100), nullable=False)

    def __init__(self, UserName, Password, Hoten, email, phoneNumber, typeUser, LevelUser):
        self.UserName = UserName
        self.Password = Password
        self.Hoten = Hoten
        self.email = email
        self.phoneNumber = phoneNumber
        self.typeUser = typeUser
        self.LevelUser = LevelUser
