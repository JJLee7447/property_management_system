from PyQt5 import QtCore, QtGui, QtWidgets


def query_resident(self, content, cursor):
    print("query_resident_clicked")
    if content[1] == '':
        try:
            sql = 'SELECT * FROM residents'
            cursor.execute(sql)
            results = cursor.fetchall()
            residents_list = [f'{result[0]} - {result[1]} - {result[2]} - {result[3]}' for result in results]
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            for resident in residents_list:
                item = QtGui.QStandardItem(resident)
                model.appendRow(item)
            # 将模型设置给listView
            self.ui.listView.setModel(model)
        except Exception as e:
            print(e)
            print("查询失败")

    else:
        try:
            sql = '''SELECT * FROM residents WHERE resident_id = %s'''
            cursor.execute(sql, content[1])
            results = cursor.fetchall()
            residents_list = [f'{result[0]} - {result[1]} - {result[2]} - {result[3]}' for result in results]
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            for resident in residents_list:
                item = QtGui.QStandardItem(resident)
                model.appendRow(item)
            # 将模型设置给listView
            self.ui.listView.setModel(model)

        except:
            print("查询失败")


def query_building(self, content, cursor):
    print("楼栋信息")
    if content[1] == '':
        try:
            sql = 'SELECT * FROM buildings'
            cursor.execute(sql)
            results = cursor.fetchall()
            buildings_list = [f'{result[0]} - {result[1]} - {result[2]}' for result in results]
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            for building in buildings_list:
                item = QtGui.QStandardItem(building)
                model.appendRow(item)
            # 将模型设置给listView
            self.ui.listView.setModel(model)

        except:
            print("查询失败")
    else:
        try:
            sql = '''SELECT * FROM buildings WHERE building_id = %s'''
            cursor.execute(sql, content[1])
            results = cursor.fetchall()
            buildings_list = [f'{result[0]} - {result[1]} - {result[2]}' for result in results]
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            for building in buildings_list:
                item = QtGui.QStandardItem(building)
                model.appendRow(item)
            # 将模型设置给listView
            self.ui.listView.setModel(model)

        except:
            print("查询失败")


def query_house(self, content, cursor):
    print("住房信息")
    if content[1] == '':
        try:
            sql = 'SELECT * FROM house'
            cursor.execute(sql)
            results = cursor.fetchall()
            houses_list = [f'{result[0]} - {result[1]} - {result[2]} - {result[3]}' for result in results]
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            for house in houses_list:
                item = QtGui.QStandardItem(house)
                model.appendRow(item)
            # 将模型设置给listView
            self.ui.listView.setModel(model)

        except:
            print("查询失败")
    else:
        try:
            sql = '''SELECT * FROM house WHERE house_id = %s'''
            cursor.execute(sql, content[1])
            results = cursor.fetchall()
            houses_list = [f'{result[0]} - {result[1]} - {result[2]} - {result[3]}' for result in results]
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            for house in houses_list:
                item = QtGui.QStandardItem(house)
                model.appendRow(item)
            # 将模型设置给listView
            self.ui.listView.setModel(model)

        except:
            print("查询失败")


def query_maintenance(self, content, cursor):
    print("维修信息")
    if content[1] == '':
        try:
            sql = 'SELECT * FROM maintenance'
            cursor.execute(sql)
            results = cursor.fetchall()
            maintenance_list = [f'{result[0]} - {result[1]} - {result[2]} - {result[3]} - {result[4]} - {result[5]} - {result[6]} - {result[7]} ' for result in results]
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            for maintenance in maintenance_list:
                item = QtGui.QStandardItem(maintenance)
                model.appendRow(item)
            # 将模型设置给listView
            self.ui.listView.setModel(model)

        except:
            print("查询失败")
    else:
        try:
            sql = '''SELECT * FROM maintenance WHERE maintenance_id = %s'''
            cursor.execute(sql, content[1])
            results = cursor.fetchall()
            maintenance_list = [
                f'{result[0]} - {result[1]} - {result[2]} - {result[3]} - {result[4]} - {result[5]} - {result[6]} - {result[7]} '
                for result in results]
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            for maintenance in maintenance_list:
                item = QtGui.QStandardItem(maintenance)
                model.appendRow(item)
            # 将模型设置给listView
            self.ui.listView.setModel(model)

        except:
            print("查询失败")


def query_parking_fees(self, content, cursor):
    print("停车费信息")
    if content[1] == '':
        try:
            sql = 'SELECT * FROM parking_fees'
            cursor.execute(sql)
            results = cursor.fetchall()
            parking_fees_list = [f'{result[0]} - {result[1]} - {result[2]} - {result[3]} - {result[4]} - {result[5]} - {result[6]} - {result[7]} ' for result in results]
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            for parking_fees in parking_fees_list:
                item = QtGui.QStandardItem(parking_fees)
                model.appendRow(item)
            # 将模型设置给listView
            self.ui.listView.setModel(model)

        except:
            print("查询失败")
    else:
        try:
            sql = '''SELECT * FROM parking_fees WHERE parking_fee_id = %s'''
            cursor.execute(sql, content[1])
            results = cursor.fetchall()
            parking_fees_list = [
                f'{result[0]} - {result[1]} - {result[2]} - {result[3]} - {result[4]} - {result[5]} - {result[6]} - {result[7]} '
                for result in results]

            # 创建一个模型
            model = QtGui.QStandardItemModel()
            for parking_fees in parking_fees_list:
                item = QtGui.QStandardItem(parking_fees)
                model.appendRow(item)
            # 将模型设置给listView
            self.ui.listView.setModel(model)

        except:
            print("查询失败")


