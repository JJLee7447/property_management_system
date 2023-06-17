from PyQt5 import QtCore, QtGui, QtWidgets


def query_resident(self, content, cursor):
    print("query_resident_clicked")
    if content[1] == '':
        try:
            sql = 'SELECT * FROM residents'
            cursor.execute(sql)
            results = cursor.fetchall()

            # 将查询结果表格化形式给 tableView
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            # 设置属性名
            model.setHorizontalHeaderLabels(['住户编号', 'email', '姓名', '公司', '家庭人数'])
            # 将结果添加到模型中
            for row in results:
                row_items = [QtGui.QStandardItem(str(item)) for item in row]
                model.appendRow(row_items)
            # 将模型设置给tableView
            self.ui.tableView.setModel(model)

        except Exception as e:
            print(e)
            print("查询失败")

    else:
        try:
            sql = '''SELECT * FROM residents WHERE resident_id = %s'''
            cursor.execute(sql, content[1])
            results = cursor.fetchall()

            # 将查询结果表格化形式给 tableView
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            # 设置属性名
            model.setHorizontalHeaderLabels(['住户编号', 'email', '姓名', '公司', '家庭人数'])
            # 将结果添加到模型中
            for row in results:
                row_items = [QtGui.QStandardItem(str(item)) for item in row]
                model.appendRow(row_items)
            # 将模型设置给tableView
            self.ui.tableView.setModel(model)

        except Exception as e:
            print(e)
            print("查询失败")


def query_building(self, content, cursor):
    print("楼栋信息")
    if content[1] == '':
        try:
            sql = 'SELECT building_id, property_id FROM buildings'
            cursor.execute(sql)
            results = cursor.fetchall()
            # 将查询结果表格化形式给 tableView
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            # model.setEditStrategy(QtGui.QSqlTableModel.OnFieldChange)
            # 设置属性名
            model.setHorizontalHeaderLabels(['楼栋编号', '负责人id'])
            # 将结果添加到模型中
            for row in results:
                row_items = [QtGui.QStandardItem(str(item)) for item in row]
                model.appendRow(row_items)
            # 将模型设置给tableView
            self.ui.tableView.setModel(model)

        except Exception as e:
            print(e)
            print("查询失败")
    else:
        try:
            sql = '''SELECT building_id, property_id FROM buildings WHERE building_id = %s'''
            cursor.execute(sql, content[1])
            results = cursor.fetchall()
            # 将查询结果表格化形式给 tableView
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            # 设置属性名
            model.setHorizontalHeaderLabels(['楼栋编号', '负责人id'])
            # 将结果添加到模型中
            for row in results:
                row_items = [QtGui.QStandardItem(str(item)) for item in row]
                model.appendRow(row_items)
            # 将模型设置给tableView
            self.ui.tableView.setModel(model)

        except Exception as e:
            print(e)
            print("查询失败")


def query_house(self, content, cursor):
    print("住房信息")
    if content[1] == '':
        try:
            sql = 'SELECT * FROM house'
            cursor.execute(sql)
            results = cursor.fetchall()
            # 将查询结果表格化形式给 tableView
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            # 设置属性名
            model.setHorizontalHeaderLabels(['房间编号', '楼栋编号', '房间面积', '住户编号'])
            # 将结果添加到模型中
            for row in results:
                row_items = [QtGui.QStandardItem(str(item)) for item in row]
                model.appendRow(row_items)
            # 将模型设置给tableView
            self.ui.tableView.setModel(model)

        except Exception as e:
            print(e)
            print("查询失败")
    else:
        try:
            sql = '''SELECT * FROM house WHERE house_id = %s'''
            cursor.execute(sql, content[1])
            results = cursor.fetchall()
            # 将查询结果表格化形式给 tableView
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            # 设置属性名
            model.setHorizontalHeaderLabels(['房间编号', '楼栋编号', '房间面积', '住户编号'])
            # 将结果添加到模型中
            for row in results:
                row_items = [QtGui.QStandardItem(str(item)) for item in row]
                model.appendRow(row_items)
            # 将模型设置给tableView
            self.ui.tableView.setModel(model)

        except Exception as e:
            print(e)
            print("查询失败")


