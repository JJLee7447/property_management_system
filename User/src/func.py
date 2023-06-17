# -*- coding: utf-8 -*-
from PyQt5.QtGui import QFont
from src.db_config import db_connect

def setFont(label):
    font = QFont()
    font.setFamily("微软雅黑")
    font.setPointSize(12)
    label.setFont(font)
    # 背景灰色

    label.setStyleSheet("color: rgb(0, 0, 0);" "background-color: rgb(226, 226, 226);")

def find_building_id_house_id(resident_id):
    conn = db_connect()
    cursor = conn.cursor()
    sql = '''SELECT building_id, house_id FROM build_house_resident WHERE resident_id = %s'''
    cursor.execute(sql, (resident_id,))
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return res


def Get_due_paid_fee(property_id):
    conn = db_connect()
    cursor = conn.cursor()
    print(f'住户编号为{property_id}')
    try:
        sql = '''SELECT property_fee FROM house WHERE resident_id = %s ;'''
        cursor.execute(sql, (property_id,))
        res = cursor.fetchone()
        if res is None:
            print('查询结果为空')
            return False
        else:
            return res[0]

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def check_is_property_fee_paid(self, year, month, ):
    house_id = self.house_id_comboBox.currentText()
    conn = db_connect()
    cursor = conn.cursor()
    try :
        sql = '''SELECT is_paid FROM property_fees WHERE  house_id = %s AND year = %s AND month = %s ;'''
        cursor.execute(sql, (house_id, year, month))
        res = cursor.fetchone()
        print(res)
        if res is None:
            return False
        else:
            return True
    except Exception as e:
        print(e)
    else:
        print('查询成功')
    finally:
        cursor.close()
        conn.close()


def Get_staff_id(building_id):
    conn = db_connect()
    cursor = conn.cursor()
    try:
        sql = '''SELECT property_id FROM buildings WHERE building_id = %s ;'''
        cursor.execute(sql, (building_id,))
        res = cursor.fetchone()
        if res is None:
            return False
        else:
            return res[0]

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def check_is_parking_fee_paid(year, month, parking_space_id) -> bool:
    conn = db_connect()
    cursor = conn.cursor()
    try :
        sql = '''SELECT is_paid FROM parking_fees WHERE   year = %s AND month = %s AND parking_space_id = %s ;'''
        cursor.execute(sql, (year, month, parking_space_id))
        res = cursor.fetchone()
        print(f'function_check_is_parking_fee_paid: {res}')
        if res is None:
            return False
        else:
            return True
    except Exception as e:
        print(e)
    else:
        print('查询成功')
    finally:
        cursor.close()
        conn.close()


def Get_parking_space_id(resident_id):
    conn = db_connect()
    cursor = conn.cursor()
    try:
        sql = '''SELECT parking_space_id FROM parking_spaces WHERE resident_id = %s ;'''
        cursor.execute(sql, (resident_id,))
        res = cursor.fetchall()
        if res is None:
            return False
        else:
            return res

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def Get_due_pay_parking_fee(parking_space_id):
    conn = db_connect()
    cursor = conn.cursor()
    try:
        sql = '''SELECT parking_fee, building_id FROM parking_spaces WHERE parking_space_id = %s ;'''
        cursor.execute(sql, (parking_space_id,))
        res = cursor.fetchall()
        if res is None:
            return False
        else:
            return res

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def Use_house_id_Get_building_id(house_id):
    conn = db_connect()
    cursor = conn.cursor()
    try:
        sql = '''SELECT building_id FROM house WHERE house_id = %s ;'''
        cursor.execute(sql, (house_id,))
        res = cursor.fetchone()
        if res is None:
            return False
        else:
            return res[0]

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()