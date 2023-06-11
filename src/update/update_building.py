from PyQt5 import QtWidgets
from UI.update_ui.update_building_ui import Ui_update_building
from src.db_config import db_connect
import sys

class UpdateBuilding(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_update_building()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.update_building_clicked)

    def update_building_clicked(self):
        building_id = self.ui.building_id_lineEdit.text()
        staff_id = self.ui.staff_id_lineEdit.text()
        values = [building_id, staff_id]
        conn = db_connect()
        cursor = conn.cursor()
        sql = '''UPDATE buildings SET property_id = %s  WHERE building_id = %s;'''
        cursor.execute(sql, values)
        conn.commit()
        conn.close()

        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    update_building = UpdateBuilding()
    update_building.show()
    sys.exit(app.exec_())