def query_maintenance(self, content, cursor):
    print("维修信息")
    if content[1] == '':
        try:
            sql = 'SELECT * FROM maintenance'
            cursor.execute(sql)
            results = cursor.fetchall()
            # 将查询结果表格化形式给 tableView
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            # 设置属性名
            model.setHorizontalHeaderLabels(['维修编号', '住户编号', '维修内容', '报告日期', '维修日期', '维修费用', '是否从维修基金支付', '维修人员编号', '账户编号'])
            # 将结果添加到模型中
            for row in results:
                row_items = [QtGui.QStandardItem(str(item)) for item in row]
                model.appendRow(row_items)
            # 将模型设置给tableView
            self.ui.tableView.setModel(model)

        except Exception as e:
            print(e)
            print("查询失败")
    else:
        try:
            sql = '''SELECT * FROM maintenance WHERE maintenance_id = %s'''
            cursor.execute(sql, content[1])
            # 将查询结果表格化形式给 tableView
            # 创建一个模型
            results = cursor.fetchall()
            model = QtGui.QStandardItemModel()
            # 设置属性名
            model.setHorizontalHeaderLabels(['维修编号', '住户编号', '维修内容', '报告日期', '维修日期', '维修费用', '是否从维修基金支付', '维修人员编号', '账户编号'])
            # 将结果添加到模型中
            for row in results:
                row_items = [QtGui.QStandardItem(str(item)) for item in row]
                model.appendRow(row_items)
            # 将模型设置给tableView
            self.ui.tableView.setModel(model)

        except Exception as e:
            print(e)
            print("查询失败")


def query_parking_fees(self, content, cursor):
    print("停车费信息")
    if content[1] == '':
        try:
            sql = 'SELECT * FROM parking_fees'
            cursor.execute(sql)
            results = cursor.fetchall()
            # 将查询结果表格化形式给 tableView
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            # 设置属性名
            model.setHorizontalHeaderLabels(['停车费编号', '车位编号', '年', '月', '应缴费金额', '实缴费金额', '缴费日期', '员工编号', '是否缴费'])
            # 将结果添加到模型中
            for row in results:
                row_items = [QtGui.QStandardItem(str(item)) for item in row]
                model.appendRow(row_items)
            # 将模型设置给tableView
            self.ui.tableView.setModel(model)

        except Exception as e:
            print(e)
            print("查询失败")
    else:
        try:
            sql = '''SELECT * FROM parking_fees WHERE parking_fee_id = %s'''
            cursor.execute(sql, content[1])
            results = cursor.fetchall()
            # 将查询结果表格化形式给 tableView
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            # 设置属性名
            model.setHorizontalHeaderLabels(['停车费编号', '车位编号', '年', '月', '应缴费金额', '实缴费金额', '缴费日期', '员工编号', '是否缴费'])
            # 将结果添加到模型中
            for row in results:
                row_items = [QtGui.QStandardItem(str(item)) for item in row]
                model.appendRow(row_items)
            # 将模型设置给tableView
            self.ui.tableView.setModel(model)

        except Exception as e:
            print(e)
            print("查询失败")


def query_parking_spaces(self, content, cursor):
    print("车位信息")
    if content[1] == '':
        try:
            sql = 'SELECT * FROM parking_spaces'
            cursor.execute(sql)
            results = cursor.fetchall()
            # 将查询结果表格化形式给 tableView
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            # 设置属性名
            model.setHorizontalHeaderLabels(['车位编号', '楼栋编号', '房间编号', '车牌号码', '停车费'])
            # 将结果添加到模型中
            for row in results:
                row_items = [QtGui.QStandardItem(str(item)) for item in row]
                model.appendRow(row_items)
            # 将模型设置给tableView
            self.ui.tableView.setModel(model)

        except Exception as e:
            print(e)
            print("查询失败")
    else:
        try:
            sql = '''SELECT * FROM parking_spaces WHERE parking_space_id = %s'''
            cursor.execute(sql, content[1])
            results = cursor.fetchall()
            # 将查询结果表格化形式给 tableView
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            # 设置属性名
            model.setHorizontalHeaderLabels(['车位编号', '楼栋编号', '房间编号', '车牌号码', '停车费', '是否缴费'])
            # 将结果添加到模型中
            for row in results:
                row_items = [QtGui.QStandardItem(str(item)) for item in row]
                model.appendRow(row_items)
            # 将模型设置给tableView
            self.ui.tableView.setModel(model)

        except Exception as e:
            print(e)
            print("查询失败")


