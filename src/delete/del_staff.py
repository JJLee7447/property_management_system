from UI.delete_ui.del_staff_ui import Ui_del_staff
from PyQt5 import QtWidgets
from src.db_config import db_connect
import sys

class DelStaff(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_del_staff()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.delete_staff_clicked)

    def delete_staff_clicked(self):
        property_id = self.ui.staff_id_lineEdit.text()
        staff_name = self.ui.staff_id_lineEdit.text()
        if property_id == '' or staff_name == '':
            print('property_id or staff_name are empty')
            return
        values = [property_id, staff_name]
        conn = db_connect()
        cursor = conn.cursor()
        try:
            sql = '''DELETE FROM property_staff WHERE property_id = %s or staff_name = %s;'''
            cursor.execute(sql, values)
            conn.commit()

        except Exception as e:
            print(e)

        finally:
            conn.close()
            print('staff_delete_success')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    del_staff = DelStaff()
    del_staff.show()
    sys.exit(app.exec_())