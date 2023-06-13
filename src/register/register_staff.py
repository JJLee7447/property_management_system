from PyQt5 import QtWidgets
from UI.register_ui.register_staff_ui import Ui_register_staff
import sys
from src.db_config import db_connect


class RegisterStaff(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_register_staff()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.register_staff_clicked)

    def register_staff_clicked(self):
        print("register_staff_clicked")
        staff_name = self.ui.name_editor.text()
        if staff_name == '':
            print('staff_name is empty')
            return
        position = self.ui.position_combox.currentText()
        values = [staff_name, position]
        try:
            conn = db_connect()
            cursor = conn.cursor()
            sql = '''INSERT INTO property_staff (staff_name, position) VALUES (%s, %s);'''
            cursor.execute(sql, values)
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)

        print(staff_name, position)
        print('register_staff_success')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    register_staff = RegisterStaff()
    register_staff.show()
    sys.exit(app.exec_())

# Path: src\register\register_resident.py
