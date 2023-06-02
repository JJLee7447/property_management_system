from src.db_config import db_connect
from PyQt5 import QtWidgets
from UI.procedure_ui.p_count_pro_fee_ui import Ui_p_count_pro_fee


class P_count_pro_fee(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_p_count_pro_fee()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.query_btn_clicked)

    def query_btn_clicked(self):
        try:
            print("query_btn_clicked")
            conn = db_connect()
            cursor = conn.cursor()
            year = self.ui.year_lineEdit.text()
            month = self.ui.month_lineEdit.text()
            print(year, month)
            query = "CALL Get_property_fee_info(%s, %s, @deu_fee, @paid_fee, @unpaid_fee)"
            cursor.execute(query, (year, month))
            cursor.execute("SELECT @deu_fee, @paid_fee, @unpaid_fee")
            result = cursor.fetchone()
            deu_fee = result[0]
            paid_fee = result[1]
            unpaid_fee = result[2]
            self.ui.due_pay_lineEdit.setText(str(deu_fee))
            self.ui.paid_lineEdit.setText(str(paid_fee))
            self.ui.not_paid_lineEdit.setText(str(unpaid_fee))

        except Exception as e:
            print(e)


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    procedure = P_count_pro_fee()
    procedure.show()
    sys.exit(app.exec_())