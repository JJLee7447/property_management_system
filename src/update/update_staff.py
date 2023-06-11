from UI.update_ui.update_staff_info_ui import Ui_update_staff_info
from PyQt5 import QtWidgets
from src.db_config import db_connect
import sys


class UpdateStaff(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_update_staff_info()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.update_staff_info_clicked)

    def update_staff_info_clicked(self):
        staff_id = self.ui.staff_id_lineEdit.text()
        name = self.ui.name_editor.text()
        position = self.ui.position_combox.currentText()
        password = self.ui.password_lineEdit.text()
        values = [name, position, password, staff_id]

        conn = db_connect()
        cursor = conn.cursor()
        sql = '''UPDATE property_staff SET staff_name = %s, position = %s ,pass_word = %s where property_id = %s;'''
        cursor.execute(sql, values)
        conn.commit()
        conn.close()

        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    update_staff = UpdateStaff()
    update_staff.show()
    sys.exit(app.exec_())
