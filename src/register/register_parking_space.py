from src.db_config import db_connect
from PyQt5 import QtWidgets
from UI.register_ui.register_parking_space_ui import Ui_register_parking_space
import sys


class RegisterParkingSpace(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_register_parking_space()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.register_parking_space_clicked)

    def register_parking_space_clicked(self):
        print("register_parking_space_clicked")
        building_id = self.ui.building_id.text()
        house_id = self.ui.house_id.text()
        parking_fee = self.ui.parking_fee.text()
        values = [building_id, house_id, parking_fee]
        conn = db_connect()
        cursor = conn.cursor()
        sql = '''INSERT INTO parking_spaces (building_id, house_id, parking_fee) VALUES (%s, %s, %s);'''
        cursor.execute(sql, values)
        conn.commit()
        conn.close()

        print(building_id, house_id, parking_fee)
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    register_parking_space = RegisterParkingSpace()
    register_parking_space.show()
    sys.exit(app.exec_())
