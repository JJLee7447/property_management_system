from UI.register_ui.register_parking_fees_ui import Ui_register_parking_fees
from PyQt5 import QtWidgets
from datetime import datetime
from PyQt5.QtCore import QDateTime
from src.db_config import db_connect
import sys

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

        self.ui.paid_dateEdit.dateChanged.connect(self.update_year_month)

    def register_btn_clicked(self):
        print("register_btn_clicked")
        parking_id = self.ui.parking_id_lineEdit.text()
        year = self.ui.year_lineEdit.text()
        month = self.ui.month_lineEdit.text()
        due_pay = self.ui.due_pay_lineEdit.text()
        paid = self.ui.paid_lineEdit.text()
        paid_date = self.ui.paid_dateEdit.text()
        paid_date_mysql = paid_date.replace("/", "-")
        staff_id = self.ui.staff_id_lineEdit.text()
        values = [parking_id, year, month, due_pay, paid, paid_date_mysql, staff_id]
        conn = db_connect()
        cursor = conn.cursor()
        sql = '''INSERT INTO parking_fees (parking_space_id, year, month, due_parking_fee, paid_parking_fee, payment_date, property_id) VALUES (%s, %s, %s, %s, %s, %s, %s);'''
        cursor.execute(sql, values)
        conn.commit()
        conn.close()

        print(parking_id, year, month, due_pay, paid, paid_date_mysql, staff_id)
        self.close()

    def update_year_month(self, date):
        year = date.year()
        month = date.month()
        self.ui.year_lineEdit.setText(str(year))
        self.ui.month_lineEdit.setText(str(month))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    register_parking_fees = RegisterParkingFees()
    register_parking_fees.show()
    sys.exit(app.exec_())