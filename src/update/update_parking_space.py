from PyQt5 import QtWidgets
from UI.update_ui.update_parking_space_ui import Ui_update_parking_space
from src.db_config import db_connect
import sys

def GetParkingSpaceId():
    conn = db_connect()
    cursor = conn.cursor()
    sql = '''SELECT parking_space_id FROM parking_spaces;'''
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def GetParkingSpaceInfo(parking_space_id):
    conn = db_connect()
    cursor = conn.cursor()
    sql = '''SELECT building_id, house_id,license_plate,parking_fee FROM parking_spaces WHERE parking_space_id = %s;'''
    cursor.execute(sql, (parking_space_id,))
    result = cursor.fetchone()
    return result

class UpdateParkingSpace(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_update_parking_space()
        self.ui.setupUi(self)
        self.ui.parking_space_id_comboBox.addItems([str(i[0]) for i in GetParkingSpaceId()])

        parking_space_id = self.ui.parking_space_id_comboBox.currentText()
        building_id, house_id, license_plate, parking_fee = GetParkingSpaceInfo(parking_space_id)
        self.ui.building_id.setText(str(building_id))
        self.ui.house_id.setText(str(house_id))

        self.ui.license.setPlaceholderText(str(license_plate))
        self.ui.parking_fee.setPlaceholderText(str(parking_fee))


        self.ui.parking_space_id_comboBox.currentIndexChanged.connect(self.update_building_id_house_id)
        self.ui.pushButton.clicked.connect(self.update_parking_space_clicked)

    def update_parking_space_clicked(self):
        parking_space_id = self.ui.parking_space_id_comboBox.currentText()
        building_id = self.ui.building_id.text()
        house_id = self.ui.house_id.text()
        license = self.ui.license.text()
        parking_fee = self.ui.parking_fee.text()
        values = [building_id, house_id, license, parking_fee, parking_space_id]
        conn = db_connect()
        cursor = conn.cursor()
        try:
            sql = '''UPDATE parking_spaces SET building_id = %s, house_id = %s, license_plate = %s, parking_fee = %s WHERE parking_space_id = %s;'''
            cursor.execute(sql, values)
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)

        else:
            print('update parking space success')

    def update_building_id_house_id(self):

        print("update_building_id_house_id")
        parking_space_id = self.ui.parking_space_id_comboBox.currentText()
        building_id, house_id, license_plate, parking_fee = GetParkingSpaceInfo(parking_space_id)
        self.ui.building_id.setText(str(building_id))
        self.ui.house_id.setText(str(house_id))

        self.ui.license.setPlaceholderText(str(license_plate))
        self.ui.parking_fee.setPlaceholderText(str(parking_fee))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    update_parking_space = UpdateParkingSpace()
    update_parking_space.show()
    sys.exit(app.exec_())