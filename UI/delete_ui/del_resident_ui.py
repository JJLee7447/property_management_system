# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'del_resident.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_del_resident(object):
    def setupUi(self, del_resident):
        del_resident.setObjectName("del_resident")
        del_resident.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(del_resident)
        self.lineEdit.setGeometry(QtCore.QRect(150, 40, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.resident_id_label = QtWidgets.QLabel(del_resident)
        self.resident_id_label.setGeometry(QtCore.QRect(30, 40, 101, 16))
        self.resident_id_label.setObjectName("resident_id_label")
        self.name_label = QtWidgets.QLabel(del_resident)
        self.name_label.setGeometry(QtCore.QRect(30, 80, 72, 15))
        self.name_label.setObjectName("name_label")
        self.lineEdit_2 = QtWidgets.QLineEdit(del_resident)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 80, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(del_resident)
        self.pushButton.setGeometry(QtCore.QRect(150, 190, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(del_resident)
        QtCore.QMetaObject.connectSlotsByName(del_resident)

    def retranslateUi(self, del_resident):
        _translate = QtCore.QCoreApplication.translate
        del_resident.setWindowTitle(_translate("del_resident", "del_resident"))
        self.resident_id_label.setText(_translate("del_resident", "resident_id"))
        self.name_label.setText(_translate("del_resident", "name"))
        self.pushButton.setText(_translate("del_resident", "确定"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    del_resident = QtWidgets.QWidget()
    ui = Ui_del_resident()
    ui.setupUi(del_resident)
    del_resident.show()
    sys.exit(app.exec_())
