from UI.update_ui.update_property_fee_ui import Ui_update_property_fee
from src.db_config import db_connect
from PyQt5 import QtCore, QtGui, QtWidgets


def NotPaidHouseId_BuildingId(year, month):
    conn = db_connect()
    cursor = conn.cursor()

    sql = '''SELECT house_id, building_id, due_property_fee FROM property_fees WHERE year = %s AND month = %s AND is_paid = '否'; '''
    cursor.execute(sql, (year, month))
    result = cursor.fetchall()
    conn.close()
    print(result)
    return result

def Due_paid_Fee(year, month, building_id, house_id):
    conn = db_connect()
    cursor = conn.cursor()

    sql = '''SELECT due_property_fee FROM property_fees WHERE year = %s AND month = %s AND house_id = %s AND building_id = %s; '''
    cursor.execute(sql, (year, month, house_id, building_id))
    result = cursor.fetchall()
    conn.close()
    print(result)
    return result

class UpdatePropertyFee(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_update_property_fee()
        self.ui.setupUi(self)
        self.ui.paid_dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.ui.year_lineEdit.setText(QtCore.QDateTime.currentDateTime().toString("yyyy"))
        self.ui.month_lineEdit.setText(QtCore.QDateTime.currentDateTime().toString("MM"))
        self.ui.due_payment_lineEdit.setReadOnly(True)
        year, month = self.ui.year_lineEdit.text(), self.ui.month_lineEdit.text()

        self.ui.house_id_comboBox.addItems([str(i[0]) for i in NotPaidHouseId_BuildingId(year, month)])
        self.ui.building_id_comboBox.addItems([str(i[1]) for i in NotPaidHouseId_BuildingId(year, month)])
        building_id, house_id = self.ui.building_id_comboBox.currentText(), self.ui.house_id_comboBox.currentText()
        due_payment = Due_paid_Fee(year, month, building_id, house_id)
        self.ui.due_payment_lineEdit.setText(str(due_payment[0][0]))

        self.ui.pushButton.clicked.connect(self.update_property_fee)
        self.ui.paid_dateEdit.dateTimeChanged.connect(self.update_year_month)
        self.ui.house_id_comboBox.currentIndexChanged.connect(self.update_building_id)
        self.ui.house_id_comboBox.currentIndexChanged.connect(self.update_due_paid_fee)

    def update_year_month(self):
        date = self.ui.paid_dateEdit.dateTime()
        year = date.toString("yyyy")
        month = date.toString("MM")
        self.ui.year_lineEdit.setText(year)
        self.ui.month_lineEdit.setText(month)


    def update_due_paid_fee(self):
        year, month = self.ui.year_lineEdit.text(), self.ui.month_lineEdit.text()
        house_id, building_id = self.ui.house_id_comboBox.currentText(), self.ui.building_id_comboBox.currentText()
        conn = db_connect()
        cursor = conn.cursor()

        sql = '''SELECT due_property_fee FROM property_fees WHERE year = %s AND month = %s AND house_id = %s AND building_id = %s; '''
        cursor.execute(sql, (year, month, house_id, building_id))
        result = cursor.fetchone()
        conn.close()
        self.ui.due_payment_lineEdit.setText(str(result[0]))


    def update_building_id(self):
        house_id = self.ui.house_id_comboBox.currentText()
        conn = db_connect()
        cursor = conn.cursor()
        sql = '''SELECT building_id FROM build_house_resident WHERE house_id = %s;'''
        cursor.execute(sql, (house_id,))
        result = cursor.fetchall()
        conn.close()
        self.ui.building_id_comboBox.clear()
        self.ui.building_id_comboBox.addItems([str(i[0]) for i in result])


    def update_property_fee(self):
        print("update_property_fee")
        year, month = self.ui.year_lineEdit.text() , self.ui.month_lineEdit.text()
        house_id, building_id = self.ui.house_id_comboBox.currentText(), self.ui.building_id_comboBox.currentText()
        paid_date = self.ui.paid_dateEdit.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        paid_property_fee = self.ui.payment_lineEdit.text()
        conn = db_connect()
        cursor = conn.cursor()
        try:

            sql = '''UPDATE property_fees SET is_paid = '是',paid_property_fee = %s WHERE year = %s AND month = %s AND house_id = %s AND building_id = %s;'''
            cursor.execute(sql, (paid_property_fee, year, month, house_id, building_id))
            conn.commit()

        except Exception as e:
            print(e)

        else:
            print("update_property_fee success")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    update_property_fee = UpdatePropertyFee()
    update_property_fee.show()
    sys.exit(app.exec_())
