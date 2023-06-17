from UI.login_su_ui import Ui_login
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from src.db_config import db_connect
from src.mainwindow import MainWindow
from User.src.User_mianWind import UserMainWind
import re
def login_fuc(property_id, password)->bool:
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

def User_login_fuc(email)->bool:
    conn = db_connect()
    cursor = conn.cursor()
    # 使用参数化查询，防止 SQL 注入攻击
    sql = 'SELECT email FROM residents WHERE email = %s;'
    cursor.execute(sql, (email,))
    res = cursor.fetchone()
    return bool(res)



class LoginSu(Ui_login, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.win = None
        self.User_win = None

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.pushButton.clicked.connect(self.show_widget_2)
        self.pushButton_2.clicked.connect(self.show_widget_3)
        self.pushButton_3.clicked.connect(self.log_in)
        self.pushButton_5.clicked.connect(self.check_pw)


    def show_widget_2(self):
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.widget_2.show()
        self.widget_3.hide()

    def show_widget_3(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.widget_3.show()
        self.widget_2.hide()

    def log_in(self):
        print("log in")
        property_id = self.lineEdit.text()
        password = self.lineEdit_2.text()
        print(property_id)
        print(password)
        pattern = re.compile(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$')
        try:
            # 用户登录
            if pattern.match(property_id):
                print("邮箱登录")
                if User_login_fuc(property_id):
                    self.User_win = UserMainWind()
                    self.User_win.set_person_info(property_id)
                    self.User_win.show()
                    self.close()
                else:
                    print("邮箱不存在")
            # 管理员登录
            elif login_fuc(password=password, property_id=property_id):
                self.win = MainWindow()
                self.win.show()
                self.close()
        except Exception as e:
            print(e)

        else:
            print('登录成功')


    def check_pw(self):
        print("sig up")
        staff_id = self.lineEdit_3.text()
        pd = self.lineEdit_4.text()
        pd2 = self.lineEdit_5.text()
        if pd == pd2:
            sig_up_fuc(staff_id=staff_id, pd=pd)
        else:
            print("两次密码不一致")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_su = LoginSu()
    login_su.widget_3.hide()
    login_su.show()
    sys.exit(app.exec_())