from UI.update_ui.update_repair_fund_ui import Ui_update_repair_fund
from src.db_config import db_connect
from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QApplication


class UpdateRepairFund(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_update_repair_fund()
        self.ui.setupUi(self)
        self.ui.yes_btn.clicked.connect(self.update_btn_clicked)
        self.ui.yes_btn.clicked.connect(self.new_btn_clicked)
        self.ui.new_btn.clicked.connect(self.new_btn_clicked)

    def update_btn_clicked(self):
        try:
            print("update_btn_clicked")
            conn = db_connect()
            cursor = conn.cursor()
            add_money = self.ui.add_money_lineEdit.text()
            sql = '''UPDATE repair_fund SET balance= repair_fund.balance + %s where account_id = 1;'''
            cursor.execute(sql, add_money)
            conn.commit()
            conn.close()

            print("update repair fund success")
        except Exception as e:
            print(e)


    def new_btn_clicked(self):
        try:
            print("new_btn_clicked")
            conn = db_connect()
            cursor = conn.cursor()
            sql = '''select balance from repair_fund where account_id = 1;'''
            cursor.execute(sql)
            result = cursor.fetchone()
            balance = result[0]
            self.ui.balance_lineEdit.setText(str(balance))
            self.ui.add_money_lineEdit.setText("")
            conn.commit()
            conn.close()

            print("new repair fund success")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    update_repair_fund = UpdateRepairFund()
    update_repair_fund.show()
    sys.exit(app.exec_())