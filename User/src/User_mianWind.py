from User.ui.User_mianWind_ui import Ui_User_mainWind
from PyQt5 import QtWidgets, QtCore
from src.db_config import db_connect
import sys
from PyQt5.QtGui import QFont
from User.src.property_fee import PropertyFee
from User.src.parking_fee import ParkingFee


def search_resident_info(email):
    conn = db_connect()
    cursor = conn.cursor()
    sql = '''SELECT owner_name,email,resident_id FROM residents WHERE email = %s'''
    cursor.execute(sql, (email,))
    res = cursor.fetchone()
    if res:
        owner_name, email, resident_id = res
        return owner_name, email, resident_id
    else:
        return None


class UserMainWind(QtWidgets.QMainWindow, Ui_User_mainWind):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.email = None
        self.resident_id = None
        self.property_fee_ui = None
        self.parking_fee_ui = None

        self.prpperty_fee_pushButton.clicked.connect(self.show_property_fee)
        self.parking_fee_pushButton.clicked.connect(self.show_pariking_fee)


    def show_property_fee(self):
        print("property fee")
        self.property_fee_ui = PropertyFee()
        self.property_fee_ui.Get_resident_id(self.resident_id)
        self.property_fee_ui.show()


    def show_pariking_fee(self):
        print("parking fee")
        self.parking_fee_ui = ParkingFee()
        self.parking_fee_ui.Get_resident_id(self.resident_id)
        self.parking_fee_ui.show()

    def set_person_info(self,  email):
        name = search_resident_info(email)[0]
        email = search_resident_info(email)[1]
        resident_id = search_resident_info(email)[2]
        self.email = email
        self.resident_id = resident_id
        print(name)
        font = QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.person_info_label.setFont(font)
        self.person_info_label.setStyleSheet("color: rgb(0, 0, 0);" "background-color: rgb(0, 0, 0);")
        self.person_info_label.setText(f'欢迎您，{name}')
        return email


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    user_main_wind = UserMainWind()
    user_main_wind.show()
    sys.exit(app.exec_())
