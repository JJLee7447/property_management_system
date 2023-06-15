from login_ui import Ui_login
from src.mainwindow import MainWindow
import sys
from src.db_config import db_connect
from PyQt5 import QtWidgets


class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_login()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.show_widget_2)
        self.ui.pushButton_2.clicked.connect(self.show_widget_3)
        # self.ui.pushButton_3.clicked.connect(self.log_in)
        # self.ui.pushButton_5.clicked.connect(self.sig_up)

    def show_widget_2(self):
        self.ui.widget_2.show()
        self.ui.widget_3.hide()

    def show_widget_3(self):
        self.ui.widget_3.show()
        self.ui.widget_2.hide()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec_())