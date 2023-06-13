from src.db_config import db_connect
from PyQt5 import QtWidgets
from UI.delete_ui.del_resident_ui import Ui_del_resident
import sys


class DelResident(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_del_resident()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.del_resident_clicked)

    def del_resident_clicked(self):
        print("del_resident_clicked")
        resident_id = self.ui.lineEdit.text()
        name = self.ui.lineEdit_2.text()
        if resident_id == '' or name == '':
            print('resident_id or name are empty')
            return
        values = [resident_id, name]
        conn = db_connect()
        cursor = conn.cursor()
        sql = '''DELETE FROM residents WHERE resident_id = %s or owner_name = %s;'''
        try:
            cursor.execute(sql, values)
            conn.commit()
            conn.close()

        except Exception as e:
            print(e)
        print('del_resident_success')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    del_resident = DelResident()
    del_resident.show()
    sys.exit(app.exec_())
