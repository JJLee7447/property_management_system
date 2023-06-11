# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(840, 602)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.register_btn = QtWidgets.QPushButton(self.centralwidget)
        self.register_btn.setGeometry(QtCore.QRect(550, 380, 93, 28))
        self.register_btn.setObjectName("register_btn")
        self.register_com_box = QtWidgets.QComboBox(self.centralwidget)
        self.register_com_box.setGeometry(QtCore.QRect(550, 420, 91, 22))
        self.register_com_box.setObjectName("register_com_box")
        self.register_com_box.addItem("")
        self.register_com_box.addItem("")
        self.register_com_box.addItem("")
        self.register_com_box.addItem("")
        self.register_com_box.addItem("")
        self.register_com_box.addItem("")
        self.register_com_box.addItem("")
        self.register_com_box.addItem("")
        self.register_com_box.addItem("")
        self.query_btn = QtWidgets.QPushButton(self.centralwidget)
        self.query_btn.setGeometry(QtCore.QRect(140, 380, 93, 28))
        self.query_btn.setObjectName("query_btn")
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setGeometry(QtCore.QRect(680, 70, 93, 28))
        self.clear_btn.setObjectName("clear_btn")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(680, 110, 93, 28))
        self.exit_btn.setObjectName("exit_btn")
        self.query_editor = QtWidgets.QLineEdit(self.centralwidget)
        self.query_editor.setGeometry(QtCore.QRect(250, 420, 113, 21))
        self.query_editor.setObjectName("query_editor")
        self.update_btn = QtWidgets.QPushButton(self.centralwidget)
        self.update_btn.setGeometry(QtCore.QRect(140, 470, 93, 28))
        self.update_btn.setObjectName("update_btn")
        self.update_com_box = QtWidgets.QComboBox(self.centralwidget)
        self.update_com_box.setGeometry(QtCore.QRect(140, 510, 91, 22))
        self.update_com_box.setObjectName("update_com_box")
        self.update_com_box.addItem("")
        self.update_com_box.addItem("")
        self.update_com_box.addItem("")
        self.update_com_box.addItem("")
        self.del_com_box = QtWidgets.QComboBox(self.centralwidget)
        self.del_com_box.setGeometry(QtCore.QRect(550, 510, 91, 22))
        self.del_com_box.setObjectName("del_com_box")
        self.del_com_box.addItem("")
        self.del_com_box.addItem("")
        self.del_com_box.addItem("")
        self.del_btn = QtWidgets.QPushButton(self.centralwidget)
        self.del_btn.setGeometry(QtCore.QRect(550, 470, 93, 28))
        self.del_btn.setObjectName("del_btn")
        self.query_com_box = QtWidgets.QComboBox(self.centralwidget)
        self.query_com_box.setGeometry(QtCore.QRect(140, 420, 91, 22))
        self.query_com_box.setObjectName("query_com_box")
        self.query_com_box.addItem("")
        self.query_com_box.addItem("")
        self.query_com_box.addItem("")
        self.query_com_box.addItem("")
        self.query_com_box.addItem("")
        self.query_com_box.addItem("")
        self.query_com_box.addItem("")
        self.query_com_box.addItem("")
        self.query_com_box.addItem("")
        self.count_fee_btn = QtWidgets.QPushButton(self.centralwidget)
        self.count_fee_btn.setGeometry(QtCore.QRect(680, 210, 131, 28))
        self.count_fee_btn.setObjectName("count_fee_btn")
        self.sta_pro_fee_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sta_pro_fee_btn.setGeometry(QtCore.QRect(680, 260, 93, 28))
        self.sta_pro_fee_btn.setObjectName("sta_pro_fee_btn")
        self.sum_parking_space_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sum_parking_space_btn.setGeometry(QtCore.QRect(680, 320, 131, 28))
        self.sum_parking_space_btn.setObjectName("sum_parking_space_btn")
        self.sum_resident_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sum_resident_btn.setGeometry(QtCore.QRect(680, 380, 131, 28))
        self.sum_resident_btn.setObjectName("sum_resident_btn")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(140, 40, 501, 331))
        self.tableView.setObjectName("tableView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 840, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.exit_btn.clicked.connect(MainWindow.close) # type: ignore
        self.clear_btn.clicked.connect(self.tableView.clearSelection) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.register_btn.setText(_translate("MainWindow", "登记"))
        self.register_com_box.setItemText(0, _translate("MainWindow", "住户信息"))
        self.register_com_box.setItemText(1, _translate("MainWindow", "楼栋信息"))
        self.register_com_box.setItemText(2, _translate("MainWindow", "住房信息"))
        self.register_com_box.setItemText(3, _translate("MainWindow", "物业费信息"))
        self.register_com_box.setItemText(4, _translate("MainWindow", "停车费信息"))
        self.register_com_box.setItemText(5, _translate("MainWindow", "车位信息"))
        self.register_com_box.setItemText(6, _translate("MainWindow", "维修信息"))
        self.register_com_box.setItemText(7, _translate("MainWindow", "维修基金"))
        self.register_com_box.setItemText(8, _translate("MainWindow", "员工信息"))
        self.query_btn.setText(_translate("MainWindow", "查询"))
        self.clear_btn.setText(_translate("MainWindow", "clear"))
        self.exit_btn.setText(_translate("MainWindow", "exit"))
        self.update_btn.setText(_translate("MainWindow", "更新"))
        self.update_com_box.setItemText(0, _translate("MainWindow", "住户信息"))
        self.update_com_box.setItemText(1, _translate("MainWindow", "员工信息"))
        self.update_com_box.setItemText(2, _translate("MainWindow", "楼栋信息"))
        self.update_com_box.setItemText(3, _translate("MainWindow", "车位信息"))
        self.del_com_box.setItemText(0, _translate("MainWindow", "住户信息"))
        self.del_com_box.setItemText(1, _translate("MainWindow", "车位信息"))
        self.del_com_box.setItemText(2, _translate("MainWindow", "员工信息"))
        self.del_btn.setText(_translate("MainWindow", "删除"))
        self.query_com_box.setItemText(0, _translate("MainWindow", "住户信息"))
        self.query_com_box.setItemText(1, _translate("MainWindow", "楼栋信息"))
        self.query_com_box.setItemText(2, _translate("MainWindow", "住房信息"))
        self.query_com_box.setItemText(3, _translate("MainWindow", "物业费信息"))
        self.query_com_box.setItemText(4, _translate("MainWindow", "停车费信息"))
        self.query_com_box.setItemText(5, _translate("MainWindow", "车位信息"))
        self.query_com_box.setItemText(6, _translate("MainWindow", "维修信息"))
        self.query_com_box.setItemText(7, _translate("MainWindow", "维修基金"))
        self.query_com_box.setItemText(8, _translate("MainWindow", "员工信息"))
        self.count_fee_btn.setText(_translate("MainWindow", "计算物业、停车费"))
        self.sta_pro_fee_btn.setText(_translate("MainWindow", "统计物业费"))
        self.sum_parking_space_btn.setText(_translate("MainWindow", "计算停车位总数"))
        self.sum_resident_btn.setText(_translate("MainWindow", "计算小区总户数"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
