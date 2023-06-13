from UI.register_ui.register_parking_fees_ui import Ui_register_parking_fees
from PyQt5 import QtWidgets
from datetime import datetime
from PyQt5.QtCore import QDateTime
from src.db_config import db_connect
import sys


def get_parking_space_id():
    conn = db_connect()
    cursor = conn.cursor()
    sql = '''SELECT parking_space_id FROM parking_spaces;'''
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.close()
    return result


class RegisterParkingFees(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_register_parking_fees()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.register_btn_clicked)
        current_datetime = QDateTime.currentDateTime()
        self.ui.paid_dateEdit.setDateTime(current_datetime)
        self.ui.year_lineEdit.setText(str(datetime.now().year))
        self.ui.month_lineEdit.setText(str(datetime.now().month))

        self.ui.parking_id_comboBox.addItems([str(i[0]) for i in get_parking_space_id()])
        self.ui.paid_dateEdit.dateChanged.connect(self.update_year_month)
        self.ui.parking_id_comboBox.currentIndexChanged.connect(self.update_staff_id)
        self.ui.parking_id_comboBox.currentIndexChanged.connect(self.update_parking_fee)

    def register_btn_clicked(self):
        print("register_btn_clicked")
        parking_id = self.ui.parking_id_comboBox.currentText()
        year = self.ui.year_lineEdit.text()
        month = self.ui.month_lineEdit.text()
        due_pay = self.ui.due_pay_lineEdit.text()
        paid = self.ui.paid_lineEdit.text()
        paid_date = self.ui.paid_dateEdit.text()
        paid_date_mysql = paid_date.replace("/", "-")
        staff_id = self.ui.staff_id_lineEdit.text()
        if self.ui.is_paid_radioButton.isChecked():
            is_paid = '是'
        else:
            is_paid = '否'
        values = [parking_id, year, month, due_pay, paid, paid_date_mysql, staff_id, is_paid]
        conn = db_connect()
        cursor = conn.cursor()
        sql = '''INSERT INTO parking_fees (parking_space_id, year, month, due_parking_fee, paid_parking_fee, payment_date, property_id, is_paid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'''
        try:
            cursor.execute(sql, values)
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)

        print(parking_id, year, month, due_pay, paid, paid_date_mysql, staff_id, is_paid)

    def update_year_month(self, date):
        year = date.year()
        month = date.month()
        self.ui.year_lineEdit.setText(str(year))
        self.ui.month_lineEdit.setText(str(month))

    def update_staff_id(self):
        print("update_staff_id")
        parking_id = self.ui.parking_id_comboBox.currentText()
        conn = db_connect()
        cursor = conn.cursor()
        sql1 = '''SELECT building_id FROM parking_spaces WHERE parking_space_id=%s;'''
        cursor.execute(sql1, parking_id)
        result1 = cursor.fetchone()

        sql2 = '''SELECT property_id FROM buildings where building_id = %s;'''
        cursor.execute(sql2, result1[0])
        result2 = cursor.fetchone()

        self.ui.staff_id_lineEdit.setText(str(result2[0]))


    def update_parking_fee(self):
        print("update_parking_fee")
        parking_id = self.ui.parking_id_comboBox.currentText()
        conn = db_connect()
        cursor = conn.cursor()
        sql = '''SELECT parking_fee FROM parking_spaces WHERE parking_space_id=%s;'''
        cursor.execute(sql, parking_id)
        result = cursor.fetchone()
        self.ui.due_pay_lineEdit.setText(str(result[0]))
        conn.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    register_parking_fees = RegisterParkingFees()
    register_parking_fees.show()
    sys.exit(app.exec_())