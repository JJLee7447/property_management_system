from login_ui import Ui_login
from src.mainwindow import MainWindow
import sys
from src.db_config import db_connect
from PyQt5 import QtWidgets, QtCore, QtGui


class Login(Ui_login, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec_())