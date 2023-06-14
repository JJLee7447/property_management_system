from UI.delete_ui.del_staff_ui import Ui_del_staff
from PyQt5 import QtWidgets
from src.db_config import db_connect
import sys

def GetStaffId():
    conn = db_connect()
    cursor = conn.cursor()
    try:
        sql = '''SELECT property_id FROM property_staff;'''
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(e)
    finally:
        conn.close()

class DelStaff(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_del_staff()
        self.ui.setupUi(self)
        self.ui.staff_id_comboBox.addItems([str(i[0]) for i in GetStaffId()])

        self.ui.staff_id_comboBox.currentIndexChanged.connect(self.staff_id_changed)
        self.ui.pushButton.clicked.connect(self.delete_staff_clicked)
        self.ui.pushButton.clicked.connect(self.update_staff_id)

    def delete_staff_clicked(self):
        property_id = self.ui.staff_id_comboBox.currentText()
        staff_name = self.ui.staff_name_lineEdit.text()
        if property_id == '' or staff_name == '':
            print('property_id or staff_name are empty')
            return
        values = [property_id, staff_name]
        conn = db_connect()
        cursor = conn.cursor()
        try:
            sql = '''DELETE FROM property_staff WHERE property_id = %s and staff_name = %s;'''
            cursor.execute(sql, values)
            conn.commit()

        except Exception as e:
            print(e)

        else:
            conn.close()
            print('staff_delete_success')

    def staff_id_changed(self):
        property_id = self.ui.staff_id_comboBox.currentText()
        conn = db_connect()
        cursor = conn.cursor()
        try:
            sql = '''SELECT staff_name FROM property_staff WHERE property_id = %s;'''
            cursor.execute(sql, property_id)
            result = cursor.fetchone()
            self.ui.staff_name_lineEdit.setText(result[0])
        except Exception as e:
            print(e)
        finally:
            conn.close()

    def update_staff_id(self):
        self.ui.staff_id_comboBox.clear()
        self.ui.staff_id_comboBox.addItems([str(i[0]) for i in GetStaffId()])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    del_staff = DelStaff()
    del_staff.show()
    sys.exit(app.exec_())