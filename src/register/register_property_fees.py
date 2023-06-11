from UI.register_ui.register_property_fees_ui import Ui_register_property_fees
from PyQt5 import QtWidgets
from datetime import datetime
from PyQt5.QtCore import QDateTime
from src.db_config import db_connect
import sys


class RegisterPropertyFees(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_register_property_fees()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.register_btn_clicked)
        current_datetime = QDateTime.currentDateTime()
        self.ui.paid_dateEdit.setDateTime(current_datetime)
        self.ui.year_lineEdit.setText(str(datetime.now().year))
        self.ui.month_lineEdit.setText(str(datetime.now().month))

    def register_btn_clicked(self):
        print("register_btn_clicked")
        building_id = self.ui.building_id_lineEdit.text()
        house_id = self.ui.house_id_lineEdit.text()
        year = self.ui.year_lineEdit.text()
        month = self.ui.month_lineEdit.text()
        due_pay = self.ui.due_payment_lineEdit.text()
        paid = self.ui.payment_lineEdit.text()
        paid_date = self.ui.paid_dateEdit.text()
        paid_date_mysql = paid_date.replace("/", "-")
        staff_id = self.ui.staff_id_lineEdit.text()
        values = [building_id, house_id, year, month, due_pay, paid, paid_date_mysql, staff_id]
        conn = db_connect()
        cursor = conn.cursor()
        try:
            sql = '''INSERT INTO property_fees (building_id, house_id, year, month, due_property_fee, paid_property_fee, 
            payment_date, property_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'''
            cursor.execute(sql, values)
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)
            print("Error: Duplicate entry for key 'PRIMARY'")

        print(building_id, house_id, year, month, due_pay, paid, paid_date_mysql, staff_id)
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    register_property_fees = RegisterPropertyFees()
    register_property_fees.show()
    sys.exit(app.exec_())
