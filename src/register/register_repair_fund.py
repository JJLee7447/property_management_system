from PyQt5 import QtWidgets
from UI.register_ui.register_repair_fund_ui import Ui_register_repair_fund
from src.db_config import db_connect
import sys


class RegisterRepairFound(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_register_repair_fund()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.register_repair_found_clicked)

    def register_repair_found_clicked(self):
        print("register_repair_found_clicked")
        account_id = self.ui.id_lineEdit.text()
        balance = self.ui.balance_lineEdit.text()
        values = [account_id, balance]
        conn = db_connect()
        cursor = conn.cursor()
        try:
            sql = '''insert into repair_fund(account_id, balance) values(%s, %s)'''
            cursor.execute(sql, values)
            conn.commit()
        except Exception as e:
            print("An error occurred while inserting into the repair_fund table:")
            print(e)
            conn.rollback()

        cursor.close()
        conn.close()
        print(values)
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    register_repair_found = RegisterRepairFound()
    register_repair_found.show()
    sys.exit(app.exec_())
