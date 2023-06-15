from src.db_config import db_connect
from PyQt5 import QtWidgets
from UI.delete_ui.del_resident_ui import Ui_del_resident
import sys


def GetResidentId():
    conn = db_connect()
    cursor = conn.cursor()
    try:
        sql = '''SELECT resident_id FROM residents;'''
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(e)
    finally:
        conn.close()

class DelResident(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_del_resident()
        self.ui.setupUi(self)
        self.ui.resident_id_comboBox.addItems([str(i[0]) for i in GetResidentId()])
        self.ui.resident_id_comboBox.currentIndexChanged.connect(self.update_resident_name)

        self.ui.pushButton.clicked.connect(self.del_resident_clicked)

    def del_resident_clicked(self):
        print("del_resident_clicked")
        resident_id = self.ui.resident_id_comboBox.currentText()
        name = self.ui.lineEdit_2.text()
        if resident_id == '' or name == '':
            print('resident_id or name are empty')
            return
        values = [resident_id, name]
        conn = db_connect()
        cursor = conn.cursor()
        sql = '''DELETE FROM residents WHERE resident_id = %s and owner_name = %s;'''
        try:
            cursor.execute(sql, values)
            conn.commit()
            conn.close()

        except Exception as e:
            print(e)
        else:
            print('del_resident_success')


    def update_resident_name(self):
        resident_id = self.ui.resident_id_comboBox.currentText()
        conn = db_connect()
        cursor = conn.cursor()
        try:
            sql = '''SELECT owner_name FROM residents WHERE resident_id = %s;'''
            cursor.execute(sql, resident_id)
            result = cursor.fetchone()
            self.ui.lineEdit_2.setText(result[0])
        except Exception as e:
            print(e)
        finally:
            conn.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    del_resident = DelResident()
    del_resident.show()
    sys.exit(app.exec_())
