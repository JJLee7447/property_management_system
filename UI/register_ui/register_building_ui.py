# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_building.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_register_building(object):
    def setupUi(self, register_building):
        register_building.setObjectName("register_building")
        register_building.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(register_building)
        self.lineEdit.setGeometry(QtCore.QRect(160, 50, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(register_building)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 80, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(register_building)
        self.label.setGeometry(QtCore.QRect(40, 50, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(register_building)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 81, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(register_building)
        self.pushButton.setGeometry(QtCore.QRect(160, 190, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(register_building)
        QtCore.QMetaObject.connectSlotsByName(register_building)

    def retranslateUi(self, register_building):
        _translate = QtCore.QCoreApplication.translate
        register_building.setWindowTitle(_translate("register_building", "register_building"))
        self.label.setText(_translate("register_building", "楼栋号"))
        self.label_2.setText(_translate("register_building", "管理员工ID"))
        self.pushButton.setText(_translate("register_building", "确定"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    register_building = QtWidgets.QWidget()
    ui = Ui_register_building()
    ui.setupUi(register_building)
    register_building.show()
    sys.exit(app.exec_())
