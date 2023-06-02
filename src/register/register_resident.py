import sys
from PyQt5 import QtWidgets

from UI.register_ui.register_resident_ui import Ui_register_resident
from src.db_config import db_connect

class  RegisterResident(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_register_resident()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.register_resident_clicked)



    def register_resident_clicked(self):
        print("register_resident_clicked")
        email = self.ui.lineEdit.text()
        name = self.ui.lineEdit_2.text()
        employer = self.ui.lineEdit_3.text()
        family_size = self.ui.lineEdit_4.text()
        values = [email, name, employer, int(family_size)]
        conn = db_connect()
        cursor = conn.cursor()
        sql = '''INSERT INTO residents (email, owner_name, employer, family_size) VALUES (%s, %s, %s, %s);'''
        cursor.execute(sql, values)
        conn.commit()
        conn.close()

        print(email, name, employer, family_size)
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    register_resident = RegisterResident()
    register_resident.show()
    sys.exit(app.exec_())
