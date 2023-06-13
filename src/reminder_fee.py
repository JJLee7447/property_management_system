from UI.reminder_fee_ui import Ui_reminder_fee
from PyQt5 import QtWidgets, QtGui
from src.db_config import db_connect
import sys
from datetime import datetime


def email_send(email, unpaid_fee, name,content):
    print(f"{name} 你好，你的{content}用为{unpaid_fee}元，请及时缴纳。")


def property_fee_reminder(self):
    conn = db_connect()
    cursor = conn.cursor()
    year = self.ui.today_dateEdit.date().year()
    month = self.ui.today_dateEdit.date().month()
    values = [year, month]
    try:
        # 查询未缴费的业主信息
        # 在property_fees表中查询，条件是year, month ,查询出已缴费 条件为（due_property_fee == paid_property_fee）的业主信息，然后在build_house_resident表中查询出未缴费所有业主信息
        sql = '''
                SELECT R.resident_id, R.owner_name, R.email, H.property_fee
                FROM residents R
                JOIN house H ON R.resident_id = H.resident_id
                WHERE R.resident_id NOT IN (
                SELECT BHR.resident_id
                FROM property_fees P
                JOIN build_house_resident BHR ON P.building_id = BHR.building_id AND P.house_id = BHR.house_id
                WHERE P.year = %s AND P.month = %s AND P.is_paid = '否'
                );
                '''

        cursor.execute(sql, values)
        result = cursor.fetchall()
        print(result)
        # 将结果显示在tableView中
        # 创建一个model
        model = QtGui.QStandardItemModel()
        # 设置表头
        model.setHorizontalHeaderLabels(['业主ID', '业主姓名', '电子邮箱', '未缴物业费'])
        # 增加数据
        for row in result:
            row_items = [QtGui.QStandardItem(str(field)) for field in row]
            model.appendRow(row_items)

        self.ui.tableView.setModel(model)

        cursor.execute(sql, values)
        result = cursor.fetchall()
        print(result)
        # 将结果显示在tableView中
        # 创建一个model
        model = QtGui.QStandardItemModel()
        # 设置表头
        model.setHorizontalHeaderLabels(['业主ID', '业主姓名', '电子邮箱', '未缴物业费'])
        # 增加数据
        for row in result:
            row_items = [QtGui.QStandardItem(str(field)) for field in row]
            model.appendRow(row_items)

        self.ui.tableView.setModel(model)

    except Exception as e:
        print(e)

def parking_fee_reminder(self):
    conn = db_connect()
    cursor = conn.cursor()
    year = self.ui.today_dateEdit.date().year()
    month = self.ui.today_dateEdit.date().month()
    values = [year, month]
    try:
        # 查询未缴费的业主信息
        # 在parking_fees表中查询，条件是year, month ,查询出已缴费 条件为（due_property_fee == paid_property_fee）的parking_space_id
        # 根据parking_space_id 在 parking_spaces 表中查询出已缴费的 resident_id
        # 在parking_parking_space表中查询出 未缴费的resident_id 和 未缴的停车费 parking_fee
        # 根据 resident_id 在 residents 表中查询出 业主姓名 和 电子邮箱
        sql = '''
                SELECT R.resident_id,R.owner_name,R.email, PS.parking_fee
                FROM parking_spaces PS
                JOIN house H ON PS.house_id = H.house_id
                JOIN residents R ON H.resident_id = R.resident_id
                WHERE PS.parking_space_id NOT IN (
                    SELECT parking_space_id
                    FROM parking_fees
                    where year = %s AND month = %s AND is_paid = '否'
);
                '''

        cursor.execute(sql, values)
        result = cursor.fetchall()
        print(result)
        # 将结果显示在tableView中
        # 创建一个model
        model = QtGui.QStandardItemModel()
        # 设置表头
        model.setHorizontalHeaderLabels(['业主ID', '业主姓名', '电子邮箱', '未缴停车费'])
        # 增加数据
        for row in result:
            row_items = [QtGui.QStandardItem(str(field)) for field in row]
            model.appendRow(row_items)

        self.ui.tableView.setModel(model)

        cursor.execute(sql, values)
        result = cursor.fetchall()
        print(result)
        # 将结果显示在tableView中
        # 创建一个model
        model = QtGui.QStandardItemModel()
        # 设置表头
        model.setHorizontalHeaderLabels(['业主ID', '业主姓名', '电子邮箱', '未缴停车费'])
        # 增加数据
        for row in result:
            row_items = [QtGui.QStandardItem(str(field)) for field in row]
            model.appendRow(row_items)

        self.ui.tableView.setModel(model)
    except Exception as e:
        print(e)


class ReminderFee(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_reminder_fee()
        self.ui.setupUi(self)
        current_date = datetime.now().strftime("%Y-%m-%d")
        self.ui.today_dateEdit.setDate(datetime.strptime(current_date, "%Y-%m-%d"))

        self.ui.query_not_paid_btn.clicked.connect(self.query_fee_clicked)
        self.ui.reminder_pay_btn.clicked.connect(self.reminder_pay_btn_clicked)

    def query_fee_clicked(self):
        print("query_fee_clicked")
        if self.ui.fee_species_comboBox.currentText() == '物业费':
            print("物业费")
            property_fee_reminder(self)
        elif self.ui.fee_species_comboBox.currentText() == '停车费':
            print("停车费")
            parking_fee_reminder(self)

    def reminder_pay_btn_clicked(self, content):
        print("reminder_pay_btn_clicked")
        fee_species = self.ui.fee_species_comboBox.currentText()
        model = self.ui.tableView.model()  # 获取TableView的模型
        rowCount = model.rowCount()  # 获取行数
        data = []
        for row in range(rowCount):
            rowData = []
            for column in range(model.columnCount()):
                index = model.index(row, column)  # 获取单元格的索引
                item = model.data(index)  # 获取单元格的数据
                rowData.append(item)
            data.append(rowData)

        # 获取email和unpaid_fee,姓名
        for row in data:
            email = row[2]
            unpaid_fee = row[3]
            name = row[1]
            email_send(email, unpaid_fee, name, fee_species)

        # 现在，data 列表中包含了TableView的所有行数据
        print(data)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    reminder_fee = ReminderFee()
    reminder_fee.show()
    sys.exit(app.exec_())