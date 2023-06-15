from UI.register_ui.register_property_fees_ui import Ui_register_property_fees
from PyQt5 import QtWidgets
from datetime import datetime
from PyQt5.QtCore import QDateTime
from src.db_config import db_connect
import sys


def GetBuildingId():
    conn = db_connect()
    cursor = conn.cursor()
    sql = '''select building_id from buildings;'''
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        return result
    except Exception as e:
        print(e)

def GetHouseId(building_id):
    conn = db_connect()
    cursor = conn.cursor()
    sql = '''select house_id from build_house_resident where building_id = %s;'''
    try:
        cursor.execute(sql, (building_id,))
        result = cursor.fetchall()
        print(result)
        return result
    except Exception as e:
        print(e)


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
        self.ui.building_id_comboBox.addItems([str(i[0]) for i in GetBuildingId()])
        building_id = self.ui.building_id_comboBox.currentText()
        self.ui.house_id_comboBox.addItems([str(i[0]) for i in GetHouseId(building_id)])

        self.ui.building_id_comboBox.currentIndexChanged.connect(self.update_house_id)
        self.ui.building_id_comboBox.currentIndexChanged.connect(self.update_staff_id)
        self.ui.house_id_comboBox.currentIndexChanged.connect(self.update_property_fee)
        self.ui.paid_dateEdit.dateChanged.connect(self.update_year_month)

    def register_btn_clicked(self):
        print("register_btn_clicked")
        try:
            building_id = self.ui.building_id_comboBox.currentText()
            house_id = self.ui.house_id_comboBox.currentText()
            year = self.ui.year_lineEdit.text()
            month = self.ui.month_lineEdit.text()
            due_pay = self.ui.due_payment_lineEdit.text()
            paid = self.ui.payment_lineEdit.text()
            paid_date = self.ui.paid_dateEdit.text()
            paid_date_mysql = paid_date.replace("/", "-")
            staff_id = self.ui.staff_id_lineEdit.text()
            if self.ui.is_paid_radioButton.isChecked():
                is_paid = "是"
            else:
                is_paid = "否"
            values = [building_id, house_id, year, month, due_pay, paid, paid_date_mysql, staff_id, is_paid]
            conn = db_connect()
            cursor = conn.cursor()
            sql = '''INSERT INTO property_fees (building_id, house_id, year, month, due_property_fee, paid_property_fee, 
            payment_date, property_id, is_paid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);'''
            cursor.execute(sql, values)
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)

        else:
            print(building_id, house_id, year, month, due_pay, paid, paid_date_mysql, staff_id, is_paid)
            print("register_property_fees success")

    def update_year_month(self, date):
        year = date.year()
        month = date.month()
        self.ui.year_lineEdit.setText(str(year))
        self.ui.month_lineEdit.setText(str(month))

    def update_house_id(self):
        building_id = self.ui.building_id_comboBox.currentText()
        self.ui.house_id_comboBox.clear()
        conn = db_connect()
        cursor = conn.cursor()
        sql = '''select house_id from house where building_id=%s;'''
        try:
            cursor.execute(sql, building_id)
            result = cursor.fetchall()
            print(result)
            self.ui.house_id_comboBox.addItems([str(i[0]) for i in result])
        except Exception as e:
            print(e)

    def update_staff_id(self):
        building_id = self.ui.building_id_comboBox.currentText()
        conn = db_connect()
        cursor = conn.cursor()
        sql = '''select property_id from buildings where building_id=%s;'''
        try:
            cursor.execute(sql, building_id)
            result = cursor.fetchall()
            print(result)
            self.ui.staff_id_lineEdit.setText(str(result[0][0]))
        except Exception as e:
            print(e)


    def update_property_fee(self):
        house_id = self.ui.house_id_comboBox.currentText()
        conn = db_connect()
        cursor = conn.cursor()
        sql = '''select property_fee from house where house_id=%s;'''
        try:
            cursor.execute(sql, house_id)
            result = cursor.fetchall()
            print(result)
            self.ui.due_payment_lineEdit.setText(str(result[0][0]))
        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    register_property_fees = RegisterPropertyFees()
    register_property_fees.show()
    sys.exit(app.exec_())
