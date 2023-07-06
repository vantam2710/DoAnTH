from flask import Flask, request, jsonify, g
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import bcrypt
import jwt
import json
import csv
import logging
import time
from functools import wraps
from Models.PhanCongGanNhan import PhanCongGanNhan
from Models.Nhan import Nhan
from Models.LoaiNhan import LoaiNhan
from Models.NguoiDung import NguoiDung
from Models.DuAn import DuAn
from Models.VanBan import VanBan
from Models.Database import db

secret_key = 'secret_key@18120113'
app = Flask(__name__)
app.secret_key = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/udpt_g8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/import-vanban', methods=['POST'])
def import_vanban():
    file = request.files['file']
    data = file.read().decode('utf-8')

    # Kiểm tra định dạng file (json hoặc csv) dựa trên phần mở rộng tệp
    if file.filename.endswith('.json'):
        try:
            json_data = json.loads(data)
            for item in json_data:
                vanban = VanBan(
                    VanBan=item['VanBan'],
                    idNgonNgu=item['idNgonNgu'],
                    idDuAn=item['idDuAn'],
                    idVanBan2=item['idVanBan2']
                )
                db.session.add(vanban)
            db.session.commit()
            return jsonify({'message': 'Dữ liệu đã được import thành công từ tệp JSON!'})
        except json.JSONDecodeError:
            return jsonify({'error': 'Định dạng JSON không hợp lệ!'})

    elif file.filename.endswith('.csv'):
        try:
            csv_data = csv.reader(data.splitlines(), delimiter=',')
            next(csv_data)  # Bỏ qua header của file CSV
            for row in csv_data:
                vanban = VanBan(
                    VanBan=row[0],
                    idNgonNgu=int(row[1]),
                    idDuAn=int(row[2]),
                    idVanBan2=int(row[3])
                )
                db.session.add(vanban)
            db.session.commit()
            return jsonify({'message': 'Dữ liệu đã được import thành công từ tệp CSV!'})
        except csv.Error:
            return jsonify({'error': 'Định dạng CSV không hợp lệ!'})

    else:
        return jsonify({'error': 'Định dạng file không được hỗ trợ!'}) 
    


    
@app.route('/them-nguoidung-duan', methods=['POST'])
def them_nguoidung_duan():
    data = request.get_json()
    idDuAn = data.get('idDuAn')
    idNguoiGanNhan = data.get('idNguoiGanNhan')
    phancong = PhanCongGanNhan(idDuAn=idDuAn, idNguoiGanNhan=idNguoiGanNhan)
    db.session.add(phancong)
    db.session.commit()
    return jsonify({'message': 'Người dùng đã được thêm vào dự án thành công!'})



@app.route('/nhan', methods=['GET'])
def get_all_nhan():
    nhans = Nhan.query.all()
    result = []
    for nhan in nhans:
        nhan_data = {
            'idNhan': nhan.idNhan,
            'idDuAn': nhan.idDuAn,
            'idNguoiGanNhan': nhan.idNguoiGanNhan,
            'NoiDung': nhan.NoiDung,
            'idNgonNgu': nhan.idNgonNgu,
            'TrangThai': nhan.TrangThai
        }
        result.append(nhan_data)
    return jsonify(result)


@app.route('/nhan/duan/<int:id_duan>', methods=['GET'])
def get_nhan_by_id_duan(id_duan):
    nhans = Nhan.query.filter_by(idDuAn=id_duan).all()
    if nhans:
        result = []
        for nhan in nhans:
            result.append({
                'idNhan': nhan.idNhan,
                'idDuAn': nhan.idDuAn,
                'idNguoiGanNhan': nhan.idNguoiGanNhan,
                'NoiDung': nhan.NoiDung,
                'idNgonNgu': nhan.idNgonNgu,
                'TrangThai': nhan.TrangThai
            })
        return jsonify(result)
    else:
        return jsonify({'message': 'Không tìm thấy nhãn cho dự án.'}), 404
    
@app.route('/nhanbynguoidung/<int:id_nguoidung>', methods=['GET'])
def search_nhan_by_nguoidung(id_nguoidung):
    nhans = Nhan.query.filter_by(idNguoiGanNhan=id_nguoidung).all()
    if nhans:
        result = []
        for nhan in nhans:
            result.append({
                'idNhan': nhan.idNhan,
                'idDuAn': nhan.idDuAn,
                'idNguoiGanNhan': nhan.idNguoiGanNhan,
                'NoiDung': nhan.NoiDung,
                'idNgonNgu': nhan.idNgonNgu,
                'TrangThai': nhan.TrangThai
            })
        return jsonify(result)
    else:
        return jsonify({'message': 'Không tìm thấy nhãn được gán bởi người dùng.'}), 404

