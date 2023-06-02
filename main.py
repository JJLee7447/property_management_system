from src.login import login_wid
import sys
from PyQt5.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = login_wid()
    login.show()
    sys.exit(app.exec_())
