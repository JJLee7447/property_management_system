# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_maintenance.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_register_maintenance(object):
    def setupUi(self, register_maintenance):
        register_maintenance.setObjectName("register_maintenance")
        register_maintenance.resize(645, 491)
        self.label = QtWidgets.QLabel(register_maintenance)
        self.label.setGeometry(QtCore.QRect(70, 110, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(register_maintenance)
        self.label_2.setGeometry(QtCore.QRect(420, 110, 72, 15))
        self.label_2.setObjectName("label_2")
        self.report_dateEdit = QtWidgets.QDateEdit(register_maintenance)
        self.report_dateEdit.setGeometry(QtCore.QRect(190, 160, 121, 22))
        self.report_dateEdit.setObjectName("report_dateEdit")
        self.label_3 = QtWidgets.QLabel(register_maintenance)
        self.label_3.setGeometry(QtCore.QRect(70, 160, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(register_maintenance)
        self.label_4.setGeometry(QtCore.QRect(70, 210, 72, 15))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(register_maintenance)
        self.label_5.setGeometry(QtCore.QRect(70, 260, 72, 15))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(register_maintenance)
        self.label_6.setGeometry(QtCore.QRect(70, 310, 141, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(register_maintenance)
        self.label_7.setGeometry(QtCore.QRect(70, 410, 72, 15))
        self.label_7.setObjectName("label_7")
        self.repair_dateEdit = QtWidgets.QDateEdit(register_maintenance)
        self.repair_dateEdit.setGeometry(QtCore.QRect(190, 210, 121, 22))
        self.repair_dateEdit.setObjectName("repair_dateEdit")
        self.resident_id_lineEdit = QtWidgets.QLineEdit(register_maintenance)
        self.resident_id_lineEdit.setGeometry(QtCore.QRect(190, 110, 113, 21))
        self.resident_id_lineEdit.setObjectName("resident_id_lineEdit")
        self.description_textEdit = QtWidgets.QTextEdit(register_maintenance)
        self.description_textEdit.setGeometry(QtCore.QRect(420, 160, 211, 131))
        self.description_textEdit.setObjectName("description_textEdit")
        self.yes = QtWidgets.QRadioButton(register_maintenance)
        self.yes.setGeometry(QtCore.QRect(240, 310, 41, 19))
        self.yes.setChecked(True)
        self.yes.setObjectName("yes")
        self.payment_lineEdit = QtWidgets.QLineEdit(register_maintenance)
        self.payment_lineEdit.setGeometry(QtCore.QRect(190, 260, 113, 21))
        self.payment_lineEdit.setObjectName("payment_lineEdit")
        self.account_lineEdit = QtWidgets.QLineEdit(register_maintenance)
        self.account_lineEdit.setGeometry(QtCore.QRect(190, 410, 113, 21))
        self.account_lineEdit.setObjectName("account_lineEdit")
        self.pushButton = QtWidgets.QPushButton(register_maintenance)
        self.pushButton.setGeometry(QtCore.QRect(420, 450, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_8 = QtWidgets.QLabel(register_maintenance)
        self.label_8.setGeometry(QtCore.QRect(70, 360, 72, 15))
        self.label_8.setObjectName("label_8")
        self.repair_id = QtWidgets.QLineEdit(register_maintenance)
        self.repair_id.setGeometry(QtCore.QRect(190, 360, 113, 21))
        self.repair_id.setObjectName("repair_id")

        self.retranslateUi(register_maintenance)
        QtCore.QMetaObject.connectSlotsByName(register_maintenance)

    def retranslateUi(self, register_maintenance):
        _translate = QtCore.QCoreApplication.translate
        register_maintenance.setWindowTitle(_translate("register_maintenance", "register_miantenance"))
        self.label.setText(_translate("register_maintenance", "住户编号"))
        self.label_2.setText(_translate("register_maintenance", "维修描述"))
        self.label_3.setText(_translate("register_maintenance", "上报时间"))
        self.label_4.setText(_translate("register_maintenance", "维修时间"))
        self.label_5.setText(_translate("register_maintenance", "维修金额"))
        self.label_6.setText(_translate("register_maintenance", "是否从维修基金支出"))
        self.label_7.setText(_translate("register_maintenance", "账号_id"))
        self.yes.setText(_translate("register_maintenance", "是"))
        self.pushButton.setText(_translate("register_maintenance", "确定"))
        self.label_8.setText(_translate("register_maintenance", "维修人_id"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    register_maintenance = QtWidgets.QWidget()
    ui = Ui_register_maintenance()
    ui.setupUi(register_maintenance)
    register_maintenance.show()
    sys.exit(app.exec_())
