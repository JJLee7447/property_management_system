from UI.procedure_ui.P_count_fee_ui import Ui_P_count_fee
from PyQt5 import QtWidgets, QtGui
from src.db_config import db_connect


class P_count_fee(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_P_count_fee()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.query_btn_clicked)

    def query_btn_clicked(self):
        try:
            print("query_btn_clicked")
            conn = db_connect()
            cursor = conn.cursor()
            building_id = self.ui.building_id_lineEdit.text()
            house_id = self.ui.house_id_lineEdit.text()
            print(building_id, house_id)
            query = "CALL GetPropertyInfo(%s, %s, @p_due_parking_fee, @p_due_property_fee)"
            cursor.execute(query, (building_id, house_id))
            cursor.execute("SELECT @p_due_parking_fee, @p_due_property_fee")
            result = cursor.fetchone()
            due_parking_fee = result[0]
            due_property_fee = result[1]
            self.ui.parking_fee.setText(str(due_parking_fee))
            self.ui.property_fee.setText(str(due_property_fee))

        except Exception as e:
            print(e)


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    procedure = P_count_fee()
    procedure.show()
    sys.exit(app.exec_())
