from PyQt5 import QtWidgets
from UI.register_ui.register_maintenance_ui import Ui_register_maintenance
import sys
from PyQt5.QtCore import QDateTime
from src.db_config import db_connect
from datetime import datetime

class RegisterMaintenance(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_register_maintenance()
        self.ui.setupUi(self)
        current_date = QDateTime.currentDateTime()
        self.ui.report_dateEdit.setDateTime(current_date)
        self.ui.repair_dateEdit.setDateTime(current_date)

        self.ui.pushButton.clicked.connect(self.register_maintenance_clicked)

    def register_maintenance_clicked(self):
        print("register_maintenance_clicked")
        resident_id = self.ui.resident_id_lineEdit.text()
        description = self.ui.description_textEdit.toPlainText()
        # 获取报告日期
        report_date_str = self.ui.report_dateEdit.text()
        report_date = datetime.strptime(report_date_str, "%Y/%m/%d").date()
        report_date_mysql = report_date.strftime("%Y-%m-%d")

        # 获取修复日期
        repair_date_str = self.ui.repair_dateEdit.text()
        repair_date = datetime.strptime(repair_date_str, "%Y/%m/%d").date()
        repair_date_mysql = repair_date.strftime("%Y-%m-%d")
        print(report_date, repair_date)
        amount = self.ui.payment_lineEdit.text()
        repair_person = self.ui.repair_id.text()
        account_id = self.ui.account_lineEdit.text()
        y_n = ['是', '否']
        yes = self.ui.yes.isChecked()
        if yes:
            values = [resident_id, description, report_date_mysql, repair_date_mysql, amount, repair_person, y_n[0], account_id]
        else:
            values = [resident_id, description, report_date_mysql, repair_date_mysql, amount, repair_person, y_n[1], account_id]

        conn = db_connect()
        cursor = conn.cursor()
        try:
            sql = '''insert into maintenance(resident_id, description, report_date, repair_date, amount, repair_person, is_from_repair_fund, account_id)
             values(%s, %s, %s, %s, %s, %s, %s, %s)'''
            cursor.execute(sql, values)
            conn.commit()
        except Exception as e:
            print("An error occurred while inserting into the maintenance table:")
            print(e)
            conn.rollback()
        else:
            print("register_maintenance_success")
            cursor.close()
            conn.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    register_maintenance = RegisterMaintenance()
    register_maintenance.show()
    sys.exit(app.exec_())
