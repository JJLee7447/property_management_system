from src.login_su import LoginSu
import sys
from PyQt5.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginSu()
    login.ui.widget_3.hide()
    login.show()
    sys.exit(app.exec_())
