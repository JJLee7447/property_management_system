# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_property_fees.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_register_property_fees(object):
    def setupUi(self, register_property_fees):
        register_property_fees.setObjectName("register_property_fees")
        register_property_fees.resize(569, 436)
        self.label = QtWidgets.QLabel(register_property_fees)
        self.label.setGeometry(QtCore.QRect(60, 60, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(register_property_fees)
        self.label_2.setGeometry(QtCore.QRect(60, 110, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(register_property_fees)
        self.label_3.setGeometry(QtCore.QRect(60, 150, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(register_property_fees)
        self.label_4.setGeometry(QtCore.QRect(60, 190, 72, 15))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(register_property_fees)
        self.label_5.setGeometry(QtCore.QRect(60, 230, 72, 15))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(register_property_fees)
        self.label_6.setGeometry(QtCore.QRect(60, 270, 72, 15))
        self.label_6.setObjectName("label_6")
        self.year_lineEdit = QtWidgets.QLineEdit(register_property_fees)
        self.year_lineEdit.setGeometry(QtCore.QRect(170, 60, 113, 21))
        self.year_lineEdit.setReadOnly(True)
        self.year_lineEdit.setObjectName("year_lineEdit")
        self.month_lineEdit = QtWidgets.QLineEdit(register_property_fees)
        self.month_lineEdit.setGeometry(QtCore.QRect(170, 110, 113, 21))
        self.month_lineEdit.setReadOnly(True)
        self.month_lineEdit.setObjectName("month_lineEdit")
        self.due_payment_lineEdit = QtWidgets.QLineEdit(register_property_fees)
        self.due_payment_lineEdit.setGeometry(QtCore.QRect(170, 150, 113, 21))
        self.due_payment_lineEdit.setObjectName("due_payment_lineEdit")
        self.payment_lineEdit = QtWidgets.QLineEdit(register_property_fees)
        self.payment_lineEdit.setGeometry(QtCore.QRect(170, 190, 113, 21))
        self.payment_lineEdit.setObjectName("payment_lineEdit")
        self.paid_dateEdit = QtWidgets.QDateEdit(register_property_fees)
        self.paid_dateEdit.setGeometry(QtCore.QRect(170, 230, 110, 22))
        self.paid_dateEdit.setObjectName("paid_dateEdit")
        self.staff_id_lineEdit = QtWidgets.QLineEdit(register_property_fees)
        self.staff_id_lineEdit.setGeometry(QtCore.QRect(170, 270, 113, 21))
        self.staff_id_lineEdit.setObjectName("staff_id_lineEdit")
        self.pushButton = QtWidgets.QPushButton(register_property_fees)
        self.pushButton.setGeometry(QtCore.QRect(170, 340, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(register_property_fees)
        self.label_7.setGeometry(QtCore.QRect(350, 120, 72, 15))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(register_property_fees)
        self.label_8.setGeometry(QtCore.QRect(350, 190, 72, 15))
        self.label_8.setObjectName("label_8")
        self.building_id_lineEdit = QtWidgets.QLineEdit(register_property_fees)
        self.building_id_lineEdit.setGeometry(QtCore.QRect(420, 120, 113, 21))
        self.building_id_lineEdit.setObjectName("building_id_lineEdit")
        self.house_id_lineEdit = QtWidgets.QLineEdit(register_property_fees)
        self.house_id_lineEdit.setGeometry(QtCore.QRect(420, 180, 113, 21))
        self.house_id_lineEdit.setObjectName("house_id_lineEdit")

        self.retranslateUi(register_property_fees)
        QtCore.QMetaObject.connectSlotsByName(register_property_fees)

    def retranslateUi(self, register_property_fees):
        _translate = QtCore.QCoreApplication.translate
        register_property_fees.setWindowTitle(_translate("register_property_fees", "register_property_fees"))
        self.label.setText(_translate("register_property_fees", "年"))
        self.label_2.setText(_translate("register_property_fees", "月"))
        self.label_3.setText(_translate("register_property_fees", "应付物业费"))
        self.label_4.setText(_translate("register_property_fees", "实付物业费"))
        self.label_5.setText(_translate("register_property_fees", "付费时间"))
        self.label_6.setText(_translate("register_property_fees", "员工_id"))
        self.pushButton.setText(_translate("register_property_fees", "确定"))
        self.label_7.setText(_translate("register_property_fees", "楼号"))
        self.label_8.setText(_translate("register_property_fees", "房号"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    register_property_fees = QtWidgets.QWidget()
    ui = Ui_register_property_fees()
    ui.setupUi(register_property_fees)
    register_property_fees.show()
    sys.exit(app.exec_())