def query_parking_spaces(self, content, cursor):
    print("车位信息")
    if content[1] == '':
        try:
            sql = 'SELECT * FROM parking_spaces'
            cursor.execute(sql)
            results = cursor.fetchall()
            parking_spaces_list = [f'{result[0]} - {result[1]} - {result[2]} - {result[3]} - {result[4]}' for result in results]
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            for parking_spaces in parking_spaces_list:
                item = QtGui.QStandardItem(parking_spaces)
                model.appendRow(item)
            # 将模型设置给listView
            self.ui.listView.setModel(model)

        except:
            print("查询失败")
    else:
        try:
            sql = '''SELECT * FROM parking_spaces WHERE parking_space_id = %s'''
            cursor.execute(sql, content[1])
            results = cursor.fetchall()
            parking_spaces_list = [f'{result[0]} - {result[1]} - {result[2]}' for result in results]
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            for parking_spaces in parking_spaces_list:
                item = QtGui.QStandardItem(parking_spaces)
                model.appendRow(item)
            # 将模型设置给listView
            self.ui.listView.setModel(model)

        except:
            print("查询失败")


def query_property_fees(self, content, cursor):
    print("物业管理信息")
    if content[1] == '':
        try:
            sql = 'SELECT * FROM property_fees'
            cursor.execute(sql)
            results = cursor.fetchall()
            property_management_list = [
                f'{result[0]} - {result[1]} - {result[2]} - {result[3]} - {result[4]} - {result[5]} - {result[6]} - {result[7]} - {result[8]}  '
                for result in results]
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            for property_management in property_management_list:
                item = QtGui.QStandardItem(property_management)
                model.appendRow(item)
            # 将模型设置给listView
            self.ui.listView.setModel(model)

        except:
            print("查询失败")
    else:
        try:
            sql = '''SELECT * FROM property_fees WHERE property_fee_id = %s'''
            cursor.execute(sql, content[1])
            results = cursor.fetchall()
            property_management_list = [
                f'{result[0]} - {result[1]} - {result[2]} - {result[3]} - {result[4]} - {result[5]} - {result[6]} - {result[7]} - {result[8]}  '
                for result in results]
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            for property_management in property_management_list:
                item = QtGui.QStandardItem(property_management)
                model.appendRow(item)
            # 将模型设置给listView
            self.ui.listView.setModel(model)

        except:
            print("查询失败")


def query_property_staff(self, content, cursor):
    print("物业人员信息")
    if content[1] == '':
        try:
            sql = 'SELECT * FROM property_staff'
            cursor.execute(sql)
            results = cursor.fetchall()
            print(results)
            property_staff_list = [f'{result[0]} - {result[1]} - {result[2]}' for result in results]
            property_staff_list.insert(0, '员工编号 - 员工姓名 - 密码')
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            for property_staff in property_staff_list:
                item = QtGui.QStandardItem(property_staff)
                model.appendRow(item)
            # 将模型设置给listView
            self.ui.listView.setModel(model)

        except Exception as e:
            print(e)
            print("查询失败")
    else:
        try:
            sql = '''SELECT * FROM property_staff WHERE property_id = %s'''
            cursor.execute(sql, content[1])
            results = cursor.fetchall()
            property_staff_list = [f'{result[0]} - {result[1]} - {result[2]}' for result in results]
            # 创建一个模型
            print(property_staff_list)
            property_staff_list.insert(0, '员工编号 - 员工姓名 - 密码')
            model = QtGui.QStandardItemModel()
            for property_staff in property_staff_list:
                item = QtGui.QStandardItem(property_staff)
                print(type(item))
                print(item)
                model.appendRow(item)
            # 将模型设置给listView
            self.ui.listView.setModel(model)

        except Exception as e:
            print(e)
            print("查询失败")


def query_repair_fund(self, content, cursor):
    print("维修基金信息")
    if content[1] == '':
        try:
            sql = 'SELECT * FROM repair_fund'
            cursor.execute(sql)
            results = cursor.fetchall()
            repair_fund_list = [f'{result[0]} - {result[1]}' for result in results]
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            for repair_fund in repair_fund_list:
                item = QtGui.QStandardItem(repair_fund)
                model.appendRow(item)
            # 将模型设置给listView
            self.ui.listView.setModel(model)

        except Exception as e:
            print(e)
            print("查询失败")
    else:
        try:
            sql = '''SELECT * FROM repair_fund WHERE account_id = %s'''
            cursor.execute(sql, content[1])
            results = cursor.fetchall()
            repair_fund_list = [f'{result[0]} - {result[1]}' for result in results]
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            for repair_fund in repair_fund_list:
                item = QtGui.QStandardItem(repair_fund)
                model.appendRow(item)
            # 将模型设置给listView
            self.ui.listView.setModel(model)


        except Exception as e:
            print(e)
            print("查询失败")
