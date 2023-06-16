from UI.update_ui.update_staff_info_ui import Ui_update_staff_info
from PyQt5 import QtWidgets
from src.db_config import db_connect
import sys

def GetstaffId():
    conn = db_connect()
    cursor = conn.cursor()
    sql = '''SELECT property_id FROM property_staff'''
    cursor.execute(sql)
    res = cursor.fetchall()
    conn.close()
    return res

def Getstaffname(staff_id):
    conn = db_connect()
    cursor = conn.cursor()
    sql = '''SELECT staff_name FROM property_staff WHERE property_id = %s'''
    cursor.execute(sql, (staff_id,))
    res = cursor.fetchall()
    conn.close()
    return res

class UpdateStaff(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_update_staff_info()
        self.ui.setupUi(self)
        self.ui.staff_id_cbox.addItems([str(i[0]) for i in GetstaffId()])
        staff_id = self.ui.staff_id_cbox.currentText()
        self.ui.name_editor.setText(str(Getstaffname(staff_id)[0][0]))

        self.ui.pushButton.clicked.connect(self.update_staff_info_clicked)
        self.ui.staff_id_cbox.currentTextChanged.connect(self.staff_id_cbox_currentTextChanged)

    def update_staff_info_clicked(self):
        staff_id = self.ui.staff_id_cbox.currentText()
        name = self.ui.name_editor.text()
        position = self.ui.position_combox.currentText()
        password1 = self.ui.password_lineEdit.text()
        password2 = self.ui.password_lineEdit_2.text()
        if password1 != password2:
            print('两次密码不一致')
            return
        password = password1
        values = [name, position, password, staff_id]
        if password == '':
            print('密码不能为空')
            return
        conn = db_connect()
        cursor = conn.cursor()
        try:
            sql = '''UPDATE property_staff SET staff_name = %s, position = %s ,pass_word = %s where property_id = %s;'''
            cursor.execute(sql, values)
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)
        else:
            print('update_staff_info_success')

    def staff_id_cbox_currentTextChanged(self):
        staff_id = self.ui.staff_id_cbox.currentText()
        self.ui.name_editor.setText(str(Getstaffname(staff_id)[0][0]))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    update_staff = UpdateStaff()
    update_staff.show()
    sys.exit(app.exec_())
