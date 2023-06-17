from User.ui.parking_fee_ui import Ui_parking_fee
from PyQt5 import QtWidgets, QtCore
import sys
from src.db_config import db_connect
from datetime import datetime
from User.src.func import Get_staff_id, check_is_parking_fee_paid, setFont, Get_parking_space_id, Get_due_pay_parking_fee


class ParkingFee(QtWidgets.QWidget, Ui_parking_fee):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resident_id = None
        self.staff_id = None
        to_day = datetime.now().strftime('%Y-%m-%d')
        self.paid_dateEdit.setDate(QtCore.QDate.fromString(to_day, 'yyyy-MM-dd'))
        self.year_lineEdit.setText(to_day[:4])
        self.month_lineEdit.setText(to_day[5:7])

        self.pushButton.hide()
        self.exit_pushButton.hide()

        self.new_pushButton.clicked.connect(self.update_info)
        self.pushButton.clicked.connect(self.parking_fee)
        self.parking_id_comboBox.currentIndexChanged.connect(self.update_info_2)

    def update_info(self):
        print('update_info')
        self.parking_id_comboBox.clear()
        year = self.year_lineEdit.text()
        month = self.month_lineEdit.text()
        res = Get_parking_space_id(self.resident_id)
        self.parking_id_comboBox.addItems([str(i[0]) for i in res])

        building_id = Get_due_pay_parking_fee(self.parking_id_comboBox.currentText())[0][1]
        self.staff_id = Get_staff_id(building_id)
        self.staff_id_lineEdit.setText(str(self.staff_id))
        resident_id = self.resident_id
        self.due_payment_lineEdit.setText(str(Get_due_pay_parking_fee(self.parking_id_comboBox.currentText())[0][0]))
        try:

            if check_is_parking_fee_paid(year=year, month=month, parking_space_id=self.parking_id_comboBox.currentText()):
                setFont(self.is_paid_label)
                self.is_paid_label.setText('您已缴费')
                print('已缴费')
            else:
                setFont(self.is_paid_label)
                self.is_paid_label.setText('您未缴费')
                print('未缴费')
        except Exception as e:
            print(e)
        else:
            if self.is_paid_label.text() == '您已缴费':
                self.new_pushButton.hide()
                self.pushButton.hide()
                self.exit_pushButton.show()
            print('update_info_success')

    def Get_resident_id(self, resident_id):
        print(f'function Get_resident_id: {resident_id}')
        self.resident_id = resident_id

    def parking_fee(self):
        print("parking fee")
        year, month, paid_date = self.year_lineEdit.text(), self.month_lineEdit.text(), self.paid_dateEdit.text()
        parking_id = self.parking_id_comboBox.currentText()
        staff_id = self.staff_id_lineEdit.text()
        is_paid = '是'
        parking_fee_ = self.due_payment_lineEdit.text()
        conn = db_connect()
        cursor = conn.cursor()
        sql = '''INSERT INTO parking_fees (parking_space_id, year, month, due_parking_fee, paid_parking_fee, payment_date, property_id, is_paid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'''
        try:
            cursor.execute(sql, (parking_id, year, month, parking_fee_, parking_fee_, paid_date, staff_id, is_paid))
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
        else:
            print('parking_fee_success')
            self.is_paid_label.setText('您已缴费')
            self.exit_pushButton.show()
            self.pushButton.hide()
            self.new_pushButton.hide()

    def update_info_2(self):
        print('update_info_2')
        year = self.year_lineEdit.text()
        month = self.month_lineEdit.text()
        property_fee = Get_due_pay_parking_fee(self.parking_id_comboBox.currentText())
        self.due_payment_lineEdit.setText(str(property_fee[0][0]))
        try:
            if check_is_parking_fee_paid(year=year, month=month, parking_space_id=self.parking_id_comboBox.currentText()):
                setFont(self.is_paid_label)
                self.is_paid_label.setText('您已缴费')
                print('已缴费')
            else:
                setFont(self.is_paid_label)
                self.is_paid_label.setText('您未缴费')
                print('未缴费')
        except Exception as e:
            print(e)
        else:
            print('update_info_2_success')
        if self.is_paid_label.text() == '您已缴费':
            self.new_pushButton.hide()
            self.pushButton.hide()
            self.exit_pushButton.show()
        elif self.is_paid_label.text() == '您未缴费':
            self.new_pushButton.show()
            self.pushButton.show()
            self.exit_pushButton.hide()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    parking_fee = ParkingFee()
    parking_fee.show()
    sys.exit(app.exec_())