# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P_count_fee.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_P_count_fee(object):
    def setupUi(self, P_count_fee):
        P_count_fee.setObjectName("P_count_fee")
        P_count_fee.resize(599, 300)
        self.label = QtWidgets.QLabel(P_count_fee)
        self.label.setGeometry(QtCore.QRect(50, 50, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(P_count_fee)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 72, 15))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(P_count_fee)
        self.pushButton.setGeometry(QtCore.QRect(130, 190, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(P_count_fee)
        self.label_3.setGeometry(QtCore.QRect(300, 50, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(P_count_fee)
        self.label_4.setGeometry(QtCore.QRect(300, 110, 72, 15))
        self.label_4.setObjectName("label_4")
        self.parking_fee = QtWidgets.QLineEdit(P_count_fee)
        self.parking_fee.setGeometry(QtCore.QRect(380, 50, 113, 21))
        self.parking_fee.setReadOnly(True)
        self.parking_fee.setObjectName("parking_fee")
        self.property_fee = QtWidgets.QLineEdit(P_count_fee)
        self.property_fee.setGeometry(QtCore.QRect(380, 100, 113, 21))
        self.property_fee.setReadOnly(True)
        self.property_fee.setObjectName("property_fee")
        self.building_id_comboBox = QtWidgets.QComboBox(P_count_fee)
        self.building_id_comboBox.setGeometry(QtCore.QRect(130, 50, 111, 22))
        self.building_id_comboBox.setObjectName("building_id_comboBox")
        self.house_id_comboBox = QtWidgets.QComboBox(P_count_fee)
        self.house_id_comboBox.setGeometry(QtCore.QRect(130, 110, 111, 22))
        self.house_id_comboBox.setObjectName("house_id_comboBox")

        self.retranslateUi(P_count_fee)
        QtCore.QMetaObject.connectSlotsByName(P_count_fee)

    def retranslateUi(self, P_count_fee):
        _translate = QtCore.QCoreApplication.translate
        P_count_fee.setWindowTitle(_translate("P_count_fee", "P_count_fee"))
        self.label.setText(_translate("P_count_fee", "楼号"))
        self.label_2.setText(_translate("P_count_fee", "房号"))
        self.pushButton.setText(_translate("P_count_fee", "确定"))
        self.label_3.setText(_translate("P_count_fee", "停车费"))
        self.label_4.setText(_translate("P_count_fee", "物业费"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    P_count_fee = QtWidgets.QWidget()
    ui = Ui_P_count_fee()
    ui.setupUi(P_count_fee)
    P_count_fee.show()
    sys.exit(app.exec_())
