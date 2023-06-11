import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView
from UI.mainwindow_ui import Ui_MainWindow
from src.db_config import db_connect
from src.register.register_resident import RegisterResident
from src.register.register_building import RegisterBuilding
from src.register.register_house import RegisterHouse
from src.register.register_parking_space import RegisterParkingSpace
from src.register.register_staff import RegisterStaff
from src.register.register_maintenance import RegisterMaintenance
from src.register.register_parking_fees import RegisterParkingFees
from src.register.register_property_fees import RegisterPropertyFees
from src.delete.del_resident import DelResident
from src.update.update_resident import UpdateResident
from src.update.update_staff import UpdateStaff
from src.update.update_building import UpdateBuilding
from src.update.update_parking_space import UpdateParkingSpace
import src.query_all as query_all
from src.procedure.P_count_fee import P_count_fee
from src.procedure.p_count_pro_fee import P_count_pro_fee


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.register_parking_space = None
        self.register_staff = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.register_resident = None
        self.del_resident = None
        self.register_building = None
        self.update_resident = None
        self.register_house = None
        self.register_parking_fees = None
        self.register_property_fees = None
        self.register_maintenance = None
        self.P_count_fee = None
        self.P_count_pro_fee = None
        self.update_staff = None
        self.update_building = None
        self.update_parking_space = None

        self.ui.register_btn.clicked.connect(self.register_resident_clicked)
        self.ui.query_btn.clicked.connect(self.query_resident_clicked)
        self.ui.clear_btn.clicked.connect(self.clear_btn_clicked)
        self.ui.del_btn.clicked.connect(self.del_btn_clicked)
        self.ui.update_btn.clicked.connect(self.update_btn_clicked)
        self.ui.count_fee_btn.clicked.connect(self.P_count_fee_btn_clicked)
        self.ui.sta_pro_fee_btn.clicked.connect(self.P_count_pro_fee_btn_clicked)
        self.ui.sum_parking_space_btn.clicked.connect(self.sum_parking_space_btn_clicked)
        self.ui.sum_resident_btn.clicked.connect(self.sum_resident_btn_clicked)

    def clear_btn_clicked(self):
        try:
            model = self.ui.tableView.model()
            model.clear()
            model.setHorizontalHeaderLabels([''])
            self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.ui.tableView.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        except Exception as e:
            print(e)

    def register_resident_clicked(self):
        print("register_resident_clicked")
        content = self.ui.register_com_box.currentText()
        if content == '住户信息':
            print("住户信息")
            self.register_resident = RegisterResident()
            self.register_resident.show()

        elif content == '楼栋信息':
            print("楼栋信息")
            self.register_building = RegisterBuilding()
            self.register_building.show()

        elif content == '住房信息':
            print("住房信息")
            self.register_house = RegisterHouse()
            self.register_house.show()

        elif content == '车位信息':
            print("车位信息")
            self.register_parking_space = RegisterParkingSpace()
            self.register_parking_space.show()

        elif content == '员工信息':
            print("员工信息")
            self.register_staff = RegisterStaff()
            self.register_staff.show()

        elif content == '停车费信息':
            print("停车费信息")
            self.register_parking_fees = RegisterParkingFees()
            self.register_parking_fees.show()

        elif content == '物业费信息':
            print("物业费信息")
            self.register_property_fees = RegisterPropertyFees()
            self.register_property_fees.show()

        elif content == '维修信息':
            print("维修信息")
            self.register_maintenance = RegisterMaintenance()
            self.register_maintenance.show()

    def query_resident_clicked(self):
        print("query_resident_clicked")
        content = self.ui.query_com_box.currentText(), self.ui.query_editor.text()
        print(content)
        conn = db_connect()
        cursor = conn.cursor()
        if content[0] == '住户信息':
            query_all.query_resident(self, content, cursor)

        elif content[0] == '楼栋信息':
            query_all.query_building(self, content, cursor)

        elif content[0] == '住房信息':
            query_all.query_house(self, content, cursor)

        elif content[0] == '维修信息':
            query_all.query_maintenance(self, content, cursor)

        elif content[0] == '停车费信息':
            query_all.query_parking_fees(self, content, cursor)

        elif content[0] == '物业费信息':
            query_all.query_property_fees(self, content, cursor)

        elif content[0] == '车位信息':
            query_all.query_parking_spaces(self, content, cursor)

        elif content[0] == '员工信息':
            query_all.query_property_staff(self, content, cursor)

        elif content[0] == '维修基金':
            query_all.query_repair_fund(self, content, cursor)

    def del_btn_clicked(self):
        print("del_btn_clicked")
        if self.ui.del_com_box.currentText() == '住户信息':
            print("住户信息")
            self.del_resident = DelResident()
            self.del_resident.show()

        elif self.ui.del_com_box.currentText() == '车位信息':
            print("车位信息")

        elif self.ui.del_com_box.currentText() == '员工信息':
            print("员工信息")


    def update_btn_clicked(self):
        print("update_btn_clicked")
        if self.ui.update_com_box.currentText() == '住户信息':
            print("住户信息")
            self.update_resident = UpdateResident()
            self.update_resident.show()

        elif self.ui.update_com_box.currentText() == '楼栋信息':
            print("楼栋信息")
            self.update_building = UpdateBuilding()
            self.update_building.show()

        elif self.ui.update_com_box.currentText() == '员工信息':
            print("员工信息")
            self.update_staff = UpdateStaff()
            self.update_staff.show()

        elif self.ui.update_com_box.currentText() == '车位信息':
            print("车位信息")
            self.update_parking_space = UpdateParkingSpace()
            self.update_parking_space.show()

    def P_count_fee_btn_clicked(self):
        print("P_count_fee_btn_clicked")
        self.P_count_fee = P_count_fee()
        self.P_count_fee.show()

    def P_count_pro_fee_btn_clicked(self):
        print("P_count_pro_fee_btn_clicked")
        self.P_count_pro_fee = P_count_pro_fee()
        self.P_count_pro_fee.show()

    def sum_parking_space_btn_clicked(self):
        print("sum_parking_space_btn_clicked")
        conn = db_connect()
        cursor = conn.cursor()
        try:
            query = 'call sum_parking_space(@sum_parking_space);'
            cursor.execute(query)
            cursor.execute('select @sum_parking_space;')
            result = cursor.fetchall()
            sum_parking_space = result[0][0]
            model = QtGui.QStandardItemModel()
            model.setHorizontalHeaderLabels(['车位总数'])
            item = QtGui.QStandardItem(str(sum_parking_space))
            model.appendRow(item)
            self.ui.tableView.setModel(model)

        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.warning(self, "错误", "查询失败", QtWidgets.QMessageBox.Yes)

    def sum_resident_btn_clicked(self):
        print("sum_resident_btn_clicked")
        conn = db_connect()
        cursor = conn.cursor()
        try:
            query = 'call sum_resident(@sum_resident);'
            cursor.execute(query)
            cursor.execute('select @sum_resident;')
            result = cursor.fetchall()
            sum_resident = result[0][0]
            model = QtGui.QStandardItemModel()
            model.setHorizontalHeaderLabels(['住户总数'])
            item = QtGui.QStandardItem(str(sum_resident))
            model.appendRow(item)
            self.ui.tableView.setModel(model)

        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.warning(self, "错误", "查询失败", QtWidgets.QMessageBox.Yes)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
