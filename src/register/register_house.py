from src.db_config import db_connect
from PyQt5 import QtWidgets
from UI.register_ui.register_house_ui import Ui_register_house


class RegisterHouse(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_register_house()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.register_btn_clicked)

    def register_btn_clicked(self):
        print("is_ok_btn_clicked")
        building_id = self.ui.building_id.text()
        area = self.ui.area.text()
        resident_id = self.ui.resident_id.text()
        values = [building_id, area, resident_id]
        conn = db_connect()
        cursor = conn.cursor()
        sql = '''INSERT INTO house (building_id, area, resident_id) VALUES (%s, %s, %s);'''
        cursor.execute(sql, values)
        conn.commit()
        conn.close()

        print(building_id, area, resident_id)
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    register_house = RegisterHouse()
    register_house.show()
    sys.exit(app.exec_())
