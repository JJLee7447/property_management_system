from src.db_config import db_connect
from PyQt5 import QtWidgets
from UI.update_ui.update_resident_ui import Ui_update_resident
import sys

def GetresidentId():
    conn = db_connect()
    cursor = conn.cursor()
    sql = '''SELECT resident_id FROM residents;'''
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.close()
    return result

def GetResidentInfo(resident_id):
    conn = db_connect()
    cursor = conn.cursor()
    sql = '''SELECT * FROM residents WHERE resident_id = %s;'''
    cursor.execute(sql, resident_id)
    result = cursor.fetchone()
    conn.close()
    return result

class  UpdateResident(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_update_resident()
        self.ui.setupUi(self)
        self.ui.resident_id_comboBox.addItems([str(i[0]) for i in GetresidentId()])
        self.ui.resident_id_comboBox.currentIndexChanged.connect(self.update_resident_info)
        info = GetResidentInfo(self.ui.resident_id_comboBox.currentText())
        self.ui.email_edit.setPlaceholderText(info[1])
        self.ui.name_edit.setPlaceholderText(info[2])
        self.ui.employer_edit.setPlaceholderText(info[3])
        self.ui.family_size_edit.setPlaceholderText(str(info[4]))

        self.ui.pushButton.clicked.connect(self.update_resident_clicked)


    def update_resident_clicked(self):
        try:
            resident_id = self.ui.resident_id_comboBox.currentText()
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
        except Exception as e:
            print(e)

        else:
            print("update resident success")
            print(resident_id, email, name, employer, family_size)

    def update_resident_info(self):
        resident_id = self.ui.resident_id_comboBox.currentText()
        result = GetResidentInfo(resident_id)
        self.ui.email_edit.setPlaceholderText(result[1])
        self.ui.name_edit.setPlaceholderText(result[2])
        self.ui.employer_edit.setPlaceholderText(result[3])
        self.ui.family_size_edit.setPlaceholderText(str(result[4]))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    update_resident = UpdateResident()
    update_resident.show()
    sys.exit(app.exec_())