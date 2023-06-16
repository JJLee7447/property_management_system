from src.db_config import db_connect
from PyQt5 import QtWidgets
from UI.register_ui.register_house_ui import Ui_register_house

def GetBuildingId():
    conn = db_connect()
    cursor = conn.cursor()
    sql = '''SELECT building_id FROM buildings;'''
    cursor.execute(sql)
    res = cursor.fetchall()
    conn.close()
    return res


class RegisterHouse(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_register_house()
        self.ui.setupUi(self)
        self.ui.building_id_comboBox.addItems([str(i[0]) for i in GetBuildingId()])

        self.ui.pushButton.clicked.connect(self.register_btn_clicked)

    def register_btn_clicked(self):
        print("is_ok_btn_clicked")
        try:
            building_id = self.ui.building_id_comboBox.currentText()
            area = self.ui.area.text()
            resident_id = self.ui.resident_id.text()
            property_fee = float(area) * 1.25
            values = [building_id, area, resident_id, property_fee]
            conn = db_connect()
            cursor = conn.cursor()
            sql = '''INSERT INTO house (building_id, area, resident_id,property_fee) VALUES (%s, %s, %s,%s);'''
            cursor.execute(sql, values)
            conn.commit()
            conn.close()

        except Exception as e:
            print(e)

        else:
            print('register_house_success')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    register_house = RegisterHouse()
    register_house.show()
    sys.exit(app.exec_())
