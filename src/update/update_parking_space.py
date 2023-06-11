from PyQt5 import QtWidgets
from UI.update_ui.update_parking_space_ui import Ui_update_parking_space
from src.db_config import db_connect
import sys

class UpdateParkingSpace(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_update_parking_space()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.update_parking_space_clicked)

    def update_parking_space_clicked(self):
        parking_space_id = self.ui.parking_space_id_lineEdit.text()
        building_id = self.ui.building_id.text()
        house_id = self.ui.house_id.text()
        license = self.ui.license.text()
        parking_fee = self.ui.parking_fee.text()
        values = [building_id, house_id, license, parking_fee, parking_space_id]
        conn = db_connect()
        cursor = conn.cursor()
        sql = '''UPDATE parking_spaces SET building_id = %s, house_id = %s, license_plate = %s, parking_fee = %s WHERE parking_space_id = %s;'''
        cursor.execute(sql, values)
        conn.commit()
        conn.close()

        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    update_parking_space = UpdateParkingSpace()
    update_parking_space.show()
    sys.exit(app.exec_())