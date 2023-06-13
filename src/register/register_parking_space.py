from src.db_config import db_connect
from PyQt5 import QtWidgets
from UI.register_ui.register_parking_space_ui import Ui_register_parking_space
import sys


def GetBuildingId():
    conn = db_connect()
    cursor = conn.cursor()
    sql = '''SELECT building_id FROM buildings;'''
    cursor.execute(sql)
    building_ids = cursor.fetchall()
    conn.close()
    return building_ids

class RegisterParkingSpace(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_register_parking_space()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.register_parking_space_clicked)
        self.ui.building_id_comboBox.addItems([str(i[0]) for i in GetBuildingId()])
        self.ui.building_id_comboBox.currentIndexChanged.connect(self.update_house_id)
        self.ui.house_id_comboBox.currentIndexChanged.connect(self.update_resident_id)

    def register_parking_space_clicked(self):
        print("register_parking_space_clicked")
        conn = db_connect()
        cursor = conn.cursor()
        building_id = self.ui.building_id_comboBox.currentText()
        house_id = self.ui.house_id_comboBox.currentText()
        license_plate = self.ui.license_plate.text()
        try:
            sql1 = '''SELECT resident_id FROM build_house_resident WHERE building_id = %s AND house_id = %s;'''
            values1 = [building_id, house_id]
            cursor.execute(sql1, values1)
            resident_id = cursor.fetchone()[0]
            parking_fee = self.ui.parking_fee.text()
            values = [building_id, house_id, license_plate,parking_fee, resident_id]
            sql2 = '''INSERT INTO parking_spaces (building_id, house_id, license_plate,parking_fee,resident_id) VALUES (%s, %s, %s, %s, %s);'''
            cursor.execute(sql2, values)
            conn.commit()

        except Exception as e:
            print(e)
            conn.rollback()

        else:
            conn.close()
            print("register_parking_space success")

    def update_house_id(self):
        building_id = self.ui.building_id_comboBox.currentText()
        conn = db_connect()
        cursor = conn.cursor()
        sql = '''SELECT house_id FROM house WHERE building_id = %s;'''
        cursor.execute(sql, (building_id,))
        house_ids = cursor.fetchall()
        conn.close()
        self.ui.house_id_comboBox.clear()
        self.ui.house_id_comboBox.addItems([str(i[0]) for i in house_ids])

    def update_resident_id(self):
        building_id = self.ui.building_id_comboBox.currentText()
        house_id = self.ui.house_id_comboBox.currentText()
        conn = db_connect()
        cursor = conn.cursor()
        sql = '''SELECT resident_id FROM build_house_resident WHERE building_id = %s AND house_id = %s;'''
        cursor.execute(sql, (building_id, house_id))
        resident_id = cursor.fetchone()
        conn.close()
        self.ui.resident_id_lineEdit.setText(str(resident_id[0]))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    register_parking_space = RegisterParkingSpace()
    register_parking_space.show()
    sys.exit(app.exec_())
