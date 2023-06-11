from src.db_config import db_connect
from PyQt5 import QtWidgets
from UI.update_ui.update_resident_ui import Ui_update_resident
import sys

class  UpdateResident(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_update_resident()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.update_resident_clicked)

    def update_resident_clicked(self):
        resident_id = self.ui.id_edit.text()
        email = self.ui.email_edit.text()
        name = self.ui.name_edit.text()
        employer = self.ui.employer_edit.text()
        family_size = self.ui.family_size_edit.text()
        values = [email, name, employer, int(family_size), resident_id]

        conn = db_connect()
        cursor = conn.cursor()
        sql = '''UPDATE residents SET email = %s, owner_name = %s, employer = %s, family_size = %s WHERE resident_id 
        = %s;'''
        cursor.execute(sql, values)
        conn.commit()
        conn.close()

        print(resident_id, email, name, employer, family_size)

        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    update_resident = UpdateResident()
    update_resident.show()
    sys.exit(app.exec_())