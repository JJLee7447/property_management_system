from UI.login_su_ui import Ui_login
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from src.db_config import db_connect
from src.mainwindow import MainWindow

def login_fuc(property_id, password):
    conn = db_connect()
    cursor = conn.cursor()
    # 使用参数化查询，防止 SQL 注入攻击
    sql = 'SELECT property_id, position,pass_word FROM property_staff WHERE property_id = %s;'
    cursor.execute(sql, (property_id,))
    res = cursor.fetchone()
    if res:
        stored_property_id, position, stored_password = res
        if password == stored_password and position == '管理员':
            # 验证成功
            print("登录成功")
            cursor.close()
            conn.close()
            return True
            # 执行登录成功后的操作
        elif position != '管理员':
            # 密码错误
            print('只有管理员才能使用')
            cursor.close()
            conn.close()
            return False
            # 执行登录失败后的操作
        elif password != stored_password:
            # 密码错误
            print("密码错误")
            cursor.close()
            conn.close()
            return False
            # 执行登录失败后的操作
    else:
        # 用户不存在
        print("用户不存在")
        cursor.close()
        conn.close()
        return False
        # 执行登录失败后的操作

def sig_up_fuc(staff_id, pd):
    conn = db_connect()
    cursor = conn.cursor()
    try:
        sql = '''INSERT INTO property_staff (property_id, position, staff_name, pass_word) VALUES (%s, %s, %s, %s)'''
        values = (staff_id, '管理员', 'property_name', pd)  # 根据实际情况设置 position_value 和 property_name_value 的值
        select = '''SELECT property_id FROM property_staff WHERE property_id = %s'''
        cursor.execute(select, (staff_id,))
        res = cursor.fetchone()
        if res:
            print("用户已存在")
            cursor.close()
            conn.close()
            return False
        else:
            cursor.execute(sql, values)
            conn.commit()
            conn.close()
    except Exception as e:
        print(e)
        conn.rollback()
        conn.close()
        return False

    else:
        print("注册成功")
        return True


class LoginSu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_login()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.show_widget_2)
        self.ui.pushButton_2.clicked.connect(self.show_widget_3)
        self.ui.pushButton_3.clicked.connect(self.log_in)
        self.ui.pushButton_5.clicked.connect(self.sig_up)

    def show_widget_2(self):
        self.ui.widget_2.show()
        self.ui.widget_3.hide()

    def show_widget_3(self):
        self.ui.widget_3.show()
        self.ui.widget_2.hide()

    def log_in(self):
        print("log in")
        property_id = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        print(property_id)
        print(password)
        if login_fuc(password=password, property_id=property_id):
            self.win = MainWindow()
            self.win.show()
            self.close()

    def sig_up(self):
        print("sig up")
        staff_id = self.ui.lineEdit_3.text()
        pd = self.ui.lineEdit_4.text()
        pd2 = self.ui.lineEdit_5.text()
        if pd == pd2:
            sig_up_fuc(staff_id=staff_id, pd=pd)
        else:
            print("两次密码不一致")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_su = LoginSu()
    login_su.ui.widget_3.hide()
    login_su.show()
    sys.exit(app.exec_())