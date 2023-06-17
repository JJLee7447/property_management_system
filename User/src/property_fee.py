from User.ui.property_fee_ui import Ui_property_fee
from PyQt5 import QtWidgets, QtCore
import sys
from PyQt5.QtGui import QFont
from src.db_config import db_connect
from datetime import datetime
from User.src.func import find_building_id_house_id, Get_staff_id, Get_due_paid_fee, check_is_property_fee_paid, setFont, Use_house_id_Get_building_id


class PropertyFee(QtWidgets.QMainWindow, Ui_property_fee):
    def __init__(self):
        super().__init__()
        self.resident_id = None
        self.setupUi(self)
        to_day = datetime.now().strftime('%Y-%m-%d')
        self.paid_dateEdit.setDate(QtCore.QDate.fromString(to_day, 'yyyy-MM-dd'))
        self.year_lineEdit.setText(to_day[:4])
        self.month_lineEdit.setText(to_day[5:7])
        self.pushButton.hide()
        self.exit_pushButton.hide()

        self.new_pushButton.clicked.connect(self.update_info)
        self.pushButton.clicked.connect(self.pay_property_fee)
        self.house_id_comboBox.currentIndexChanged.connect(self.update_building_id)

    def pay_property_fee(self):
        print('pay_property_fee')
        year, month, paid_date = self.year_lineEdit.text(), self.month_lineEdit.text(), self.paid_dateEdit.text()
        building_id, house_id = self.building_id_comboBox.currentText(), self.house_id_comboBox.currentText()
        staff_id = Get_staff_id(building_id)
        due_payment = self.due_payment_lineEdit.text()
        paid_fee = due_payment
        conn = db_connect()
        cursor = conn.cursor()
        try:
            sql = '''INSERT INTO property_fees (building_id, house_id, year, month, payment_date, due_property_fee, paid_property_fee, is_paid, property_id ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            cursor.execute(sql, (building_id, house_id, year, month, paid_date, due_payment, paid_fee, '是', staff_id))
            conn.commit()

        except Exception as e:
            print(e)
            print('缴费失败')
            conn.rollback()
        else:
            print('缴费成功')
            self.update_info()

    def update_info(self):
        print('update_info')
        self.building_id_comboBox.clear()
        self.house_id_comboBox.clear()
        year = self.year_lineEdit.text()
        month = self.month_lineEdit.text()
        resident_id = self.resident_id

        self.building_id_comboBox.addItems([str(i[0]) for i in find_building_id_house_id(resident_id)])
        self.house_id_comboBox.addItems([str(i[1]) for i in find_building_id_house_id(resident_id)])
        self.due_payment_lineEdit.setText(str(Get_due_paid_fee(resident_id)))
        staff_id = Get_staff_id(self.building_id_comboBox.currentText())
        self.staff_id_lineEdit.setText(str(staff_id))

        if check_is_property_fee_paid(self, year, month):
            setFont(self.is_paid_label)
            self.is_paid_label.setText('您已缴费')
            print('已缴费')
        else:
            setFont(self.is_paid_label)
            self.is_paid_label.setText('您未缴费')
            print('未缴费')

        if self.is_paid_label.text() == '您未缴费':
            self.pushButton.show()
        else:
            self.new_pushButton.hide()
            self.pushButton.hide()
            self.exit_pushButton.show()

        if not check_is_property_fee_paid(self, year, month):
            self.pushButton.show()
        else:
            self.new_pushButton.hide()
            self.pushButton.hide()
            self.exit_pushButton.show()

    def Get_resident_id(self, resident_id):
        print(f'住户编号为 demo {resident_id}')

        self.resident_id = resident_id

    def update_building_id(self):
        print('update_building_id')
        self.building_id_comboBox.clear()
        building_id = Use_house_id_Get_building_id(self.house_id_comboBox.currentText())
        self.building_id_comboBox.addItem(str(building_id))
        staff_id = Get_staff_id(building_id)
        self.staff_id_lineEdit.setText(str(staff_id))
        year = self.year_lineEdit.text()
        month = self.month_lineEdit.text()

        if check_is_property_fee_paid(self, year, month):
            setFont(self.is_paid_label)
            self.is_paid_label.setText('您已缴费')
            print('已缴费')
        else:
            setFont(self.is_paid_label)
            self.is_paid_label.setText('您未缴费')
            print('未缴费')

        if self.is_paid_label.text() == '您未缴费':
            self.pushButton.show()
        else:
            self.new_pushButton.hide()
            self.pushButton.hide()
            self.exit_pushButton.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    property_fee = PropertyFee()
    property_fee.show()
    sys.exit(app.exec_())
