from UI.register_ui.register_building_ui import Ui_register_building
import sys
from PyQt5 import QtWidgets
from src.db_config import db_connect


class RegisterBuilding(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_register_building()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.register_building_clicked)

    def register_building_clicked(self):
        print("register_building_clicked")
        building_id = self.ui.lineEdit.text()
        mag_staff = self.ui.lineEdit_2.text()
        values = [building_id, mag_staff]
        conn = db_connect()
        cursor = conn.cursor()
        sql = '''INSERT INTO buildings (building_id, property_id) VALUES (%s, %s);'''
        try:
            cursor.execute(sql, values)
            conn.commit()
            conn.close()

        except Exception as e:
            print(e)

        else:
            print('register_building_success')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    register_building = RegisterBuilding()
    register_building.show()
    sys.exit(app.exec_())