@app.route('/nhan/<int:idNhan>', methods=['PUT'])
def update_nhan(idNhan):
    nhan = Nhan.query.get(idNhan)
    if nhan:
        data = request.get_json()
        nhan.idDuAn = data['idDuAn']
        nhan.idNguoiGanNhan = data['idNguoiGanNhan']
        nhan.NoiDung = data['NoiDung']
        nhan.idNgonNgu = data['idNgonNgu']
        nhan.TrangThai = data['TrangThai']
        db.session.commit()
        return jsonify({'message': 'Dữ liệu đã được cập nhật thành công'})
    else:
        return jsonify({'message': 'Không tìm thấy dữ liệu được gán nhãn với idNhan đã cho'})

@app.route('/nhan', methods=['POST'])
def create_nhan():
    data = request.json
    idDuAn = data.get('idDuAn')
    idNguoiGanNhan = data.get('idNguoiGanNhan')
    NoiDung = data.get('NoiDung')
    idNgonNgu = data.get('idNgonNgu')
    TrangThai = data.get('TrangThai')

    nhan = Nhan(idDuAn=idDuAn, idNguoiGanNhan=idNguoiGanNhan, NoiDung=NoiDung, idNgonNgu=idNgonNgu, TrangThai=TrangThai)
    db.session.add(nhan)
    db.session.commit()

    return jsonify({'message': 'Nhãn dữ liệu đã được gán thành công!'})

@app.route('/nhan/search', methods=['POST'])
def search_nhan():
    data = request.get_json()
    idDuAn = data['idDuAn']
    idNguoiGanNhan = data['idNguoiGanNhan']
    nhans = Nhan.query.filter_by(idDuAn=idDuAn, idNguoiGanNhan=idNguoiGanNhan).all()
    result = []
    for nhan in nhans:
        nhan_data = {
            'idNhan': nhan.idNhan,
            'idDuAn': nhan.idDuAn,
            'idNguoiGanNhan': nhan.idNguoiGanNhan,
            'NoiDung': nhan.NoiDung,
            'idNgonNgu': nhan.idNgonNgu,
            'TrangThai': nhan.TrangThai
        }
        result.append(nhan_data)
    return jsonify(result)


@app.route('/loainhan', methods=['GET'])
def get_all_loainhan():
    loainhans = LoaiNhan.query.all()
    result = []
    for loainhan in loainhans:
        loainhan_data = {
            'idLoaiNhan': loainhan.idLoaiNhan,
            'LoaiNhan': loainhan.LoaiNhan
        }
        result.append(loainhan_data)
    return jsonify(result)

@app.route('/nguoidung/<int:user_id>', methods=['GET'])
def get_nguoidung(user_id):
    nguoidung = db.session.get(NguoiDung,user_id)
    if nguoidung:
        return jsonify({
            'idUser': nguoidung.idUser,
            'UserName': nguoidung.UserName,
            'Password': nguoidung.Password,
            'Hoten': nguoidung.Hoten,
            'email': nguoidung.email,
            'phoneNumber': nguoidung.phoneNumber,
            'typeUser': nguoidung.typeUser,
            'LevelUser': nguoidung.LevelUser
        })
    else:
        return jsonify({'message': 'Người dùng không tồn tại.'}), 404

@app.route('/nguoidung/<int:user_id>', methods=['PUT'])
def update_nguoidung(user_id):
    nguoidung = db.session.get(NguoiDung,user_id)
    if nguoidung:
        data = request.json
        nguoidung.UserName = data.get('UserName', nguoidung.UserName)
        nguoidung.Password = data.get('Password', nguoidung.Password)
        nguoidung.Hoten = data.get('Hoten', nguoidung.Hoten)
        nguoidung.email = data.get('email', nguoidung.email)
        nguoidung.phoneNumber = data.get('phoneNumber', nguoidung.phoneNumber)
        nguoidung.typeUser = data.get('typeUser', nguoidung.typeUser)
        nguoidung.LevelUser = data.get('LevelUser', nguoidung.LevelUser)
        db.session.commit()
        return jsonify({'message': 'Thông tin người dùng đã được cập nhật.'})
    else:
        return jsonify({'message': 'Người dùng không tồn tại.'}), 404
