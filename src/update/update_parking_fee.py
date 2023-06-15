from UI.update_ui.update_parking_fee_ui import Ui_update_parking_fee
from src.db_config import db_connect
from PyQt5 import QtWidgets
import sys
from datetime import datetime


def GetparkingSpaceId(year, month):
    conn = db_connect()
    cursor = conn.cursor()
    sql = '''SELECT parking_space_id FROM parking_fees where is_paid = '否' and year = %s and month = %s;'''
    cursor.execute(sql, (year, month))
    result = cursor.fetchall()
    return result

def GetParkingFee(parking_space_id):
    conn = db_connect()
    cursor = conn.cursor()
    sql = '''SELECT parking_fee FROM parking_spaces WHERE parking_space_id = %s;'''
    cursor.execute(sql, (parking_space_id,))
    result = cursor.fetchone()
    return result[0]

def GetStaffId(parking_space_id):
    conn = db_connect()
    cursor = conn.cursor()
    sql = '''SELECT property_id FROM buildings where building_id =(select building_id from parking_spaces where parking_space_id = %s);'''
    cursor.execute(sql, (parking_space_id,))
    result = cursor.fetchall()
    return result

class UpdateParkingFee(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_update_parking_fee()
        self.ui.setupUi(self)
        self.ui.paid_dateEdit.setDateTime(datetime.now())
        self.ui.year_lineEdit.setText(str(datetime.now().year))
        self.ui.month_lineEdit.setText(str(datetime.now().month))
        year, month = self.ui.year_lineEdit.text(), self.ui.month_lineEdit.text()
        self.ui.parking_id_comboBox.addItems([str(i[0]) for i in GetparkingSpaceId(year, month)])
        parking_space_id = self.ui.parking_id_comboBox.currentText()
        self.ui.due_pay_lineEdit.setText(str(GetParkingFee(parking_space_id)))
        self.ui.staff_id_lineEdit.setText(str(GetStaffId(parking_space_id)[0][0]))

        self.ui.parking_id_comboBox.currentIndexChanged.connect(self.update_parking_fee_staff_id)
        self.ui.pushButton.clicked.connect(self.pushButton_clicked)


    def pushButton_clicked(self):
        print("update_btn_clicked")
        try:
            conn = db_connect()
            cursor = conn.cursor()
            year, month = self.ui.year_lineEdit.text(), self.ui.month_lineEdit.text()
            parking_space_id = self.ui.parking_id_comboBox.currentText()
            paid_fee = self.ui.paid_lineEdit.text()
            values = (paid_fee, parking_space_id, year, month)
            sql = '''UPDATE parking_fees SET is_paid = '是',paid_parking_fee = %s WHERE parking_space_id = %s and year = %s and month = %s;'''
            cursor.execute(sql, values)
            conn.commit()
        except Exception as e:
            print(e)

        else:
            print("update parking fee success")

        finally:
            conn.close()

    def update_parking_fee_staff_id(self):
        parking_space_id = self.ui.parking_id_comboBox.currentText()
        self.ui.due_pay_lineEdit.setText(str(GetParkingFee(parking_space_id)))
        self.ui.staff_id_lineEdit.setText(str(GetStaffId(parking_space_id)[0][0]))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = UpdateParkingFee()
    window.show()
    sys.exit(app.exec_())
