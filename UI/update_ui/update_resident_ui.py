# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_resident.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_update_resident(object):
    def setupUi(self, update_resident):
        update_resident.setObjectName("update_resident")
        update_resident.resize(400, 331)
        self.label_3 = QtWidgets.QLabel(update_resident)
        self.label_3.setGeometry(QtCore.QRect(50, 160, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(update_resident)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(update_resident)
        self.label.setGeometry(QtCore.QRect(50, 80, 72, 15))
        self.label.setObjectName("label")
        self.family_size_edit = QtWidgets.QLineEdit(update_resident)
        self.family_size_edit.setGeometry(QtCore.QRect(180, 200, 113, 21))
        self.family_size_edit.setObjectName("family_size_edit")
        self.name_edit = QtWidgets.QLineEdit(update_resident)
        self.name_edit.setGeometry(QtCore.QRect(180, 120, 113, 21))
        self.name_edit.setObjectName("name_edit")
        self.employer_edit = QtWidgets.QLineEdit(update_resident)
        self.employer_edit.setGeometry(QtCore.QRect(180, 160, 113, 21))
        self.employer_edit.setObjectName("employer_edit")
        self.label_4 = QtWidgets.QLabel(update_resident)
        self.label_4.setGeometry(QtCore.QRect(50, 200, 91, 16))
        self.label_4.setObjectName("label_4")
        self.email_edit = QtWidgets.QLineEdit(update_resident)
        self.email_edit.setGeometry(QtCore.QRect(180, 80, 113, 21))
        self.email_edit.setObjectName("email_edit")
        self.pushButton = QtWidgets.QPushButton(update_resident)
        self.pushButton.setGeometry(QtCore.QRect(50, 260, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(update_resident)
        self.label_5.setGeometry(QtCore.QRect(50, 50, 101, 16))
        self.label_5.setObjectName("label_5")
        self.resident_id_comboBox = QtWidgets.QComboBox(update_resident)
        self.resident_id_comboBox.setGeometry(QtCore.QRect(180, 50, 111, 22))
        self.resident_id_comboBox.setObjectName("resident_id_comboBox")

        self.retranslateUi(update_resident)
        QtCore.QMetaObject.connectSlotsByName(update_resident)

    def retranslateUi(self, update_resident):
        _translate = QtCore.QCoreApplication.translate
        update_resident.setWindowTitle(_translate("update_resident", "update_resident"))
        self.label_3.setText(_translate("update_resident", "employer"))
        self.label_2.setText(_translate("update_resident", "name"))
        self.label.setText(_translate("update_resident", "email"))
        self.label_4.setText(_translate("update_resident", "family_size"))
        self.pushButton.setText(_translate("update_resident", "确定"))
        self.label_5.setText(_translate("update_resident", "resident_id"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    update_resident = QtWidgets.QWidget()
    ui = Ui_update_resident()
    ui.setupUi(update_resident)
    update_resident.show()
    sys.exit(app.exec_())