def query_property_fees(self, content, cursor):
    print("物业管理信息")
    if content[1] == '':
        try:
            sql = 'SELECT * FROM property_fees'
            cursor.execute(sql)
            results = cursor.fetchall()
            # 将查询结果表格化形式给 tableView
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            # 设置属性名
            model.setHorizontalHeaderLabels(['物业费编号', '年', '月', '应缴费金额', '实缴费金额', '缴费日期', '员工编号', '楼栋编号', '房间编号', '是否缴费'])
            # 将结果添加到模型中
            for row in results:
                row_items = [QtGui.QStandardItem(str(item)) for item in row]
                model.appendRow(row_items)
            # 将模型设置给tableView
            self.ui.tableView.setModel(model)

        except Exception as e:
            print(e)
            print("查询失败")
    else:
        try:
            sql = '''SELECT * FROM property_fees WHERE property_fee_id = %s'''
            cursor.execute(sql, content[1])
            results = cursor.fetchall()
            # 将查询结果表格化形式给 tableView
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            # 设置属性名
            model.setHorizontalHeaderLabels(['物业费编号', '年', '月', '应缴费金额', '实缴费金额', '缴费日期', '员工编号', '楼栋编号', '房间编号'])
            # 将结果添加到模型中
            for row in results:
                row_items = [QtGui.QStandardItem(str(item)) for item in row]
                model.appendRow(row_items)
            # 将模型设置给tableView
            self.ui.tableView.setModel(model)

        except Exception as e:
            print(e)
            print("查询失败")


def query_property_staff(self, content, cursor):
    print("物业人员信息")
    if content[1] == '':
        try:
            sql = 'SELECT property_id, staff_name FROM property_staff'
            cursor.execute(sql)
            results = cursor.fetchall()
            # 将查询结果表格化形式给 tableView
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            # 设置属性名
            model.setHorizontalHeaderLabels(['员工编号', '员工姓名'])
            # 将结果添加到模型中
            for row in results:
                row_items = [QtGui.QStandardItem(str(item)) for item in row]
                model.appendRow(row_items)
            # 将模型设置给tableView
            self.ui.tableView.setModel(model)

        except Exception as e:
            print(e)
            print("查询失败")
    else:
        try:
            sql = '''SELECT property_id,staff_name FROM property_staff WHERE property_id = %s'''
            cursor.execute(sql, content[1])
            results = cursor.fetchall()
            # 将查询结果表格化形式给 tableView
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            # 设置属性名
            model.setHorizontalHeaderLabels(['员工编号', '员工姓名'])
            # 将结果添加到模型中
            for row in results:
                row_items = [QtGui.QStandardItem(str(item)) for item in row]
                model.appendRow(row_items)
            # 将模型设置给tableView
            self.ui.tableView.setModel(model)

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
            # 将查询结果表格化形式给 tableView
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            # 设置属性名
            model.setHorizontalHeaderLabels(['维修基金编号', '维修基金金额'])
            # 将结果添加到模型中
            for row in results:
                row_items = [QtGui.QStandardItem(str(item)) for item in row]
                model.appendRow(row_items)
            # 将模型设置给tableView
            self.ui.tableView.setModel(model)

        except Exception as e:
            print(e)
            print("查询失败")
    else:
        try:
            sql = '''SELECT * FROM repair_fund WHERE account_id = %s'''
            cursor.execute(sql, content[1])
            results = cursor.fetchall()
            # 将查询结果表格化形式给 tableView
            # 创建一个模型
            model = QtGui.QStandardItemModel()
            # 设置属性名
            model.setHorizontalHeaderLabels(['维修基金编号', '维修基金金额'])
            # 将结果添加到模型中
            for row in results:
                row_items = [QtGui.QStandardItem(str(item)) for item in row]
                model.appendRow(row_items)
            # 将模型设置给tableView
            self.ui.tableView.setModel(model)

        except Exception as e:
            print(e)
            print("查询失败")
