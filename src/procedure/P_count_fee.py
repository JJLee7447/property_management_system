from UI.procedure_ui.P_count_fee_ui import Ui_P_count_fee
from PyQt5 import QtWidgets, QtGui
from src.db_config import db_connect

def Getbuilding_id():
    conn = db_connect()
    cursor = conn.cursor()
    query = "SELECT building_id FROM buildings"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def GetHouse_id(building_id):
    conn = db_connect()
    cursor = conn.cursor()
    query = "SELECT house_id FROM build_house_resident WHERE building_id = %s"
    cursor.execute(query, (building_id,))
    result = cursor.fetchall()
    return result


class P_count_fee(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_P_count_fee()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.query_btn_clicked)

        self.ui.building_id_comboBox.addItems([str(i[0]) for i in Getbuilding_id()])
        current_building_id = self.ui.building_id_comboBox.currentText()
        self.ui.house_id_comboBox.addItems([str(i[0]) for i in GetHouse_id(current_building_id)])

        self.ui.building_id_comboBox.currentIndexChanged.connect(self.update_house_id)

    def query_btn_clicked(self):
        try:
            print("query_btn_clicked")
            conn = db_connect()
            cursor = conn.cursor()
            building_id = self.ui.building_id_comboBox.currentText()
            house_id = self.ui.house_id_comboBox.currentText()
            print(building_id, house_id)
            query = "CALL Get_Property_fee_Parking_fee_Info(%s, %s, @p_due_parking_fee, @p_due_property_fee)"
            cursor.execute(query, (building_id, house_id))
            cursor.execute("SELECT @p_due_parking_fee, @p_due_property_fee")
            result = cursor.fetchone()
            due_parking_fee = result[0]
            due_property_fee = result[1]
            self.ui.parking_fee.setText(str(due_parking_fee))
            self.ui.property_fee.setText(str(due_property_fee))

        except Exception as e:
            print(e)

    def update_house_id(self):
        self.ui.house_id_comboBox.clear()
        self.ui.house_id_comboBox.addItems([str(i[0]) for i in GetHouse_id(self.ui.building_id_comboBox.currentText())])

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    procedure = P_count_fee()
    procedure.show()
    sys.exit(app.exec_())
