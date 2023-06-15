from PyQt5 import QtWidgets
from UI.update_ui.update_building_ui import Ui_update_building
from src.db_config import db_connect
import sys

def GetBuildingId_staffId():
    conn = db_connect()
    cursor = conn.cursor()
    try:
        sql = '''SELECT building_id,property_id FROM buildings;'''
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(e)
    finally:
        conn.close()

class UpdateBuilding(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_update_building()
        self.ui.setupUi(self)

        self.ui.building_id_comboBox.addItems([str(i[0]) for i in GetBuildingId_staffId()])
        self.ui.staff_id_lineEdit.setPlaceholderText(str(GetBuildingId_staffId()[0][1]))
        self.ui.pushButton.clicked.connect(self.update_building_clicked)
        self.ui.building_id_comboBox.currentIndexChanged.connect(self.building_id_changed)

    def update_building_clicked(self):
        building_id = self.ui.building_id_comboBox.currentText()
        staff_id = self.ui.staff_id_lineEdit.text()
        values = [building_id, staff_id]
        conn = db_connect()
        cursor = conn.cursor()
        try:
            sql = '''UPDATE buildings SET property_id = %s  WHERE building_id = %s;'''
            cursor.execute(sql, values)
            conn.commit()
        except Exception as e:
            print(e)
        else:
            print('building_update_success')
        finally:
            conn.close()


    def building_id_changed(self):
        building_id = self.ui.building_id_comboBox.currentText()
        conn = db_connect()
        cursor = conn.cursor()
        try:
            sql = '''SELECT property_id FROM buildings WHERE building_id = %s;'''
            cursor.execute(sql, building_id)
            result = cursor.fetchone()
            self.ui.staff_id_lineEdit.setPlaceholderText(str(result[0]))
        except Exception as e:
            print(e)
        finally:
            conn.close()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    update_building = UpdateBuilding()
    update_building.show()
    sys.exit(app.exec_())